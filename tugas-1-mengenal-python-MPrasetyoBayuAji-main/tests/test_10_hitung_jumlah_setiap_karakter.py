from unittest import TestCase
from tugas1 import hitung_jumlah_setiap_karakter


class TestTugas1JumlahKarakter(TestCase):
    def test_jumlah_karakter(self):
        self.assertEqual(hitung_jumlah_setiap_karakter("a"), {"a": 1})
        self.assertEqual(hitung_jumlah_setiap_karakter("aa"), {"a": 2})
        self.assertEqual(hitung_jumlah_setiap_karakter("ab"), {"a": 1, "b": 1})
        self.assertEqual(hitung_jumlah_setiap_karakter("aab"), {"a": 2, "b": 1})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabb"), {"a": 2, "b": 2})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabbcc"), {"a": 2, "b": 2, "c": 2})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabbccdd"), {"a": 2, "b": 2, "c": 2, "d": 2})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabbccdde"), {"a": 2, "b": 2, "c": 2, "d": 2, "e": 1})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabbccddeef"), {"a": 2, "b": 2, "c": 2, "d": 2, "e": 2, "f": 1})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabbccddeeff"), {"a": 2, "b": 2, "c": 2, "d": 2, "e": 2, "f": 2})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabbccddeeffg"), {"a": 2, "b": 2, "c": 2, "d": 2, "e": 2, "f": 2, "g": 1})
        self.assertEqual(hitung_jumlah_setiap_karakter("aabbccddeeffgg"), {"a": 2, "b": 2, "c": 2, "d": 2, "e": 2, "f": 2, "g": 2})