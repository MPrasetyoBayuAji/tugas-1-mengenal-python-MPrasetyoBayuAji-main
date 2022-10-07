from unittest import TestCase
from tugas1 import hitung_faktorial


class TestTugas1Faktorial(TestCase):
    def test_faktorial(self):
        self.assertEqual(hitung_faktorial(1), 1)
        self.assertEqual(hitung_faktorial(2), 2)
        self.assertEqual(hitung_faktorial(3), 6)
        self.assertEqual(hitung_faktorial(4), 24)
        self.assertEqual(hitung_faktorial(5), 120)
        self.assertEqual(hitung_faktorial(6), 720)
        self.assertEqual(hitung_faktorial(7), 5040)
        self.assertEqual(hitung_faktorial(8), 40320)
        self.assertEqual(hitung_faktorial(9), 362880)
        self.assertEqual(hitung_faktorial(10), 3628800)