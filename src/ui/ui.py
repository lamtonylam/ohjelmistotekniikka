from tkinter import Tk
from ui.views.hello_view import HelloView
from ui.views.match_recording_view import MatchRecordingView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._root.geometry("600x600")
        self._show_hello_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_match_recording_view(self):
        self._show_match_recording_view()

    def _handle_hello_view(self):
        self._show_hello_view()

    def _show_hello_view(self):
        self._hide_current_view()

        self._current_view = HelloView(self._root, self._handle_match_recording_view)

        self._current_view.pack()

    def _show_match_recording_view(self):
        self._hide_current_view()

        self._current_view = MatchRecordingView(self._root, self._handle_hello_view)

        self._current_view.start()
