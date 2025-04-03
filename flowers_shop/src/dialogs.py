from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QLabel, QHeaderView,
    QStatusBar, QDialog, QFormLayout, QMessageBox, QInputDialog, QFileDialog, QSpinBox, QMenu
)

class AddFlowerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить цветок")
        self.layout = QFormLayout()

        self.name = QLineEdit()
        self.price = QLineEdit()
        self.quantity = QLineEdit()
        self.image_path = QLineEdit()
        self.browse_btn = QPushButton("Выбрать")

        self.layout.addRow("Название", self.name)
        self.layout.addRow("Цена ($):", self.price)
        self.layout.addRow("Количество:", self.quantity)
        self.layout.addRow("Изображение:", self.image_path)
        self.layout.addWidget(self.browse_btn)

        self.buttons = QPushButton("Добавить")
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)
        self.browse_btn.clicked.connect(self.browse_image)
        self.buttons.clicked.connect(self.accept)

    def browse_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Выбрать изображение", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.image_path.setText(file_name)

    def get_data(self):
        return(
            self.name.text(),
            float(self.price.text()),
            int(self.quantity.text()),
            self.image_path.text()
        )

class AddClientDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить клиента")
        self.layout = QFormLayout()

        self.name = QLineEdit()
        self.phone = QLineEdit()
        self.email = QLineEdit()
        self.surname = QLineEdit()
        self.middle_name = QLineEdit()

        self.layout.addRow("Фамилия:", self.surname)
        self.layout.addRow("Имя:", self.name)
        self.layout.addRow("Отчество:", self.middle_name)
        self.layout.addRow("Телефон:", self.phone)
        self.layout.addRow("Email", self.email)

        self.buttons = QPushButton("Сохранить")
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)
        self.buttons.clicked.connect(self.accept)

    def get_data(self):
        return(
            self.surname.text(),
            self.name.text(),
            self.middle_name.text(),
            self.phone.text(),
            self.email.text()
        )

class CreateOrderDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Новый заказ")
        self.layout = QVBoxLayout()

        self.client_combo = QComboBox()
        self.flower_combo = QComboBox()
        self.quantity = QSpinBox()
        self.quantity.setMinimum(1)
        self.btn_add_item = QPushButton("Добавить позицию")
        self.order_items = QTableWidget()
        self.order_items.setColumnCount(3)
        self.order_items.setHorizontalHeaderLabels(["Цветок", "Количество", "Цена"])

        form_layout = QFormLayout()
        form_layout.addRow("Клиент:", self.client_combo)
        form_layout.addRow("Цветок:", self.flower_combo)
        form_layout.addRow("Количество:", self.quantity)

        self.layout.addLayout(form_layout)
        self.layout.addWidget(self.btn_add_item)
        self.layout.addWidget(self.order_items)

        self.buttons = QPushButton("Создать заказ")
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)
        self.load_data()

        self.buttons.clicked.connect(self.accept)
        self.btn_add_item.clicked.connect(self.add_item)

    def load_data(self):
        self.parent.db.cursor.execute("SELECT client_id, full_name FROM clients")
        self.client_combo.clear()
        for client_id, name in self.parent.db.cursor:
            self.client_combo.addItem(name, client_id)

        self.parent.db.cursor.execute("SELECT flower_id, name, price FROM flowers")
        self.flower_combo.clear()
        for flower_id, name, price in self.parent.db.cursor:
            self.flower_combo.addItem(f"{name} ({price} руб)", flower_id)

    def add_item(self):
        try:
            if self.flower_combo.currentData() is None:
                raise ValueError("Не выбран цветок")

            flower_id = self.flower_combo.currentData()
            name = self.flower_combo.currentText().split(' (')[0]
            quantity = self.quantity.value()

            self.parent.db.cursor.execute("SELECT quantity FROM flowers WHERE flower_id = %s", (flower_id,))
            available = self.parent.db.cursor.fetchone()[0]

            if quantity > available:
                QMessageBox.warning(self, "Ошибка", "Недостаточно цветов на складе!")
                return

            row = self.order_items.rowCount()
            self.order_items.insertRow(row)
            self.order_items.setItem(row, 0, QTableWidgetItem(name))
            self.order_items.setItem(row, 1, QTableWidgetItem(str(quantity)))
            self.order_items.setItem(row, 2, QTableWidgetItem(f"{self.parent.get_flower_price(flower_id) * quantity:.2f}"))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))


    def get_items(self):
        items = []
        for row in range(self.order_items.rowCount()):
            flower_item = self.order_items.item(row, 0)
            quantity_item = self.order_items.item(row, 1)

            if flower_item and quantity_item:
                flower_name = flower_item.text()
                quantity = int(quantity_item.text())
                items.append((flower_name, quantity))

        return items


class ViewStats(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Статитистика цветов")
        self.setMinimumSize(1000,700)

        main_layout = QVBoxLayout()

        #1. Панель фильтров
        filter_panel = QWidget()
        filter_layout = QHBoxLayout()

        #Фильтр по цене
        price_filter = QComboBox()
        price_filter.addItems(["Все цены", "До 10", "10-20", "20-50", "Выше 50"])

        #Фильтр по количеству
        quantity_filter = QComboBox()
        quantity_filter.addItems(["Все количества", "Нет в наличии (0)", "Меньше 10", "10-30", "Больше 30"])

        btn_apply = QPushButton("Применить фильтры")

        #Добавляем элементы на панель фильтров
        filter_layout.addWidget(QLabel("Фильтр по цене:"))
        filter_layout.addWidget(price_filter)
        filter_layout.addWidget(QLabel("Фильтр по количеству:"))
        filter_layout.addWidget(quantity_filter)
        filter_layout.addWidget(btn_apply)
        filter_layout.addStretch()

        filter_panel.setLayout(filter_layout)
        main_layout.addWidget(filter_panel)

