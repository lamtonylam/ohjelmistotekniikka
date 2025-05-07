from tkinter import ttk, constants, filedialog
from services.pdf_service import PdfService


class PdfExportView:
    """View for exporting players and matches to PDF."""

    def __init__(self, root, handle_hello_view):
        """Initialize the PDF export view.
        Args:
            root: The root window.
            handle_hello_view: Function to handle returning to the hello view.
        """
        self._root = root
        self.handle_hello_view = handle_hello_view
        self._frame = None
        self._initialize()

        self._pdf_service = PdfService()

    def pack(self):
        """
        Packs the internal frame widget.
        """
        self._frame.pack(fill=constants.X)

    def handle_pdf_export(self):
        """
        Opens a file dialog for the user to select a location to save a PDF file.
        If a file path is selected, calls the PDF service to generate and save the PDF at the specified location.
        """
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save PDF as",
        )
        if file_path:
            self._pdf_service.generate_pdf(file_path)

    def destroy(self):
        """
        Destroys the associated widget, effectively removing it from the UI.
        """
        self._frame.destroy()

    def _initialize(self):
        """
        Initializes the PDF export view UI components.

        Creates and packs a frame containing:
            - A label describing the export functionality.
            - A button to trigger PDF export.
            - A button to return to the home view.
        """
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Export players and matches to PDF",
            font=("Helvetica", 18, "bold"),
        )
        export_to_pdf_button = ttk.Button(
            master=self._frame, text="Export to pdf", command=self.handle_pdf_export
        )

        return_home_button = ttk.Button(
            master=self._frame, text="Return to home", command=self.handle_hello_view
        )

        label.pack(pady=10)
        export_to_pdf_button.pack(pady=10)
        return_home_button.pack(pady=10)
