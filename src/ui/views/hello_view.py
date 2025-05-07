from tkinter import ttk, constants


class HelloView:
    """Class to create the Welcome / Home view of the application"""

    def __init__(self, root, handle_show_match_recording_view, handle_pdf_export_view):
        """
        Initializes the HelloView class.

        Args:
            root: The root Tkinter widget or window.
            handle_show_match_recording_view : function to handle showing the match recording view.
            handle_pdf_export_view: function to handle exporting data to PDF.
        """
        self._root = root
        self._handle_good_bye = handle_show_match_recording_view
        self._handle_pdf_export_view = handle_pdf_export_view
        self._frame = None

        self._initialize()

    def pack(self):
        """
        Packs the frame widget into its parent widget.

        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """
        Destroys the frame associated with this view, removing it from the UI.
        """
        self._frame.destroy()

    def _initialize(self):
        """
        Initializes the main frame of the HelloView UI.

        Creates and packs a welcome label and two buttons:
        - "Record a match": triggers the _handle_good_bye to show match recording view.
        - "Export to PDF": triggers the _handle_pdf_export_view to show pdf exporting view.

        """
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
