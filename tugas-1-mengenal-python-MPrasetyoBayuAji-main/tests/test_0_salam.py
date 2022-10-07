from unittest import TestCase

from tugas1 import ucap_salam, beri_salam

class TestTugas1Salam(TestCase):
    def test_ucap_salam(self):
        self.assertEqual(ucap_salam(), "Assalamu'alaikum")
    def test_beri_salam(self):
        self.assertEqual(beri_salam("Budi"), "Assalamu'alaikum, Budi")