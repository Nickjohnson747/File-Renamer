# -*- coding: utf-8 -*-
# file_rename/app.py

"""This module provides the File Renamer application."""

import sys
from PyQt5.QtWidgets import QApplication
from views import Window


def main():
    # create the application
    app = QApplication(sys.argv)

    # create and show the main window
    win = Window()
    win.show()

    # run the event loop
    sys.exit(app.exec())
