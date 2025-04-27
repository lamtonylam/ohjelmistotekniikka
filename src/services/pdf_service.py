from reportlab.pdfgen import canvas

from .elo_service import EloService
from .match_service import MatchService


class PdfService:
    "This class is responsible for generating the PDF report of the data in the app"

    def __init__(self):
        """Initializes the PdfService with EloService and MatchService"""
        self.elo_service = EloService()
        self.match_service = MatchService()

    def generate_pdf(self, filepath):
        """Generates a PDF report of the users and matches in the app"""
        users = self.elo_service.get_all_users()
        matches = self.match_service.get_all_matches()
        c = canvas.Canvas(filepath, pagesize=(595.27, 841.89))  # A4 pagesize

        self._draw_title(c)
        y = self._draw_users(c, users)
        y = self._draw_matches(c, matches, y)

        c.showPage()
        c.save()

    def _draw_title(self, c):
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, 800, "FIFA Eloranking PDF Report")

    def _draw_users(self, c, users):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 770, "Users")
        c.setFont("Helvetica", 12)
        y = 740
        line_height = 20

        if not users:
            c.drawString(50, y, "No users found.")
        else:
            for user in users:
                name = user.name
                if len(name) > 40:
                    name = name[:20] + "..."
                c.drawString(50, y, f"Name: {name}")
                c.drawString(400, y, f"Elo ranking: {user.elo_rating}")
                y -= line_height
                if y < 50:
                    c.showPage()
                    y = 800
                    c.setFont("Helvetica", 12)
        # return y position back to the caller to remember the last position
        return y

    def _draw_matches(self, c, matches, y):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y - 50, "Matches")
        y -= 70
        c.setFont("Helvetica", 12)
        line_height = 20

        if not matches:
            c.drawString(50, y, "No matches found.")
        else:
            for match in matches:
                y = self._draw_single_match(c, match, y, line_height)
        return y

    def _draw_single_match(self, c, match, y, line_height):
        winner_name = self.elo_service.find_user_by_id(match.winner).name
        loser_name = self.elo_service.find_user_by_id(match.loser).name
        max_name_length = 15
        if len(winner_name) > max_name_length:
            winner_name = winner_name[:max_name_length] + "..."
        if len(loser_name) > max_name_length:
            loser_name = loser_name[:max_name_length] + "..."
        c.drawString(50, y, f"Winner: {winner_name}")
        c.drawString(200, y, f"Loser: {loser_name}")
        c.drawString(400, y, f"Date: {match.date}")
        y -= line_height
        if y < 50:
            c.showPage()
            y = 800
            c.setFont("Helvetica", 12)
        return y
