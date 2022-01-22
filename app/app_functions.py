####################################################################################
# DOCKER OCTOPUS BY: th3r4ven (https://github.com/th3r4ven)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
####################################################################################
import docker
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QFont

from PySide2.QtWidgets import QTableWidgetItem, QPushButton


class Functions:

    def __init__(self):
        self.doc = docker.from_env()

    def status(self):
        data = self.doc.info()
        data['status'] = "Running" if self.doc.ping() else "Offline"
        return data

    def mount_main_table(self, ui):

        conteiner_list = self.doc.containers.list(all=True)

        ui.conteiner_table.setRowCount(len(conteiner_list))

        row = 0

        for conteiner in conteiner_list:
            name = conteiner.name
            conteiner_id = conteiner.short_id
            if conteiner.ports != {}:
                conteiner_port = f"{conteiner.ports[list(conteiner.ports.keys())[0]][0]['HostPort']}:{list(conteiner.ports.keys())[0]}"
            else:
                conteiner_port = "--:--/--"
            status = conteiner.status

            ui.conteiner_table.setItem(row, 0, QTableWidgetItem(conteiner_id))
            ui.conteiner_table.setItem(row, 1, QTableWidgetItem(name))
            ui.conteiner_table.setItem(row, 2, QTableWidgetItem(conteiner_port))
            ui.conteiner_table.setItem(row, 3, QTableWidgetItem(status))

            font9 = QFont()
            font9.setFamily(u"Segoe UI")
            font9.setPointSize(9)

            btn = QPushButton()
            btn.setToolTip("Details")
            btn.setObjectName(f"details_{conteiner_id}")

            icon3 = QIcon()
            icon3.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
            btn.setIcon(icon3)
            ui.conteiner_table.setCellWidget(row, 4, btn)

            btn.clicked.connect(lambda: self.actions(ui))

            row += 1

        return ui.conteiner_table

    def mount_env_table(self, ui, container):
        env = container.attrs.get('Config').get('Env')

        ui.inspect.setRowCount(len(env))

        row = 0

        for item in env:
            ui.inspect.setItem(row, 0, QTableWidgetItem(item.split('=')[0]))
            ui.inspect.setItem(row, 1, QTableWidgetItem(item.split('=')[1]))
            row += 1

    def actions(self, ui):
        row = ui.conteiner_table.currentRow()
        container_id = ui.conteiner_table.item(row, 0).text()

        container = self.doc.containers.get(container_id)
        ui.container_id = container_id

        self.mount_env_table(ui, container)

        for w in ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == "btn_home":
                w.setStyleSheet(w.styleSheet().replace("QPushButton { border-right: 7px solid #2496ED; }", ""))

        # changing values on page_details

        ui.title.setText(f"Container {container.name}")

        if container.status == "exited":
            ui.open.setDisabled(True)
            ui.cli.setDisabled(True)

            icon3 = QIcon()
            icon3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
            ui.start_stop.setIcon(icon3)

            ui.restart.setDisabled(True)

        else:
            ui.open.setDisabled(False)
            ui.cli.setDisabled(False)

            icon3 = QIcon()
            icon3.addFile(u":/16x16/icons/16x16/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
            ui.start_stop.setIcon(icon3)

            ui.restart.setDisabled(False)

        ui.plainTextEdit_2.setPlainText(container.logs().decode())

        ui.stackedWidget.setCurrentWidget(ui.page_details)


