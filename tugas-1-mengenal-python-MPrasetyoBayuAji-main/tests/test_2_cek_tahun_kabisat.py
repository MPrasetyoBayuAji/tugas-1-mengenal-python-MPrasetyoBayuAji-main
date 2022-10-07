from unittest import TestCase
from tugas1 import cek_tahun_kabisat


class TestTugas1TahunKabisat(TestCase):
    def test_kabisat(self):
        self.assertTrue(cek_tahun_kabisat(2000))
    def test_bukan_kabisat(self):
        self.assertEqual(cek_tahun_kabisat(2001), False)
