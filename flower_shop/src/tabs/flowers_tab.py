from PyQt6.QtWidgets import (
    QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit, QHeaderView, QMessageBox, QDialog
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from dialogs import AddFlowerDialog
import logging


class FlowersTab(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_ui()
        self.load_flowers()

    def init_ui(self):
        layout = QVBoxLayout()

        self.flowers_table = QTableWidget()
        self.flowers_table.setColumnCount(5)
        self.flowers_table.setHorizontalHeaderLabels(
            ["ID", "Название", "Цена", "Количество", "Изображение"])
        self.flowers_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        control_layout = QHBoxLayout()
        self.btn_add = QPushButton("Добавить")
        self.btn_delete = QPushButton("Удалить")
        self.btn_edit = QPushButton("Редактировать")
        self.btn_refresh = QPushButton("Обновить")
        self.search = QLineEdit()
        self.search.setPlaceholderText("Поиск...")

        control_layout.addWidget(self.btn_add)
        control_layout.addWidget(self.btn_delete)
        control_layout.addWidget(self.btn_edit)
        control_layout.addWidget(self.btn_refresh)
        control_layout.addWidget(self.search)

        layout.addLayout(control_layout)
        layout.addWidget(self.flowers_table)

        self.setLayout(layout)

        self.btn_add.clicked.connect(self.add_flower)
        self.search.textChanged.connect(self.handle_search_flower)

    def load_flowers(self):
        try:
            self.db.cursor.execute("SELECT * FROM flowers")
            flowers = self.db.cursor.fetchall()
            self.flowers_table.setRowCount(len(flowers))
            for row_idx, flower in enumerate(flowers):
                for col_idx, data in enumerate(flower):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.flowers_table.setItem(row_idx, col_idx, item)

        except Exception as e:
            logging.error(f"Ошибка загрузки цветов: {str(e)}")
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить данные")

    def handle_search_flower(self):
        try:
            search_text = self.search.text()
            query = "SELECT * FROM flowers WHERE name ILIKE %s"
            self.db.cursor.execute(query, (f"%{search_text}%",))
            flowers = self.db.cursor.fetchall()

            self.flowers_table.setRowCount(len(flowers))
            for row_idx, flower in enumerate(flowers):
                for col_idx, data in enumerate(flower):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.flowers_table.setItem(row_idx, col_idx, item)

        except Exception as e:
            logging.error(f"Ошибка загрузки цветов: {str(e)}")
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить данные")

    def add_flower(self):
        try:
            dialog = AddFlowerDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                name, price, quantity, image_path = dialog.get_data()
                query = """
                    INSERT INTO flowers (name, price, quantity, image_path)
                    VALUES (%s, %s, %s, %s)
                """
                if self.db.execute_query(query, (name, price, quantity, image_path)):
                    self.load_flowers()
                    QMessageBox.information(self, "Успех", "Цветок добавлен!")
                else:
                    QMessageBox.critical(self, "Ошибка!", "Ошибка при добавлнии")

        except Exception as e:
            logging.error(f"Ошибка добавления: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")