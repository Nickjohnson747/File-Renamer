# -*- coding: utf-8 -*-
# file_rename/views.py

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
        self.dest_file_list.clear()
        if self.dir_edit.text():
            init_dir = self.dir_edit.text()
        else:
            init_dir = str(Path.home())

        files, filter = QFileDialog.getOpenFileNames(
            self, "Choose Files to Rename", init_dir, filter=FILTERS
        )
        if len(files) > 0:
            file_extension = filter[filter.index("*") : -1]
            self.extension_label.setText(file_extension)
            src_dir_name = str(Path(files[0]).parent)
            self.dir_edit.setText(src_dir_name)
            for file in files:
                self._files.append(Path(file))
                self.src_file_list.addItem(file)
            self._files_count = len(self._files)
