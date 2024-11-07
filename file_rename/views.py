# -*- coding: utf-8 -*-
# rprename/views.py

"""This module provides the File Renamer main window."""

from collections import deque
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog, QWidget
from ui.window import Ui_Window

FILTERS = ";;".join(
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "Text Files (*.txt)",
        "Python Files (*.py)",
    )
)


class Window(QWidget, Ui_Window):

    def __init__(self):
        super().__init__()

        # stack-like object; can append + pop on front and back
        self._files = deque()
        self._files_count = len(self._files)
        self._setup_UI()
        self._connect_signals_slots()

    def _setup_UI(self):
        self.setupUi(self)

    def _connect_signals_slots(self):
        self.load_files_button.clicked.connect(self.load_files)

    def load_files(self):
        pass
