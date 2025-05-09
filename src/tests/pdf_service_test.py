import unittest
import os
import pymupdf
from build import build

from services.pdf_service import PdfService
from services.elo_service import EloService
from services.match_service import MatchService


class TestPDFGeneration(unittest.TestCase):

    def setUp(self):
        build()
        self.pdfservice = PdfService()
        self.user_service = EloService()
        self.match_service = MatchService()
        self.tmp_path = "test.pdf"

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            os.remove(self.tmp_path)

    def test_pdf_file_is_created(self):
        self.pdfservice.generate_pdf(self.tmp_path)

        self.assertTrue(os.path.exists(self.tmp_path))

        self.assertGreater(os.path.getsize(self.tmp_path), 0)

    def test_pdf_file_has_players_and_matches(self):

        self.user_service.create_user("tomppa")
        self.user_service.create_user("tomppa1")

        self.match_service.create_match("tomppa", "tomppa1")

        self.pdfservice.generate_pdf(self.tmp_path)

        doc = pymupdf.open(self.tmp_path)
        text = ""
        for page in doc:
            text = text + page.get_text()

        self.assertIn("Winner: tomppa", text)
        self.assertIn("Loser: tomppa1", text)
        self.assertIn("Elo ranking: 1516", text)
        self.assertIn("Elo ranking: 1484", text)

    def test_pdf_file_with_long_player_names(self):

        player1_username = (
            "1" * 50
        )
        player2_username = (
            "2" * 50
        )
        self.user_service.create_user(player1_username)
        self.user_service.create_user(player2_username)

        self.match_service.create_match(player1_username, player2_username)
        
        self.pdfservice.generate_pdf(self.tmp_path)

        doc = pymupdf.open(self.tmp_path)
        text = ""
        for page in doc:
            text = text + page.get_text()
        
        self.assertIn("1" * 20, text)
        self.assertIn("2" * 20, text)
        
        self.assertIn("Winner: " + "1" * 15 + "...", text)
        self.assertIn("Loser: " + "2" * 15 + "...", text)

