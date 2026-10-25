"""Actual export faults: secrets/paths stay out of results and publication bytes."""
import importlib.util,shutil,tempfile,unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('publication',ROOT/'scripts/validate_publication.py')
publication=importlib.util.module_from_spec(spec);spec.loader.exec_module(publication)


class PublicationTests(unittest.TestCase):
    def fixture(self,folder):
        root=Path(folder)
        for name in publication.ALLOWED:
            path=root/name;path.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/name,path)
        return root
    def test_reviewed_export_is_complete_and_self_contained(self):
        with tempfile.TemporaryDirectory() as d:self.assertEqual(publication.validate(self.fixture(d)),[])
    def test_ignored_credential_file_still_refuses_export(self):
        with tempfile.TemporaryDirectory() as d:
            root=self.fixture(d);(root/'.env').write_text('private sentinel')
            self.assertTrue(publication.validate(root))
    def test_credential_and_private_path_are_not_echoed_by_diagnostics(self):
        for sentinel in ['ghp_'+'A'*36,'/'+'Users'+'/someone/private','/'+'Volumes'+'/private-disk/example']:
            with tempfile.TemporaryDirectory() as d:
                root=self.fixture(d);(root/'README.md').write_text(sentinel)
                errors=publication.validate(root);self.assertTrue(errors);self.assertNotIn(sentinel,str(errors))
    def test_symlink_does_not_export_an_external_document(self):
        with tempfile.TemporaryDirectory() as d,tempfile.TemporaryDirectory() as external:
            root=self.fixture(d);outside=Path(external)/'private.txt';outside.write_text('private sentinel')
            (root/'README.md').unlink();(root/'README.md').symlink_to(outside)
            self.assertTrue(publication.validate(root))
    def test_binary_oversize_and_missing_reference_refuse(self):
        for bad in [b'\0private',b'x'*65537]:
            with tempfile.TemporaryDirectory() as d:
                root=self.fixture(d);(root/'README.md').write_bytes(bad)
                self.assertTrue(publication.validate(root))
        with tempfile.TemporaryDirectory() as d:
            root=self.fixture(d);(root/'skills/component-boundaries/references/boundary-record.md').unlink()
            self.assertTrue(publication.validate(root))

if __name__=='__main__':unittest.main()
