import sys
from PyQt6.QtWidgets import QApplication
import logging
from main_window import FlowerShopApp

logging.basicConfig(
    filename='app_errors.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    app = QApplication(sys.argv)
    window = FlowerShopApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()