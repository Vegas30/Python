from PySide6.QtWidgets import QApplication, QMainWindow
from osnova_py import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.setupUi(self)

        self.db = Database()
        self.load_tasks()

        # self.pushButton.clicked.connect(self.add_item)
        self.pushButton_2.clicked.connect(self.delete_task)
    def load_tasks(self):
        self.listWidget.clear()
        tasks = self.db.get_tasks()
        for task in tasks:
            task_text = f"ID:{task[0]}\n-{task[1]}\n-Категория: {task[2]}\n-Статус: {task[3]}\n-Приоритет: {task[4]}"
            self.listWidget.addItem(task_text)

    def delete_task(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            task_id = int(selected_item.text().split('\n')[0].split(':')[1])
            self.db.delete_task(task_id)
            self.load_tasks()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()