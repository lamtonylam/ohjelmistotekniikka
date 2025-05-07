from tkinter import Tk
from ui.views.hello_view import HelloView
from ui.views.match_recording_view import MatchRecordingView
from ui.views.pdf_export_view import PdfExportView


class UI:
    """Main UI class for the application."""

    def __init__(self, root):
        """
        Initializes the UI class with the given root window.

        Args:
            root: The root window or main application window to attach the UI to.

        Attributes:
            _root: Stores the reference to the root window.
            _current_view: Keeps track of the currently active view in the UI.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """
        Initializes the main application window.
        """
        self._root.geometry("")
        self._root.update_idletasks()
        self._show_hello_view()

    def _hide_current_view(self):
        """
        Hides the currently active view in the UI.
        By destroying the current view.
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_match_recording_view(self):
        """
        Handles the transition to the match recording view by invoking the method that displays it.
        """
        self._show_match_recording_view()

    def _handle_pdf_export_view(self):
        """
        Handles the transition to the PDF export view in the UI.

        This method is responsible for displaying the PDF export interface
        by invoking the appropriate view rendering function.
        """
        self._show_pdf_export_view()

    def _handle_hello_view(self):
        """
        Handles the logic for displaying the hello view.

        This method calls the internal method to show the hello view to the user.
        """
        self._show_hello_view()

    def _show_hello_view(self):
        """
        Displays the HelloView in the UI.

        Hides the currently displayed view, creates a new instance of HelloView with the
        root window and appropriate handler callbacks, and packs it to make it visible.
        """
        self._hide_current_view()

        self._current_view = HelloView(
            self._root, self._handle_match_recording_view, self._handle_pdf_export_view
        )

        self._current_view.pack()

    def _show_match_recording_view(self):
        """
        Displays the match recording view in the UI.

        This method hides the currently visible view, initializes a new
        MatchRecordingView instance, and starts it. The new view is set as
        the current view. The view is initialized with the root window and
        a callback handler for returning to the hello view.
        """
        self._hide_current_view()

        self._current_view = MatchRecordingView(self._root, self._handle_hello_view)

        self._current_view.start()

    def _show_pdf_export_view(self):
        """
        Displays the PDF export view in the UI.

        This method hides the currently active view and replaces it with an instance
        of PdfExportView. The new view is initialized with the root window and a callback
        to handle returning to the previous view. The PDF export view is then packed
        and displayed to the user.
        """
        self._hide_current_view()

        self._current_view = PdfExportView(self._root, self._handle_hello_view)

        self._current_view.pack()
