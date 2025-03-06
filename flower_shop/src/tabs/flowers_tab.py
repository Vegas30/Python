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

    def init_ui(self):
        layout = QVBoxLayout()

        self.flowers_table = QTableWidget()
        self.flowers_table.setColumnCount(5)
        self.flowers_table.setHorizontalHeaderLabels(
            ["ID", "Название", "Цена", "Количество", "Изображение"]
        )
        self.flowers_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        control_layout = QHBoxLayout()
        self.btn_add = QPushButton("Добавить")
        self.btn_delete = QPushButton("Удалить")
        self.btn_edit = QPushButton("Изменить")
        self.refresh = QPushButton("Обновить")
        self.search = QLineEdit()
        self.search.setPlaceholderText("Поиск...")

        control_layout = addWidget(self.btn_add)
        control_layout = addWidget(self.btn_delete)
        control_layout = addWidget(self.btn_edit)

