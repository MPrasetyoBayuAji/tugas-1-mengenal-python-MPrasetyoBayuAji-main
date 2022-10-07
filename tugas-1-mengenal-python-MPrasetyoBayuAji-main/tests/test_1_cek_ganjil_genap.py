from unittest import TestCase
from tugas1 import cek_ganjil_genap


class TestTugas1GanjilGenap(TestCase):
    def test_ganjil(self):
        self.assertEqual(cek_ganjil_genap(1), "ganjil")
    def test_genap(self):
        self.assertEqual(cek_ganjil_genap(2), "genap")
