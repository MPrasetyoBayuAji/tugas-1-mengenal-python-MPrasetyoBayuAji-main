from unittest import TestCase
from tugas1 import cari_angka_terbesar


class TestTugas1CariAngkaTerbesar(TestCase):
    def test_cari_angka_terbesar(self):
        self.assertEqual(cari_angka_terbesar([1, 2, 3]), 3)
        self.assertEqual(cari_angka_terbesar([1, 3, 2]), 3)
        self.assertEqual(cari_angka_terbesar([2, 1, 3]), 3)
        self.assertEqual(cari_angka_terbesar([2, 3, 1]), 3)
        self.assertEqual(cari_angka_terbesar([3, 1, 2]), 3)
        self.assertEqual(cari_angka_terbesar([3, 2, 1]), 3)
        self.assertEqual(cari_angka_terbesar([1, 2, 3, 4]), 4)
        self.assertEqual(cari_angka_terbesar([1, 2, 4, 3]), 4)
        self.assertEqual(cari_angka_terbesar([1, 4, 2, 3]), 4)
        self.assertEqual(cari_angka_terbesar([1, 4, 3, 2]), 4)
        self.assertEqual(cari_angka_terbesar([4, 1, 2, 3]), 4)
        self.assertEqual(cari_angka_terbesar([4, 1, 3, 2]), 4)
        self.assertEqual(cari_angka_terbesar([4, 3, 1, 2]), 4)
        self.assertEqual(cari_angka_terbesar([4, 3, 2, 1]), 4)
        self.assertEqual(cari_angka_terbesar([1, 2, 3, 4, 5]), 5)
        self.assertEqual(cari_angka_terbesar([1, 2, 3, 5, 4]), 5)
        self.assertEqual(cari_angka_terbesar([1, 2, 5, 3, 4]), 5)
        self.assertEqual(cari_angka_terbesar([1, 2, 5, 4, 3]), 5)
        self.assertEqual(cari_angka_terbesar([1, 5, 2, 3, 4]), 5)