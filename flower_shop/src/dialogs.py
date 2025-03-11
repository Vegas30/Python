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
            self, "Выбрать изображение", "", "Images (*.png,*.jpg,*.jpeg)")
        if file_name:
            self.image_path.setText(file_name)

    def get_data(self):
        return(
            self.name.text(),
            float(self.price.text()),
            int(self.quantity.text()),
            self.image_path.text()
        )