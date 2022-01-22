####################################################################################
# DOCKER OCTOPUS BY: th3r4ven (https://github.com/th3r4ven)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
####################################################################################
import webbrowser


from main import *
import docker
import webbrowser
from app_functions import Functions

GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

count = 1


class UIFunctions(MainWindow):
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    def returnStatus(self):
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    def hideMenu(self):
        if not self.ui.frame_left_menu.isHidden():
            self.ui.frame_left_menu.hide()
            self.ui.frame_toggle.hide()
        else:
            self.ui.frame_left_menu.show()
            self.ui.frame_toggle.show()

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count), self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid #2496ED; }")
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid #2496ED; }", "")
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            self.ui.label_user_icon.setText(initialsTooltip)

            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        self.ui.btn_close.clicked.connect(lambda: self.close())

    def login_buttons(self, btn_name):
        if btn_name == "login_guest":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "GUEST")
            UIFunctions.hideMenu(self)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "TH3R4VEN")
            UIFunctions.hideMenu(self)

    def refresh_home_table(self):
        self.ui.conteiner_table.clearContents()
        Functions().mount_main_table(self.ui)

    def container_open(self):
        print(f"open {self.ui.container_id}")
        doc = docker.from_env()
        container = doc.containers.get(self.ui.container_id)
        if container.ports != {}:
            host = container.ports[list(container.ports.keys())[0]][0]['HostIp'] if container.ports[list(container.ports.keys())[0]][0]['HostIp'] != '0.0.0.0' else 'localhost'
            port = container.ports[list(container.ports.keys())[0]][0]['HostPort']
            webbrowser.open(f"http://{host}:{port}")
        else:
            return

    def container_cli(self):
        print(f"cli {self.ui.container_id}")

    def container_start_stop(self):
        print(f"start {self.ui.container_id}")
        doc = docker.from_env()
        container = doc.containers.get(self.ui.container_id)
        container.start() if container.status == 'exited' else container.stop()

    def container_restart(self):
        print(f"restart {self.ui.container_id}")
        doc = docker.from_env()
        container = doc.containers.get(self.ui.container_id)
        container.restart()

    def container_delete(self):
        print(f"delete {self.ui.container_id}")
        doc = docker.from_env()
        container = doc.containers.get(self.ui.container_id)
        container.stop()
        container.remove()
