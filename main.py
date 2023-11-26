#!/usr/bin/env python

import sys
from __version import APP_VERSION

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("qdall-e " + APP_VERSION)
    widget.show()
    sys.exit(app.exec())
