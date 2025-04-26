from tkinter import ttk, constants


class HelloView:
    def __init__(self, root, handle_show_match_recording_view, handle_pdf_export_view):
        self._root = root
        self._handle_good_bye = handle_show_match_recording_view
        self._handle_pdf_export_view = handle_pdf_export_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Welcome to use the FIFA Elo rating calculator!",
            font=("Helvetica", 18, "bold"),
        )
        button = ttk.Button(
            master=self._frame, text="Record a match", command=self._handle_good_bye
        )
        button2 = ttk.Button(
            master=self._frame,
            text="Export to PDF",
            command=self._handle_pdf_export_view,
        )
        label.pack(pady=10)
        button.pack(pady=10)
        button2.pack(pady=10)
