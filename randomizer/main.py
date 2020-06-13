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
        self.active = False

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
        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet(
            'background-color: rgba(0, 0, 0, 75%); border-radius: 10%;'
        )
        self.icon = QtGui.QIcon.fromTheme('shuffle')
        self.label.setPixmap(
            self.icon.pixmap(50, 50, mode=QtGui.QIcon.Disabled)
        )
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.active = not self.active
            mode = QtGui.QIcon.Active if self.active else QtGui.QIcon.Disabled
            self.label.setPixmap(self.icon.pixmap(50, 50, mode=mode))

        elif event.button() == QtCore.Qt.MiddleButton:
            QtWidgets.qApp.quit()

        elif event.button() == QtCore.Qt.RightButton:
            dialog = WeightsDialog()
            dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    indicator = IndicatorWindow()
    indicator.show()
    sys.exit(app.exec_())
