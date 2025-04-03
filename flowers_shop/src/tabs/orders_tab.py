from PyQt6.QtWidgets import (
    QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QHBoxLayout, QPushButton, QComboBox, QLineEdit, QHeaderView, QMessageBox, QDialog, QLabel, QInputDialog, QMenu
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from dialogs import CreateOrderDialog
import logging

logging.basicConfig(
    filename='app_errors_orders.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class OrdersTab(QWidget):
    def __init__(self,db):
        super().__init__()
        self.db = db
        self.init_ui()
        self.load_orders()

    def init_ui(self):
        layout = QVBoxLayout()
        self.orders_table = QTableWidget()
        self.orders_table.setColumnCount(6)
        self.orders_table.setHorizontalHeaderLabels(
            ["ID","Клиент","Статус","Дата создания","Дата обновления","Сумма"]
        )
        self.orders_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        self.orders_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.orders_table.customContextMenuRequested.connect(self.show_order_context_menu) #почитать

        control_layout = QHBoxLayout()
        self.btn_create = QPushButton("Создать заказ")
        self.filter_status = QComboBox()
        self.filter_status.addItems(["Все", "Новый",
                                     "В обработке", "Выполнен", "Отменен"])

        control_layout.addWidget(self.btn_create)
        control_layout.addWidget(QLabel("Фильтр:"))
        control_layout.addWidget(self.filter_status)

        layout.addLayout(control_layout)
        layout.addWidget(self.orders_table)
        self.setLayout(layout)

        self.filter_status.currentIndexChanged.connect(self.load_orders)
        self.btn_create.clicked.connect(self.create_order)

    def load_orders(self):
        try:
            status = self.filter_status.currentText()
            query = """
                SELECT o.order_id, c.full_name, o.status, o.order_date, o.update_date, 
                get_order_total(o.order_id)
                FROM orders o
                JOIN clients c ON o.client_id = c.client_id
                WHERE CASE WHEN %s = 'Все' THEN TRUE ELSE o.status = %s END
            """
            self.db.cursor.execute(query, (status,status))
            orders = self.db.cursor.fetchall()

            self.orders_table.setRowCount(len(orders))
            for row_idx, order in enumerate(orders):
                for col_idx, data in enumerate(order):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

                    self.orders_table.setItem(row_idx, col_idx, item)
        except Exception as e:
            logging.error(f"Ошибка загрузки заказов: {str(e)}")
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить данные")

    def show_order_context_menu(self, position):
        try:
            menu = QMenu()
            change_status_action = menu.addAction("Изменить статус")
            change_status_action.triggered.connect(self.change_order_status)
            menu.exec(self.orders_table.viewport().mapToGlobal(position))

        except Exception as e:
            logging.error(f"Ошибка контекстного меню: {str(e)}")

    def change_order_status(self):
        try:
            selected_row = self.orders_table.currentRow()
            if selected_row == -1:
                QMessageBox.warning(self, "Ошибка", "Выбрите заказ!")
                return

            order_id_item = self.orders_table.item(selected_row, 0)
            status_item = self.orders_table.item(selected_row, 2)

            if not order_id_item or not status_item:
                QMessageBox.critical(self, "Ошибка", "Некорректные данные в таблице!")
                return

            order_id = order_id_item.text()
            current_status = status_item.text()
            statuses = ["Новый", "В обработке", "Выполнен", "Отменен"]

            new_status, ok = QInputDialog.getItem(
                self,
                "Изменение статуса",
                "Выберите новый статус:",
                statuses,
                current = statuses.index(current_status) if current_status in statuses else 0,
                editable=False
            )

            if ok and new_status != current_status:
                query = "UPDATE orders SET status = %s WHERE order_id = %s"
                if self.db.execute_query(query, (new_status, order_id)):
                    self.load_orders()
                    QMessageBox.information(self, "Успех", "Статус обновлен!")
            else:
                QMessageBox.critical(self, "Ошибка", "Ошибка обновления!")

        except Exception as e:
            logging.error(f"Ошибка изменения статуса: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")



    def create_order(self):
        try:
            dialog = CreateOrderDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                client_id = dialog.client_combo.currentData()
                items = dialog.get_items()

                if not items:
                    QMessageBox.warning(self, "Ошибка", "Добавьте позиции в заказ!")
                    return

                try:
                    self.db.cursor.execute("""
                        INSERT INTO orders (client_id, status)
                        VALUES (%s, 'Новый')
                        RETURNING order_id
                    """, (client_id,))
                    order_id = self.db.cursor.fetchone()[0]

                    for flower_name, quantity in items:
                        self.db.cursor.execute(
                            "SELECT flower_id FROM flowers WHERE name = %s", (flower_name,)
                        )
                        result = self.db.cursor.fetchone()
                        if not result:
                            raise ValueError(f"Цвтеток '{flower_name}' не найден")

                        flower_id = result[0]
                        self.db.cursor.execute("""
                            INSERT INTO order_items (order_id, flower_id, quantity)
                            VALUES (%s, %s, %s)
                        """, (order_id, flower_id, quantity))

                    self.db.conn.commit()
                    self.load_orders()
                    QMessageBox.information(self, "Успех", "Заказ создан!")

                except Exception as e:
                    self.db.conn.rollback()
                    raise e

        except Exception as e:
            logging.error(f"Ошибка создания заказа: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")

    def get_flower_price(self, flower_id):
        try:
            self.db.cursor.execute("SELECT price FROM flowers WHERE flower_id = %s", (flower_id,))
            result = self.db.cursor.fetchone()
            if not result:
                raise ValueError("Цветок не найден")
            return float(result[0])

        except Exception as e:
            logging.error(f"Ошибка получения цены: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")
            return 0.0
