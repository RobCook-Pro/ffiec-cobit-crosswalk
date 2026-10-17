import contextlib
import io
import unittest
from pathlib import Path

import crosswalk as cw

ROOT = Path(__file__).resolve().parent


class TestCrosswalk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.xw = cw.Crosswalk()

    def test_data_is_valid(self):
        self.assertEqual(self.xw.validate(), [])

    def test_every_expectation_has_primary(self):
        for e in self.xw.expectations:
            self.assertTrue(any(m.strength == "primary" for m in self.xw.maps_for(e.id)), e.id)

    def test_forward_and_reverse_agree(self):
        for m in self.xw.mappings:
            self.assertIn(m, self.xw.ffiec_for(m.objective))

    def test_practice_lookup_includes_parent_objective_mappings(self):
        ids = {m.ffiec_id for m in self.xw.ffiec_for("DSS04.07")}
        self.assertIn("BCM-03", ids)

    def test_gap_logic(self):
        rows = {r["ffiec_id"]: r for r in self.xw.gap({"BAI06": (4, 4)})}
        self.assertEqual(rows["IS-09"]["status"], "meets")          # only primary is BAI06
        self.assertEqual(rows["IS-06"]["status"], "not_assessed")   # DSS05 missing
        rows = {r["ffiec_id"]: r for r in self.xw.gap({"BAI06": (2, 4)})}
        self.assertEqual(rows["IS-09"]["status"], "gap")
        self.assertEqual(rows["IS-09"]["gap_levels"], 2)

    def test_supporting_mappings_do_not_create_gaps(self):
        # IS-09's supporting BAI10 is below target, but only primaries are scored.
        rows = {r["ffiec_id"]: r for r in self.xw.gap({"BAI06": (4, 4), "BAI10": (0, 5)})}
        self.assertEqual(rows["IS-09"]["status"], "meets")

    def test_sample_assessment_end_to_end(self):
        a = cw.load_assessment(ROOT / "examples" / "assessment.csv")
        rows = self.xw.gap(a)
        prios = self.xw.priorities(rows, a)
        self.assertEqual(prios[0]["objective"], "APO10")
        self.assertTrue(cw.md_gap(self.xw, rows, prios).startswith("# FFIEC"))

    def test_cli(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(cw.main(["validate"]), 0)
            self.assertEqual(cw.main(["lookup", "is-06"]), 0)
            self.assertEqual(cw.main(["lookup", "dss05"]), 0)
            self.assertEqual(cw.main(["lookup", "nope"]), 1)


if __name__ == "__main__":
    unittest.main()
