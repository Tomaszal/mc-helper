import sys
import random
import time

# pylint: disable-msg=no-name-in-module
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from ui.dialog import Ui_Dialog
from pynput.mouse import Button, Listener as MouseListener
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController
from fbs_runtime.application_context.PyQt5 import ApplicationContext


class WeightsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBox_s1.setValue(slotRandomizer.slotWeights[0])
        self.ui.spinBox_s2.setValue(slotRandomizer.slotWeights[1])
        self.ui.spinBox_s3.setValue(slotRandomizer.slotWeights[2])
        self.ui.spinBox_s4.setValue(slotRandomizer.slotWeights[3])
        self.ui.spinBox_s5.setValue(slotRandomizer.slotWeights[4])
        self.ui.spinBox_s6.setValue(slotRandomizer.slotWeights[5])
        self.ui.spinBox_s7.setValue(slotRandomizer.slotWeights[6])
        self.ui.spinBox_s8.setValue(slotRandomizer.slotWeights[7])
        self.ui.spinBox_s9.setValue(slotRandomizer.slotWeights[8])
        self.show()

    def accept(self):
        slotRandomizer.slotWeights = [
            self.ui.spinBox_s1.value(),
            self.ui.spinBox_s2.value(),
            self.ui.spinBox_s3.value(),
            self.ui.spinBox_s4.value(),
            self.ui.spinBox_s5.value(),
            self.ui.spinBox_s6.value(),
            self.ui.spinBox_s7.value(),
            self.ui.spinBox_s8.value(),
            self.ui.spinBox_s9.value(),
        ]
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
        self.slotWeights = [0] * 9

    def onClick(self, x, y, button, pressed):
        if button != Button.right or not pressed:
            return True

        time.sleep(0.05)
        slot = random.choices(
            population=range(1, 10), weights=self.slotWeights
        )[0]
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
    appCtx = ApplicationContext()
    slotRandomizer = SlotRandomizer()
    indicator = IndicatorWindow()
    indicator.show()
    exitCode = appCtx.app.exec_()
    sys.exit(exitCode)
