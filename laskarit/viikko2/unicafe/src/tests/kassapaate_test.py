from kassapaate import Kassapaate
from maksukortti import Maksukortti
import unittest


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(500)

    def test_kassan_raha_euroina_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassapaate_luodaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisella_syo_edullisesti_riittava_maksu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_syo_edullisesti_ei_riittava_maksu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisella_syo_maukkaasti_riittava_maksu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisella_syo_maukkaasti_ei_riittava_maksu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_syo_edullisesti_riittava_saldo(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_syo_edullisesti_ei_riittava_saldo(self):
        self.kortti.ota_rahaa(300)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortilla_syo_maukkaasti_riittava_saldo(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_syo_maukkaasti_ei_riittava_saldo(self):
        self.kortti.ota_rahaa(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.00 euroa")

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_lataa_negatiivinen_summa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 5.00 euroa")
