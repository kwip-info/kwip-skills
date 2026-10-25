"""Review-sized source allowlist and leakage checks; never prints matched contents."""
import argparse,json,re,subprocess
from pathlib import Path

SKILLS=('workspace-operations','design-led-development','component-boundaries','verification-strategy','bounded-work-tracking')
ALLOWED={'README.md','LICENSE','.gitignore','scripts/validate_publication.py','tests/test_publication.py',
         'skills/component-boundaries/references/boundary-record.md',
         *('skills/'+name+'/SKILL.md' for name in SKILLS)}
PATTERNS={
    'private-home-path':re.compile('/'+'Users'+r'/[^\s/]+/'),
    'private-volume-path':re.compile('/'+'Volumes'+r'/[^\s]+'),
    'credential':re.compile(r'gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk_live_[A-Za-z0-9]{16,}|-----BEGIN (?:[A-Z ]+)?PRIVATE KEY-----'),
    'email-address':re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',re.I),
    'unreviewed-identity':re.compile(r'\b[0-9a-f]{40,64}\b|\bAW-[0-9]{8,}\b'),
}


def inspect_bytes(name,raw):
    errors=[]
    if len(raw)>65536:return [name+': file exceeds review budget']
    try:text=raw.decode('utf-8')
    except UnicodeDecodeError:return [name+': binary content refused']
    if '\0' in text:errors.append(name+': binary content refused')
    for category,pattern in PATTERNS.items():
        if pattern.search(text):errors.append(name+': '+category)
    return errors


def validate(root,staged=False):
    root=Path(root).resolve();errors=[];actual=set();total=0
    for path in root.rglob('*'):
        relative=path.relative_to(root)
        if any(p in ('.git','__pycache__','.pytest_cache') for p in relative.parts) or path.name=='.DS_Store':continue
        if path.is_symlink():errors.append(str(relative)+': symlink refused');continue
        if not path.is_file():continue
        name=relative.as_posix();actual.add(name)
        if name not in ALLOWED:errors.append(name+': unreviewed export path');continue
        size=path.stat().st_size;total+=size
        if size>65536:errors.append(name+': file exceeds review budget');continue
        errors+=inspect_bytes(name,path.read_bytes())
    if actual!=ALLOWED:errors.append('Export file set differs from reviewed allowlist')
    if total>256000:errors.append('Package exceeds review budget')
    for name in SKILLS:
        path=root/'skills'/name/'SKILL.md'
        if not path.is_file() or path.is_symlink():continue
        raw=path.read_text()
        parts=raw.split('---',2)
        if len(parts)!=3 or not parts[1].strip().startswith('name: '+name+'\n') or not re.search(r'^description: .+',parts[1],re.M):
            errors.append(name+': invalid skill identity/frontmatter')
        for target in re.findall(r'\]\(([^)]+)\)',raw):
            if '://' in target:continue
            linked=(path.parent/target).resolve()
            if not linked.is_relative_to(root) or not linked.is_file():errors.append(name+': unresolved or escaping reference')
    if staged:
        names=set(filter(None,subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')))
        if names!=ALLOWED:errors.append('Git index differs from reviewed export')
        for name in sorted(names&ALLOWED):
            size=int(subprocess.check_output(['git','cat-file','-s',':'+name],cwd=root))
            if size>65536:errors.append(name+': oversized staged blob');continue
            blob=subprocess.check_output(['git','show',':'+name],cwd=root)
            errors+=inspect_bytes(name,blob)
            if blob!=(root/name).read_bytes():errors.append(name+': staged bytes differ from reviewed source')
    return sorted(set(errors))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--staged',action='store_true');a=p.parse_args()
    errors=validate(a.root,a.staged);print(json.dumps({'passed':not errors,'files':len(ALLOWED),'errors':errors}));raise SystemExit(bool(errors))
