from PyQt6.QtWidgets import (
    QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit, QHeaderView, QMessageBox, QDialog
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from flower_shop.src.dialogs import AddClientDialog
import logging

logging.basicConfig(
    filename='app_errors_client.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ClientsTab(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_ui()
        self.load_clients()

    def init_ui(self):
        layout = QVBoxLayout()

        self.clients_table = QTableWidget()
        self.clients_table.setColumnCount(4)
        self.clients_table.setHorizontalHeaderLabels(
            ["ID", "Имя", "Телефон", "email"])
        self.clients_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        control_layout = QHBoxLayout()
        self.btn_add_client = QPushButton("Добавить")
        self.btn_delete_client = QPushButton("Удалить")
        # self.btn_edit = QPushButton("Редактировать")
        # self.btn_refresh = QPushButton("Обновить")
        self.search_clients = QLineEdit()
        self.search_clients.setPlaceholderText("Поиск...")

        control_layout.addWidget(self.btn_add_client)
        control_layout.addWidget(self.btn_delete_client)
        # control_layout.addWidget(self.btn_edit)
        # control_layout.addWidget(self.btn_refresh)
        control_layout.addWidget(self.search_clients)

        layout.addLayout(control_layout)
        layout.addWidget(self.clients_table)

        self.setLayout(layout)

        self.btn_add_client.clicked.connect(self.add_client)
        self.search_clients.textChanged.connect(self.handle_search_client)
        self.btn_delete_client.clicked.connect(self.delete_client)
        # self.btn_refresh.clicked.connect(self.load_clients)
        # self.btn_edit.clicked.connect(self.edit_client)

    def load_clients(self):
        try:
            self.db.cursor.execute("SELECT * FROM clients")
            clients = self.db.cursor.fetchall()
            self.clients_table.setRowCount(len(clients))
            for row_idx, client in enumerate(clients):
                for col_idx, data in enumerate(client):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.clients_table.setItem(row_idx, col_idx, item)

        except Exception as e:
            logging.error(f"Ошибка загрузки клиентов: {str(e)}")
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить данные")

    def handle_search_client(self):
        try:
            search_text = self.search_clients.text()
            query = ("""SELECT * FROM clients
                    WHERE full_name ILIKE %s
                    OR phone ILIKE %s
                    OR email ILIKE %s""")
            self.db.cursor.execute(query, (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%"))
            clients = self.db.cursor.fetchall()

            self.clients_table.setRowCount(len(clients))
            for row_idx, client in enumerate(clients):
                for col_idx, data in enumerate(client):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.clients_table.setItem(row_idx, col_idx, item)

        except Exception as e:
            logging.error(f"Ошибка загрузки клиентов: {str(e)}")
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить данные")

    def add_client(self):
        try:
            dialog = AddClientDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                surname, name, middle_name, phone, email = dialog.get_data()
                full_name = f"{surname} {name} {middle_name}"
                if not name.strip() or not phone.strip():
                    raise ValueError("Заполните поля Имя и Телефон")
                query = """
                    INSERT INTO clients (full_name, phone, email)
                    VALUES (%s, %s, %s)
                """
                if self.db.execute_query(query, (full_name, phone, email)):
                    self.load_clients()
                    QMessageBox.information(self, "Успех", "Клиент добавлен!")
                else:
                    QMessageBox.critical(self, "Ошибка!", "Ошибка при добавлении клиента в базу")

        except Exception as e:
            logging.error(f"Ошибка добавления: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")


    def delete_client(self):
        try:
            selected_row = self.clients_table.currentRow()
            if selected_row == -1:          # -1 это None
                QMessageBox.warning(self, "Ошибка", f"Выберите клиента!")
            client_id = self.flowers_table.item(selected_row, 0).text()
            query = "DELETE FROM flowers WHERE flower_id = %s"
            if self.db.execute_query(query,(client_id,)):
                self.load_clients()
                QMessageBox.information(self, "Успех", "Клиент удален!")
            else:
                QMessageBox.critical(self, "Ошибка", "Ошибка при удалении!")

        except Exception as e:
            logging.error(f"Ошибка удаления: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")