from reportlab.pdfgen import canvas

from .elo_service import EloService
from .match_service import MatchService


class PdfService:
    "This class is responsible for generating the PDF report of the data in the app"

    def __init__(
        self,
    ):
        self.elo_service = EloService()
        self.match_service = MatchService()

    def generate_pdf(self):
        """
        Generates a PDF report of the matches played.
        """

        users = self.elo_service.get_all_users()
        matches = self.match_service.get_all_matches()

        c = canvas.Canvas("PDF-export.pdf", pagesize=(595.27, 841.89))  # A4 pagesize
        # draw a string at x=100, y=800 points
        # point ~ standard desktop publishing (72 DPI)
        # coordinate system:
        #   y
        #   |
        #   |   page
        #   |
        #   |
        #   0-------x

        # set title
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, 800, "FIFA Eloranking PDF Report")

        # set subtitle
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 770, "Users")

        # set font for user list
        c.setFont("Helvetica", 12)
        # start y position for the user list from 740
        y = 740
        line_height = 20

        # check if there are any users to display
        if not users:
            c.drawString(50, y, "No users found.")
        else:
            # iterate through users and print their name and Elo rating
            for user in users:
                if len(user.name) > 40:
                    # if name too long, show only first 10 characters and add "..."
                    user.name = user.name[:20] + "..."
                c.drawString(50, y, f"Name: {user.name}")
                c.drawString(400, y, f"Elo ranking: {user.elo_rating}")
                y -= line_height
            # if the y position is too low, start a new page
            if y < 50:
                c.showPage()
                y = 800
                c.setFont("Helvetica", 12)

        # set subtitle
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y - 50, "Matches")
        y -= 70

        # set font for match list
        c.setFont("Helvetica", 12)

        if not matches:
            c.drawString(50, y, "No matches found.")
        else:
            for match in matches:
                winner_name = self.elo_service.find_user_by_id(match.winner).name
                loser_name = self.elo_service.find_user_by_id(match.loser).name

            # if name too long, show only first 10 characters and add "..."
            max_name_length = 15
            if len(winner_name) > max_name_length:
                winner_name = winner_name[:max_name_length] + "..."
            if len(loser_name) > max_name_length:
                loser_name = loser_name[:max_name_length] + "..."

            c.drawString(50, y, f"Winner: {winner_name}")
            c.drawString(200, y, f"Loser: {loser_name}")
            c.drawString(400, y, f"Date: {match.date}")
            y -= line_height

            # if the y position is too low, start a new page
            if y < 50:
                c.showPage()
                y = 800
                c.setFont("Helvetica", 12)

        # finish page
        c.showPage()
        # construct and save file to .pdf
        c.save()
