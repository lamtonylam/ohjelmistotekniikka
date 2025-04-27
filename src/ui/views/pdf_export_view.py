from tkinter import ttk, constants, filedialog
from services.pdf_service import PdfService


class PdfExportView:
    def __init__(self, root, handle_hello_view):
        self._root = root
        self.handle_hello_view = handle_hello_view
        self._frame = None
        self._initialize()

        self._pdf_service = PdfService()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def handle_pdf_export(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save PDF as",
        )
        if file_path:
            self._pdf_service.generate_pdf(file_path)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
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
