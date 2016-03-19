#!/bin/env python3
#
# Icarus CMS
#
# (c) 2016 Daniel Jankowski


import sys

from PyQt4 import QtCore, QtGui, uic

from test_ui import Ui_MainWindow

class MainFrame(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MainFrame()
    myapp.show()
    sys.exit(app.exec_())
    pass


if __name__ == '__main__':
    main()
