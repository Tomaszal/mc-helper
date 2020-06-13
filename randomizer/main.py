import sys

# pylint: disable-msg=no-name-in-module
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from dialog import Ui_Dialog


class WeightsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class IndicatorWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupWindow()
        self.setupWidgets()

    def setupWindow(self):
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter,
                QtCore.QSize(50, 50),
                QtWidgets.qApp.desktop().availableGeometry()
            ).adjusted(-20, 0, -20, 0)
        )

    def setupWidgets(self):
        label = QtWidgets.QLabel()
        label.setStyleSheet(
            'background-color: rgba(0, 0, 0, 75%); border-radius: 10%;'
        )
        icon = QtGui.QIcon.fromTheme('shuffle')
        label.setPixmap(icon.pixmap(50, 50, mode=QtGui.QIcon.Active))
        self.setCentralWidget(label)

    def mousePressEvent(self, event):
        QtWidgets.qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = IndicatorWindow()
    w.show()
    sys.exit(app.exec_())
