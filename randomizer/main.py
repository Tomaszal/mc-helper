import sys
import random
import time

# pylint: disable-msg=no-name-in-module
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from dialog import Ui_Dialog
from pynput.mouse import Button, Listener as MouseListener
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController


class WeightsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def accept(self):
        print(self.ui.spinBox_s1.value())
        self.close()


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

            if (self.active):
                slotRandomizer.startListener()
            else:
                slotRandomizer.stopListener()

        elif event.button() == QtCore.Qt.MiddleButton:
            QtWidgets.qApp.quit()

        elif event.button() == QtCore.Qt.RightButton:
            dialog = WeightsDialog()
            dialog.exec_()


class SlotRandomizer():
    def __init__(self):
        self.keyboard = KeyboardController()
        self.listener = MouseListener(on_click=self.onClick)
        self.slot_weights = [0] * 9

    def onClick(self, x, y, button, pressed):
        if button != Button.right or not pressed:
            return True

        time.sleep(0.05)
        slot = random.choices(
            population=range(1, 10), weights=self.slot_weights
        )[0]
        print(slot)
        key = KeyCode.from_vk(0x30 + slot)
        self.keyboard.press(key)
        time.sleep(0.05)
        self.keyboard.release(key)

    def startListener(self):
        self.listener = MouseListener(on_click=self.onClick)
        self.listener.start()

    def stopListener(self):
        self.listener.stop()
        self.listener = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    slotRandomizer = SlotRandomizer()
    indicator = IndicatorWindow()
    indicator.show()
    sys.exit(app.exec_())
