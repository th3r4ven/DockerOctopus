# -*- coding: utf-8 -*-
####################################################################################
# DOCKER OCTOPUS BY: th3r4ven (https://github.com/th3r4ven)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
####################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

import files_rc
from app_functions import Functions


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
        # endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "	color: #ffffff;\n"
                                 "	background-color: rgba(27, 29, 35, 160);\n"
                                 "	border: 1px solid rgb(40, 40, 40);\n"
                                 "	border-radius: 2px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
                                         "color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
                                      "QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* SCROLL BARS */\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 14px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "    background: rgb(85, 170, 255);\n"
                                      "    min-width: 25px;\n"
                                      "	border-radius: 7px\n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-right-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "    subcontrol-position: right;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      ""
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    subcontrol-position: left;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 14px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      " QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(85, 170, 255);\n"
                                      "    min-height: 25px;\n"
                                      "	border-radius: 7px\n"
                                      " }\n"
                                      " QScrollBar::add-line:vertical {\n"
                                      "     border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "     subcontrol-position: bottom;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(55, 63"
                                      ", 77);\n"
                                      "     height: 20px;\n"
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "     subcontrol-position: top;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      "/* CHECKBOX */\n"
                                      "QCheckBox::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "    background: 3px solid rgb(52, 59, 72);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* RADIO BUTTON */\n"
                                      "QRadioButton::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius"
                                      ": 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QRadioButton::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "    background: 3px solid rgb(94, 106, 130);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "}\n"
                                      "\n"
                                      "/* COMBOBOX */\n"
                                      "QComboBox{\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb("
                                      "85, 170, 255);	\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}\n"
                                      "\n"
                                      "/* SLIDERS */\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border-radius: 9px;\n"
                                      "    height: 18px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:horizontal:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "    border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "    border-radius: 9px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:vertical:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:verti"
                                      "cal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "	border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
                                           "	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-reperat;\n"
                                           "	border: none;\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "	background-color: rgb(33, 37, 43);\n"
                                           "}\n"
                                           "QPushButton:pressed {	\n"
                                           "	background-color: rgb(85, 170, 255);\n"
                                           "}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
                                              "background-image: url(images/icon.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
                                               "")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
                                        "	border: none;\n"
                                        "	background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
                                                "	border: none;\n"
                                                "	background-color: transparent;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "	background-color: rgb(52, 59, 72);\n"
                                                "}\n"
                                                "QPushButton:pressed {	\n"
                                                "	background-color: rgb(85, 170, 255);\n"
                                                "}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
                                     "	border: none;\n"
                                     "	background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(52, 59, 72);\n"
                                     "}\n"
                                     "QPushButton:pressed {	\n"
                                     "	background-color: rgb(85, 170, 255);\n"
                                     "}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: #2496ED")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: white ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: white")
        self.label_top_info_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)

        self.verticalLayout_2.addWidget(self.frame_top_info)

        self.horizontalLayout_3.addWidget(self.frame_top_right)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
                                           "	border-radius: 30px;\n"
                                           "	background-color: rgb(44, 49, 60);\n"
                                           "	border: 5px solid rgb(39, 44, 54);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-repeat;\n"
                                           "}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_8 = QFrame(self.page_home)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 150))
        self.frame_8.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                   "border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_8)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 881, 142))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.total_conteiners = QLabel(self.gridLayoutWidget)
        self.total_conteiners.setObjectName(u"total_conteiners")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.total_conteiners.setFont(font5)
        self.total_conteiners.setStyleSheet(u"padding: 10%;")

        self.gridLayout_3.addWidget(self.total_conteiners, 2, 0, 1, 1)

        self.label_null = QLabel(self.gridLayoutWidget)
        self.label_null.setObjectName(u"label_null")

        self.gridLayout_3.addWidget(self.label_null, 2, 1, 1, 1)

        self.engine_status = QLabel(self.gridLayoutWidget)
        self.engine_status.setObjectName(u"engine_status")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setWeight(50)
        font6.setKerning(True)
        self.engine_status.setFont(font6)

        self.gridLayout_3.addWidget(self.engine_status, 2, 2, 1, 1, Qt.AlignHCenter)

        self.logo_text = QLabel(self.gridLayoutWidget)
        self.logo_text.setObjectName(u"logo_text")
        self.logo_text.setPixmap(QPixmap("images/textOctopus.png"))

        self.gridLayout_3.addWidget(self.logo_text, 1, 0, 1, 2)

        self.refresh_btn = QPushButton(self.gridLayoutWidget)
        self.refresh_btn.setObjectName(u"refresh_btn")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(14)
        self.refresh_btn.setFont(font7)
        self.refresh_btn.setStyleSheet(u"QPushButton {\n"
                                       "	border: 2px solid rgb(52, 59, 72);\n"
                                       "	border-radius: 5px;	\n"
                                       "	padding: 5%;\n"
                                       "	background-color: rgb(52, 59, 72);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "	background-color: rgb(57, 65, 80);\n"
                                       "	border: 2px solid rgb(61, 70, 86);\n"
                                       "}\n"
                                       "QPushButton:pressed {	\n"
                                       "	background-color: rgb(35, 40, 49);\n"
                                       "	border: 2px solid rgb(43, 50, 61);\n"
                                       "}")

        self.gridLayout_3.addWidget(self.refresh_btn, 1, 2, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.page_home)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.conteiner_table = QTableWidget(self.frame_7)
        if (self.conteiner_table.columnCount() < 5):
            self.conteiner_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.conteiner_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.conteiner_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.conteiner_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.conteiner_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.conteiner_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.conteiner_table.setObjectName(u"conteiner_table")
        self.conteiner_table.setGeometry(QRect(0, 0, 891, 426))
        font8 = QFont()
        font8.setPointSize(10)
        self.conteiner_table.setFont(font8)
        self.conteiner_table.setLayoutDirection(Qt.LeftToRight)
        self.conteiner_table.setAutoFillBackground(False)
        self.conteiner_table.setStyleSheet(u"QTableWidget {	\n"
                                           "	background-color: rgb(39, 44, 54);\n"
                                           "	padding: 10px;\n"
                                           "	border-radius: 5px;\n"
                                           "	gridline-color: rgb(44, 49, 60);\n"
                                           "	border-bottom: 1px solid rgb(44, 49, 60);\n"
                                           "}\n"
                                           "QTableWidget::item{\n"
                                           "	border-color: rgb(44, 49, 60);\n"
                                           "	padding-left: 5px;\n"
                                           "	padding-right: 5px;\n"
                                           "	gridline-color: rgb(44, 49, 60);\n"
                                           "}\n"
                                           "QTableWidget::item:selected{\n"
                                           "	background-color: transparent;\n"
                                           "}\n"
                                           "QScrollBar:horizontal {\n"
                                           "    border: none;\n"
                                           "    background: rgb(52, 59, 72);\n"
                                           "    height: 14px;\n"
                                           "    margin: 0px 21px 0 21px;\n"
                                           "	border-radius: 0px;\n"
                                           "}\n"
                                           " QScrollBar:vertical {\n"
                                           "	border: none;\n"
                                           "    background: rgb(52, 59, 72);\n"
                                           "    width: 14px;\n"
                                           "    margin: 21px 0 21px 0;\n"
                                           "	border-radius: 0px;\n"
                                           " }\n"
                                           "QHeaderView::section{\n"
                                           "	Background-color: rgb(39, 44, 54);\n"
                                           "	max-width: 30px;\n"
                                           "	border: 1px solid rgb(44, 49, 60);\n"
                                           "	border-style: none;\n"
                                           "    border-bottom: 1px solid rgb(44, 49, 60);\n"
                                           "    border-right: 1px solid rgb(44, 49, 60);\n"
                                           "}\n"
                                           ""
                                           "QTableWidget::horizontalHeader {	\n"
                                           "	background-color: rgb(81, 255, 0);\n"
                                           "}\n"
                                           "QHeaderView::section:horizontal\n"
                                           "{\n"
                                           "    border: 1px solid rgb(32, 34, 42);\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "	padding: 3px;\n"
                                           "	border-top-left-radius: 7px;\n"
                                           "    border-top-right-radius: 7px;\n"
                                           "}\n"
                                           "QHeaderView::section:vertical\n"
                                           "{\n"
                                           "    border: 1px solid rgb(44, 49, 60);\n"
                                           "}\n"
                                           "")
        self.conteiner_table.setAutoScrollMargin(15)
        self.conteiner_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.conteiner_table.setDragDropOverwriteMode(False)
        self.conteiner_table.setShowGrid(True)
        self.conteiner_table.setGridStyle(Qt.SolidLine)
        self.conteiner_table.setSortingEnabled(True)
        self.conteiner_table.setRowCount(3)
        self.conteiner_table.horizontalHeader().setVisible(True)
        self.conteiner_table.horizontalHeader().setDefaultSectionSize(170)
        self.conteiner_table.verticalHeader().setVisible(False)
        self.conteiner_table.verticalHeader().setDefaultSectionSize(30)
        self.conteiner_table.verticalHeader().setHighlightSections(True)

        self.conteiner_table = Functions().mount_main_table(self)

        self.verticalLayout_10.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)

        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                    "}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        self.pushButton.setFont(font9)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	border-radius: 5px;	\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(57, 65, 80);\n"
                                      "	border: 2px solid rgb(61, 70, 86);\n"
                                      "}\n"
                                      "QPushButton:pressed {	\n"
                                      "	background-color: rgb(35, 40, 49);\n"
                                      "	border: 2px solid rgb(43, 50, 61);\n"
                                      "}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.verticalLayout_7.addWidget(self.frame_content_wid_1)

        self.verticalLayout_15.addWidget(self.frame_div_content_1)

        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                   "border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
                                             "	border: none;\n"
                                             "    background: rgb(52, 59, 72);\n"
                                             "    width: 14px;\n"
                                             "    margin: 21px 0 21px 0;\n"
                                             "	border-radius: 0px;\n"
                                             " }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
                                      "	border: none;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 14px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 14px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      "")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
                                         "	background-color: rgb(27, 29, 35);\n"
                                         "	border-radius: 5px;\n"
                                         "	padding: 10px;\n"
                                         "}\n"
                                         "QPlainTextEdit:hover {\n"
                                         "	border: 2px solid rgb(64, 71, 88);\n"
                                         "}\n"
                                         "QPlainTextEdit:focus {\n"
                                         "	border: 2px solid rgb(91, 101, 124);\n"
                                         "}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font9)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding: 5px;\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QComboBox:hover{\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "	color: rgb(85, 170, 255);	\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	padding: 10px;\n"
                                    "	selection-background-color: rgb(39, 44, 54);\n"
                                    "}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
                                               "    border: none;\n"
                                               "    background: rgb(52, 59, 72);\n"
                                               "    height: 14px;\n"
                                               "    margin: 0px 21px 0 21px;\n"
                                               "	border-radius: 0px;\n"
                                               "}\n"
                                               "")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
                                             "	color: rgb(85, 170, 255);\n"
                                             "	border-radius: 5px;\n"
                                             "	padding: 5px;\n"
                                             "}\n"
                                             "QCommandLinkButton:hover {	\n"
                                             "	color: rgb(210, 210, 210);\n"
                                             "	background-color: rgb(44, 49, 60);\n"
                                             "}\n"
                                             "QCommandLinkButton:pressed {	\n"
                                             "	color: rgb(210, 210, 210);\n"
                                             "	background-color: rgb(52, 58, 71);\n"
                                             "}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.verticalLayout_11.addLayout(self.gridLayout_2)

        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.frame_4 = QFrame(self.page_welcome)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(290, 0, 361, 110))
        self.frame_4.setMaximumSize(QSize(16777215, 110))
        self.frame_4.setStyleSheet(u"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.welcome_text = QLabel(self.frame_4)
        self.welcome_text.setObjectName(u"welcome_text")
        font10 = QFont()
        font10.setPointSize(46)
        font10.setBold(True)
        font10.setWeight(75)
        self.welcome_text.setFont(font10)

        self.verticalLayout_16.addWidget(self.welcome_text)

        self.frame_5 = QFrame(self.page_welcome)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(120, 80, 861, 221))
        self.frame_5.setMaximumSize(QSize(16777215, 350))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.all_logo = QLabel(self.frame_5)
        self.all_logo.setObjectName(u"all_logo")
        self.all_logo.setGeometry(QRect(10, 30, 861, 191))
        self.all_logo.setMaximumSize(QSize(16777215, 350))
        self.all_logo.setPixmap(QPixmap("images/all.png"))
        self.frame_6 = QFrame(self.page_welcome)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(70, 340, 861, 101))
        self.frame_6.setMaximumSize(QSize(16777215, 110))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.login_docker = QPushButton(self.frame_6)
        self.login_docker.setObjectName(u"login_docker")
        self.login_docker.setGeometry(QRect(0, 20, 411, 59))
        font11 = QFont()
        font11.setPointSize(28)
        self.login_docker.setFont(font11)
        self.login_docker.setStyleSheet(u"QPushButton {\n"
                                        "	border: 2px solid rgb(52, 59, 72);\n"
                                        "	padding: 5%;\n"
                                        "	border-radius: 5px;	\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(57, 65, 80);\n"
                                        "	border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(35, 40, 49);\n"
                                        "	border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.login_guest = QPushButton(self.frame_6)
        self.login_guest.setObjectName(u"login_guest")
        self.login_guest.setGeometry(QRect(420, 20, 411, 59))
        self.login_guest.setFont(font11)
        self.login_guest.setStyleSheet(u"QPushButton {\n"
                                       "	border: 2px solid rgb(52, 59, 72);\n"
                                       "	padding: 5%;\n"
                                       "	border-radius: 5px;	\n"
                                       "	background-color: rgb(52, 59, 72);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "	background-color: rgb(57, 65, 80);\n"
                                       "	border: 2px solid rgb(61, 70, 86);\n"
                                       "}\n"
                                       "QPushButton:pressed {	\n"
                                       "	background-color: rgb(35, 40, 49);\n"
                                       "	border: 2px solid rgb(43, 50, 61);\n"
                                       "}")
        self.login_guest.setAutoDefault(False)
        self.login_guest.setFlat(False)
        self.stackedWidget.addWidget(self.page_welcome)
        self.page_details = QWidget()
        self.page_details.setObjectName(u"page_details")
        self.frame_10 = QFrame(self.page_details)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 0, 891, 50))
        self.frame_10.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                    "border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.title = QLabel(self.frame_10)
        self.title.setText("Container name")
        self.title.setFont(font1)
        self.title.setObjectName(u"title")

        self.gridLayout_4.addWidget(self.title, 0, 0, 1, 1)

        self.line = QLabel(self.frame_10)

        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)

        self.open = QPushButton(self.frame_10)
        self.open.setObjectName(u"open")
        self.open.setFont(font9)
        self.open.setStyleSheet(u"QPushButton {\n"
                                "	border: 2px solid rgb(52, 59, 72);\n"
                                "	border-radius: 5px;	\n"
                                "	padding: 5%;\n"
                                "	background-color: rgb(52, 59, 72);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(57, 65, 80);\n"
                                "	border: 2px solid rgb(61, 70, 86);\n"
                                "}\n"
                                "QPushButton:pressed {	\n"
                                "	background-color: rgb(35, 40, 49);\n"
                                "	border: 2px solid rgb(43, 50, 61);\n"
                                "}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-external-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon3)

        self.gridLayout_4.addWidget(self.open, 2, 0, 1, 1)

        self.cli = QPushButton(self.frame_10)
        self.cli.setObjectName(u"cli")
        self.cli.setStyleSheet(u"QPushButton {\n"
                               "	border: 2px solid rgb(52, 59, 72);\n"
                               "	border-radius: 5px;	\n"
                               "	padding: 5%;\n"
                               "	background-color: rgb(52, 59, 72);\n"
                               "}\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(57, 65, 80);\n"
                               "	border: 2px solid rgb(61, 70, 86);\n"
                               "}\n"
                               "QPushButton:pressed {	\n"
                               "	background-color: rgb(35, 40, 49);\n"
                               "	border: 2px solid rgb(43, 50, 61);\n"
                               "}")

        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cli.setIcon(icon3)

        self.gridLayout_4.addWidget(self.cli, 2, 1, 1, 1)

        self.start_stop = QPushButton(self.frame_10)
        self.start_stop.setObjectName(u"start_stop")
        self.start_stop.setStyleSheet(u"QPushButton {\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	border-radius: 5px;	\n"
                                      "	padding: 5%;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(57, 65, 80);\n"
                                      "	border: 2px solid rgb(61, 70, 86);\n"
                                      "}\n"
                                      "QPushButton:pressed {	\n"
                                      "	background-color: rgb(35, 40, 49);\n"
                                      "	border: 2px solid rgb(43, 50, 61);\n"
                                      "}")

        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_stop.setIcon(icon3)

        self.gridLayout_4.addWidget(self.start_stop, 2, 2, 1, 1)

        self.restart = QPushButton(self.frame_10)
        self.restart.setObjectName(u"restart")
        self.restart.setStyleSheet(u"QPushButton {\n"
                                   "	border: 2px solid rgb(52, 59, 72);\n"
                                   "	border-radius: 5px;	\n"
                                   "	padding: 5%;\n"
                                   "	background-color: rgb(52, 59, 72);\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "	background-color: rgb(57, 65, 80);\n"
                                   "	border: 2px solid rgb(61, 70, 86);\n"
                                   "}\n"
                                   "QPushButton:pressed {	\n"
                                   "	background-color: rgb(35, 40, 49);\n"
                                   "	border: 2px solid rgb(43, 50, 61);\n"
                                   "}")

        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restart.setIcon(icon3)

        self.gridLayout_4.addWidget(self.restart, 2, 3, 1, 1)

        self.delete_2 = QPushButton(self.frame_10)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setStyleSheet(u"QPushButton {\n"
                                    "	border: 2px solid rgb(52, 59, 72);\n"
                                    "	border-radius: 5px;	\n"
                                    "	padding: 5%;\n"
                                    "	background-color: rgb(52, 59, 72);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(57, 65, 80);\n"
                                    "	border: 2px solid rgb(61, 70, 86);\n"
                                    "}\n"
                                    "QPushButton:pressed {	\n"
                                    "	background-color: rgb(35, 40, 49);\n"
                                    "	border: 2px solid rgb(43, 50, 61);\n"
                                    "}")

        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_2.setIcon(icon3)

        self.gridLayout_4.addWidget(self.delete_2, 2, 4, 1, 1)

        self.verticalLayout_17.addLayout(self.gridLayout_4)

        self.frame_11 = QFrame(self.page_details)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 60, 891, 291))
        self.frame_11.setMinimumSize(QSize(0, 150))
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                    "border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.logs_label = QLabel(self.frame_11)
        self.logs_label.setObjectName(u"logs_label")
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(11)
        self.logs_label.setFont(font12)

        self.gridLayout_5.addWidget(self.logs_label, 0, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.frame_11)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea {\n"
                                        "	border: none;\n"
                                        "	border-radius: 0px;\n"
                                        "}\n"
                                        "QScrollBar:horizontal {\n"
                                        "    border: none;\n"
                                        "    background: rgb(52, 59, 72);\n"
                                        "    height: 14px;\n"
                                        "    margin: 0px 21px 0 21px;\n"
                                        "	border-radius: 0px;\n"
                                        "}\n"
                                        " QScrollBar:vertical {\n"
                                        "	border: none;\n"
                                        "    background: rgb(52, 59, 72);\n"
                                        "    width: 14px;\n"
                                        "    margin: 21px 0 21px 0;\n"
                                        "	border-radius: 0px;\n"
                                        " }\n"
                                        "")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 857, 218))
        self.horizontalLayout_15 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(200, 200))
        self.plainTextEdit_2.setStyleSheet(u"QPlainTextEdit {\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "	border-radius: 5px;\n"
                                           "	padding: 10px;\n"
                                           "}\n"
                                           "QPlainTextEdit:hover {\n"
                                           "	border: 2px solid rgb(64, 71, 88);\n"
                                           "}\n"
                                           "QPlainTextEdit:focus {\n"
                                           "	border: 2px solid rgb(91, 101, 124);\n"
                                           "}")
        self.plainTextEdit_2.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.plainTextEdit_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_5.addWidget(self.scrollArea_2, 1, 0, 3, 1)

        self.verticalLayout_14.addLayout(self.gridLayout_5)

        self.inspect = QTableWidget(self.page_details)
        if (self.inspect.columnCount() < 2):
            self.inspect.setColumnCount(2)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.inspect.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.inspect.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        if (self.inspect.rowCount() < 3):
            self.inspect.setRowCount(3)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.inspect.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.inspect.setItem(0, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.inspect.setItem(1, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.inspect.setItem(1, 1, __qtablewidgetitem20)
        self.inspect.setObjectName(u"inspect")
        self.inspect.setGeometry(QRect(0, 360, 891, 231))
        self.inspect.setFont(font8)
        self.inspect.setLayoutDirection(Qt.LeftToRight)
        self.inspect.setAutoFillBackground(False)
        self.inspect.setStyleSheet(u"QTableWidget {	\n"
                                   "	background-color: rgb(39, 44, 54);\n"
                                   "	padding: 10px;\n"
                                   "	border-radius: 5px;\n"
                                   "	gridline-color: rgb(44, 49, 60);\n"
                                   "	border-bottom: 1px solid rgb(44, 49, 60);\n"
                                   "}\n"
                                   "QTableWidget::item{\n"
                                   "	border-color: rgb(44, 49, 60);\n"
                                   "	padding-left: 5px;\n"
                                   "	padding-right: 5px;\n"
                                   "	gridline-color: rgb(44, 49, 60);\n"
                                   "}\n"
                                   "QTableWidget::item:selected{\n"
                                   "	background-color: transparent;\n"
                                   "}\n"
                                   "QScrollBar:horizontal {\n"
                                   "    border: none;\n"
                                   "    background: rgb(52, 59, 72);\n"
                                   "    height: 14px;\n"
                                   "    margin: 0px 21px 0 21px;\n"
                                   "	border-radius: 0px;\n"
                                   "}\n"
                                   " QScrollBar:vertical {\n"
                                   "	border: none;\n"
                                   "    background: rgb(52, 59, 72);\n"
                                   "    width: 14px;\n"
                                   "    margin: 21px 0 21px 0;\n"
                                   "	border-radius: 0px;\n"
                                   " }\n"
                                   "QHeaderView::section{\n"
                                   "	Background-color: rgb(39, 44, 54);\n"
                                   "	max-width: 30px;\n"
                                   "	border: 1px solid rgb(44, 49, 60);\n"
                                   "	border-style: none;\n"
                                   "    border-bottom: 1px solid rgb(44, 49, 60);\n"
                                   "    border-right: 1px solid rgb(44, 49, 60);\n"
                                   "}\n"
                                   "QTa"
                                   "bleWidget::horizontalHeader {	\n"
                                   "	background-color: rgb(81, 255, 0);\n"
                                   "}\n"
                                   "QHeaderView::section:horizontal\n"
                                   "{\n"
                                   "    border: 1px solid rgb(32, 34, 42);\n"
                                   "	background-color: rgb(27, 29, 35);\n"
                                   "	padding: 3px;\n"
                                   "	border-top-left-radius: 7px;\n"
                                   "    border-top-right-radius: 7px;\n"
                                   "}\n"
                                   "QHeaderView::section:vertical\n"
                                   "{\n"
                                   "    border: 1px solid rgb(44, 49, 60);\n"
                                   "}\n"
                                   "")
        self.inspect.setAutoScrollMargin(15)
        self.inspect.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inspect.setDragDropOverwriteMode(False)
        self.inspect.setShowGrid(True)
        self.inspect.setGridStyle(Qt.SolidLine)
        self.inspect.setSortingEnabled(True)
        self.inspect.setRowCount(3)
        self.inspect.setColumnCount(2)
        self.inspect.horizontalHeader().setVisible(True)
        self.inspect.horizontalHeader().setDefaultSectionSize(435)
        self.inspect.verticalHeader().setVisible(False)
        self.inspect.verticalHeader().setDefaultSectionSize(30)
        self.inspect.verticalHeader().setHighlightSections(True)
        self.stackedWidget.addWidget(self.page_details)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: white")
        self.frame_label_bottom.setStyleSheet(u"background-color: #2496ED")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: white")
        self.label_version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)

        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
                                           "	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-reperat;\n"
                                           "}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)

        self.verticalLayout_4.addWidget(self.frame_grip)

        self.horizontalLayout_2.addWidget(self.frame_content_right)

        self.verticalLayout.addWidget(self.frame_center)

        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.login_guest.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
        # if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(
            QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| WELCOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.total_conteiners.setText(
            QCoreApplication.translate("MainWindow", f"Total Conteiners: {Functions().status()['Containers']}", None))
        self.label_null.setText("")
        self.engine_status.setText(
            QCoreApplication.translate("MainWindow", f"Docker Engine: {Functions().status()['status']}", None))
        self.logo_text.setText("")
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))

        # HEADERS

        ___qtablewidgetitem = self.conteiner_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Conteiner ID", None))
        ___qtablewidgetitem1 = self.conteiner_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Conteiner Name", None))
        ___qtablewidgetitem2 = self.conteiner_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Exposed Port", None))
        ___qtablewidgetitem3 = self.conteiner_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem4 = self.conteiner_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Action", None))

        # CONTENT

        __sortingEnabled = self.conteiner_table.isSortingEnabled()
        self.conteiner_table.setSortingEnabled(False)
        self.conteiner_table.setSortingEnabled(__sortingEnabled)

        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(
            QCoreApplication.translate("MainWindow",
                                       u"Ex: C:\\Program Files\\Blender Foundation\\Blender 2.82\\blender.exe",
                                       None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        self.welcome_text.setText(QCoreApplication.translate("MainWindow", u"Welcome to", None))
        self.all_logo.setText("")
        self.login_docker.setText(QCoreApplication.translate("MainWindow", u"Login with Docker", None))
        self.login_guest.setText(QCoreApplication.translate("MainWindow", u"Login as Guest", None))
        self.open.setText("")
        self.start_stop.setText("")
        self.cli.setText("")
        self.restart.setText("")
        self.delete_2.setText("")
        self.logs_label.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        ___qtablewidgetitem15 = self.inspect.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Key", None));
        ___qtablewidgetitem16 = self.inspect.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Value", None));

        __sortingEnabled1 = self.inspect.isSortingEnabled()
        self.inspect.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.inspect.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"123456", None));
        ___qtablewidgetitem18 = self.inspect.item(0, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"MFAO", None));
        ___qtablewidgetitem19 = self.inspect.item(1, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"987654", None));
        ___qtablewidgetitem20 = self.inspect.item(1, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"RISK", None));
        self.inspect.setSortingEnabled(__sortingEnabled1)

        self.label_credits.setText(
            QCoreApplication.translate("MainWindow", u"Developed by: TH3R4VEN", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi
