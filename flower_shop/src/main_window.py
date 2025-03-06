from PyQt6.QtWidgets import QMainWindow, QTabWidget
from database import Database
from tabs.flowers_tab import FlowersTab
class FlowerShopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()

    def init_ui(self):
        self.setWindowTitle("Flower Shop")
        self.setGeometry(100, 100, 1200, 800)
        self.setup_tabs()

    def setup_tabs(self):
        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        tabs.addTab(FlowersTab)

