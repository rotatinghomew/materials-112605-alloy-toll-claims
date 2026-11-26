"""核对交换资料中的实体引用与原始回执顺序。"""
from datetime import datetime
import json
from pathlib import Path
import unittest

from partner import parse_time as time

ROOT = Path(__file__).resolve().parents[1]


class ExchangeTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "fixtures" / "exchange.json").read_text(encoding="utf-8"))

    def test_record_identity(self):
        for name, collection in self.data.items():
            with self.subTest(collection=name):
                ids = [rec["id"] for rec in collection]
                self.assertTrue(ids)
                self.assertTrue(all(isinstance(i, str) and i for i in ids))
                self.assertEqual(len(ids), len(set(ids)))
                self.assertTrue(all(set(x) == set(collection[0]) for x in collection))

    def test_receipt_clocks(self):
        for rec in self.data["receipts"]:
            with self.subTest(receipt=rec["id"]):
                self.assertLessEqual(time(rec["happened"]), time(rec["arrived"]))
        with self.assertRaises(ValueError):
            time(datetime(2027, 1, 18).isoformat())

    def test_related_records(self):
        def row(collection, key):
            return next(rec for rec in self.data[collection] if rec["id"] == key)
        assert row("feed","F-2")["owner"] != row("feed","F-2")["depositor"]
        assert row("feed","F-4")["delivered"] is None
        assert row("feed","F-2")["alloy"] == row("heats","H1")["alloy"]
        assert row("taps",row("assay","Y-4")["tap"])["heat"] == "H1"
        cutoff = row("heats","H1")["threshold_h"]
        assert row("assay","Y-4")["purity"] < cutoff < row("assay","Y-2")["purity"]
        original = row("receipts","WG-1")
        assert original["qty"] < row("claims",original["claim"])["qty"]
        assert time(original["happened"]) < time(row("assay","Y-4")["happened"]) < time(original["arrived"])
