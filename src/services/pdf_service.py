from reportlab.pdfgen import canvas

from repositories.match_repository import match_repository as default_match_repository
from repositories.user_repository import user_repository as default_user_repository
from .elo_service import EloService


class PdfService:
    "This class is responsible for generating the PDF report of the data in the app"

    def __init__(
        self,
        match_repository=default_match_repository,
        user_repostory=default_user_repository,
    ):
        self.match_repository = match_repository
        self._user_repository = user_repostory
        self.elo_service = EloService()

    def generate_pdf(self):
        """
        Generates a PDF report of the matches played.
        """
        c = canvas.Canvas(
            "PDF-export.pdf", pagesize=(595.27, 841.89)
        )  # A4 pagesize
        # draw a string at x=100, y=800 points
        # point ~ standard desktop publishing (72 DPI)
        # coordinate system:
        #   y
        #   |
        #   |   page
        #   |
        #   |
        #   0-------x
        c.drawString(50, 780, "FIFA Eloranking")
        # finish page
        c.showPage()
        # construct and save file to .pdf
        c.save()
