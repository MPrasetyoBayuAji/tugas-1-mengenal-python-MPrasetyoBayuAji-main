from unittest import TestCase
from tugas1 import cari_angka_duplikat


class TestTugas1CariAngkaDuplikat(TestCase):
    def test_cari_angka_duplikat(self):
        self.assertEqual(cari_angka_duplikat([1, 2, 3]), [])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1]), [1])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1, 2]), [1, 2])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1, 2, 3, 1, 2]), [1, 2, 3])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]), [1, 2, 3])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(cari_angka_duplikat([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 3, 1]), [1, 2, 3, 4, 5])