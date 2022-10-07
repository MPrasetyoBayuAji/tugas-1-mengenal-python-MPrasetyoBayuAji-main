from unittest import TestCase
from tugas1 import hitung_luas_lingkaran


class TestTugas1LuasLingkaran(TestCase):
    def test_luas_lingkaran(self):
        self.assertAlmostEqual(hitung_luas_lingkaran(5), 78.5398, places=4)
        self.assertAlmostEqual(hitung_luas_lingkaran(6), 113.0973, places=4)
