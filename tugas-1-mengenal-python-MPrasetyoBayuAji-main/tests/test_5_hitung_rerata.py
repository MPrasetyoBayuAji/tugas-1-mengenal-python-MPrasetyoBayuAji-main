from unittest import TestCase
from tugas1 import hitung_rerata


class TestTugas1Rerata(TestCase):
    def test_rerata(self):
        self.assertEqual(hitung_rerata([1, 2, 3]), 2.0)
        self.assertEqual(hitung_rerata([1, 2, 3, 4]), 2.5)
        self.assertEqual(hitung_rerata([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(hitung_rerata([1, 2, 3, 4, 5, 6]), 3.5)