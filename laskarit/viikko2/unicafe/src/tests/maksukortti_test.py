import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_kortti_luodaan_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortin_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_kortilta_rahan_ottaminen_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)

    def test_kortilta_rahan_ottaminen_ei_vahenna_saldoa_jos_ei_riittavasti(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortilta_rahan_ottaminen_palauttaa_oikean_arvon(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
