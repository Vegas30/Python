from PyQt6.QtWidgets import (
    QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit, QHeaderView, QMessageBox, QDialog
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from flower_shop.src.dialogs import AddFlowerDialog
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
        self.btn_delete.clicked.connect(self.delete_flower)
        self.btn_refresh.clicked.connect(self.load_flowers)
        self.btn_edit.clicked.connect(self.edit_flower)

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


    def delete_flower(self):
        try:
            selected_row = self.flowers_table.currentRow()
            if selected_row == -1:          # -1 это None
                QMessageBox.warning(self, "Ошибка", f"Выберите цветок!")
            flower_id = self.flowers_table.item(selected_row, 0).text()
            query = "DELETE FROM flowers WHERE flower_id = %s"
            if self.db.execute_query(query,(flower_id,)):
                self.load_flowers()
                QMessageBox.information(self, "Успех", "Цветок удален!")
            else:
                QMessageBox.critical(self, "Ошибка", "Ошибка при удалении!")

        except Exception as e:
            logging.error(f"Ошибка удаления: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")

    def edit_flower(self):
        try:
            selected_row = self.flowers_table.currentRow()
            if selected_row == -1:          # -1 это None
                QMessageBox.warning(self, "Ошибка", f"Выберите цветок!")

            flower_id = self.flowers_table.item(selected_row,0).text()
            dialog = AddFlowerDialog(self)

            dialog.name.setText(self.flowers_table.item(selected_row, 1).text())
            dialog.price.setText(self.flowers_table.item(selected_row, 2).text())
            dialog.quantity.setText(self.flowers_table.item(selected_row, 3).text())
            dialog.image_path.setText(self.flowers_table.item(selected_row, 4).text())

            if dialog.exec() == QDialog.DialogCode.Accepted:
                name, price, quantity, image_path = dialog.get_data()
                query = """
                    UPDATE flowers
                    SET name = %s, price = %s, quantity = %s, image_path = %s
                    WHERE flower_id = %s
                """
                if self.db.execute_query(query, (name, price, quantity, image_path, flower_id)):
                    self.load_flowers()
                    QMessageBox.information(self, "Успех", f"Данные обновлены!")
                else:
                    QMessageBox.critical(self, "Ошибка!", "Ошибка при обновлении")
        except Exception as e:
            logging.error(f"Ошибка редактирования: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")