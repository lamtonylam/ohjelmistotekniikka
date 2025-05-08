from tkinter import Tk

from ui.ui import UI


def main():
    """
    Initializes and starts the main application window.

    Creates a Tkinter window, sets its title, initializes the UI view, 
    and starts the main event loop.
    """
    window = Tk()
    window.title("Football Game Elo Rating App")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
