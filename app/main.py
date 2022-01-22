####################################################################################
# DOCKER OCTOPUS BY: th3r4ven (https://github.com/th3r4ven)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
####################################################################################

import sys
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from app_modules import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UIFunctions.removeTitleBar(True)

        self.setWindowTitle('Docker Octopus - Docker Manager')
        UIFunctions.labelTitle(self, 'Docker Octopus - Docker Manager')
        UIFunctions.labelDescription(self, 'Managing all your tritium')

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        # MY BUTTON FUNCTIONS GOES HERE
        self.ui.login_guest.clicked.connect(lambda: UIFunctions.login_buttons(self, self.ui.login_guest.objectName()))
        self.ui.login_docker.clicked.connect(lambda: UIFunctions.login_buttons(self, self.ui.login_docker.objectName()))
        self.ui.refresh_btn.clicked.connect(lambda: UIFunctions.refresh_home_table(self))

        self.ui.open.clicked.connect(lambda: UIFunctions.container_open(self))
        self.ui.cli.clicked.connect(lambda: UIFunctions.container_cli(self))
        self.ui.start_stop.clicked.connect(lambda: UIFunctions.container_start_stop(self))
        self.ui.restart.clicked.connect(lambda: UIFunctions.container_restart(self))
        self.ui.delete_2.clicked.connect(lambda: UIFunctions.container_delete(self))

        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Configurations", "btn_configs", "url(:/16x16/icons/16x16/cil-equalizer.png)",
                               False)

        UIFunctions.selectStandardMenu(self, "btn_home")
        UIFunctions.hideMenu(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_welcome)

        UIFunctions.userIcon(self, "?", "", True)

        def moveWindow(event):
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.show()

    def Button(self):
        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_configs":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_configs)
            UIFunctions.resetStyle(self, "btn_configs")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
