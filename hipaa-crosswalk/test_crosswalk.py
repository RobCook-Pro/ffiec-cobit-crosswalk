import unittest, sys
sys.path.insert(0, "src")
from crosswalk import score
class T(unittest.TestCase):
    def test_status(self):
        rows=[{"nist_800_53_r5":"AC-2;AC-3"},{"nist_800_53_r5":"IA-5"},{"nist_800_53_r5":"CP-9"}]
        inv=[{"nist_800_53_r5":"AC-2"},{"nist_800_53_r5":"IA-5"}]
        self.assertEqual([s["status"] for s in score(rows,inv)],["Partial","Covered","Gap"])
if __name__=="__main__": unittest.main()
