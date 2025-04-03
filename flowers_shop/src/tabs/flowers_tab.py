from PyQt6.QtWidgets import (
    QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit, QHeaderView, QMessageBox, QDialog, QSizePolicy, QFileDialog, QTabWidget
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from dialogs import AddFlowerDialog, ViewStats
import logging

#Основной класс FlowersTab
class FlowersTab(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db #сохраняем объект базы данных
        self.init_ui() #инициализируем интерфейс
        self.load_flowers() #загружаем данные о цветах

    def init_ui(self):
        main_layout = QVBoxLayout()

        #1. Верхняя панель с кнопками управления
        top_panel = QHBoxLayout()

        #кнопки управления
        self.btn_add = QPushButton("Добавить")
        self.btn_delete = QPushButton("Удалить")
        self.btn_edit = QPushButton("Редактировать")

        #поле поиска
        self.search = QLineEdit()
        self.search.setPlaceholderText("Поиск...")

        #добавляем элементы на верхнюю панель
        top_panel.addWidget(self.btn_add)
        top_panel.addWidget(self.btn_delete)
        top_panel.addWidget(self.btn_edit)
        top_panel.addWidget(self.search)

        #2. Таблица для отображения цветов
        self.flowers_table = QTableWidget()
        self.flowers_table.setColumnCount(5)
        self.flowers_table.setHorizontalHeaderLabels(
            ["ID","Название", "Цена", "Количество", "Изображение"])
        self.flowers_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        self.flowers_table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        #3. Нижняя панель с дополнительными функциями
        bottom_panel = QHBoxLayout()

        # Левая часть нижней панели - кнопки с иконками
        left_button_panel = QHBoxLayout()

        # Кнопка обновления данных
        self.btn_refresh = QPushButton()
        self.btn_refresh.setIcon(QIcon.fromTheme("view-refresh"))
        self.btn_refresh.setToolTip("Обновить данные") #при наведении
        self.btn_refresh.setFixedSize(32, 32) #размер кнопок высота-ширина
        self.btn_refresh.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        #Кнопка просмотра статистики
        self.btn_stats = QPushButton()
        self.btn_stats.setIcon(QIcon.fromTheme("document-properties"))
        self.btn_stats.setToolTip("Показать статистику")
        self.btn_stats.setFixedSize(32,32)
        self.btn_stats.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Добавляем кнопки в левую панель
        left_button_panel.addWidget(self.btn_refresh)
        left_button_panel.addWidget(self.btn_stats)

        left_button_panel.addStretch()

        # Правая часть нижней панели - кнопки экспорта
        right_button_panel = QHBoxLayout()
        self.btn_export_excel = QPushButton("Экспорт в Excel")
        self.btn_export_pdf = QPushButton("Экспорт в PDF")

        # Добавляем элементы в правую панель
        right_button_panel.addStretch()
        right_button_panel.addWidget(self.btn_export_excel)
        right_button_panel.addWidget(self.btn_export_pdf)

        #Собираем нижнюю панель из левой и правой частей
        bottom_panel.addLayout(left_button_panel, stretch=1)
        bottom_panel.addLayout(right_button_panel, stretch=1)

        #Собираем основной интерфейс
        main_layout.addLayout(top_panel)
        main_layout.addWidget(self.flowers_table)
        main_layout.addLayout(bottom_panel)

        self.setLayout(main_layout)

        # Подключаем сигналы
        self.btn_add.clicked.connect(self.add_flower)
        self.search.textChanged.connect(self.handle_search_flowers)
        self.btn_delete.clicked.connect(self.delete_flower)
        self.btn_refresh.clicked.connect(self.load_flowers)
        self.btn_edit.clicked.connect(self.edit_flower)
        self.btn_export_excel.clicked.connect(self.export_to_excel)
        self.btn_export_pdf.clicked.connect(self.export_to_pdf)
        self.btn_stats.clicked.connect(self.show_stats)

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

    def handle_search_flowers(self):
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
            logging.error(f"Ошибка поиска: {str(e)}")
            QMessageBox.critical(self, "Ошибка", "Ошибка фильтрации")


    def add_flower(self):
        try:
            dialog = AddFlowerDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                name, price, quantity, image_path = dialog.get_data()
                query = """
                    INSERT INTO flowers (name, price, quantity, image_path)
                    VALUES (%s, %s, %s, %s)
                """

                if self.db.execute_query(query, (name,price,quantity,image_path)):
                    self.load_flowers()
                    QMessageBox.information(self, "Успех", "Цветок добавлен!")
                else:
                    QMessageBox.critical(self, "Ошибка!", "Ошибка при добавлении")

        except Exception as e:
            logging.error(f"Ошибка добавления: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")


    def delete_flower(self):
        try:
            selected_row = self.flowers_table.currentRow()
            if selected_row == -1:
                QMessageBox.warning(self, "Ошибка", "Выберите цветок!")

            flower_id = self.flowers_table.item(selected_row,0).text()
            query = "DELETE FROM flowers WHERE flower_id = %s"
            if self.db.execute_query(query, (flower_id,)):
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
            if selected_row == -1:
                QMessageBox.warning(self, "Ошибка", "Выберите цветок!")


            flower_id = self.flowers_table.item(selected_row, 0).text()
            dialog = AddFlowerDialog(self)

            dialog.name.setText(self.flowers_table.item(selected_row,1).text())
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
                if self.db.execute_query(query, (name,price,quantity,image_path, flower_id)):
                    self.load_flowers()
                    QMessageBox.information(self, "Успех", "Данные обновлены!")
                else:
                    QMessageBox.critical(self, "Ошибка!", "Ошибка при обновлении")

        except Exception as e:
            logging.error(f"Ошибка редактирования: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")

    def export_to_excel(self):
        try:
            import pandas as pd
        except ImportError as e:
            QMessageBox.critical(
                self, "Ошибка",
                "Для экспорта в Excel необходимо установить библиотки: \n"
                "pandas, openpyxl, xlswriter\n\n"
                "Выполните: pip install pandas openpyxl xlsxwriter"
            )
            return

        if self.flowers_table.rowCount() == 0:
            QMessageBox.warning(self,"Ошибка", "Нет данных для экспорта!")
            return

        try:
            #получает заголовки таблицы
            headers = [
                self.flowers_table.horizontalHeaderItem(i).text()
                for i in range(self.flowers_table.columnCount())
            ]

            #собираем данные из таблицы
            data = []
            for row in range(self.flowers_table.rowCount()):
                row_data = []
                for col in range(self.flowers_table.columnCount()):
                    item = self.flowers_table.item(row,col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)

            df = pd.DataFrame(data, columns=headers)
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Сохранить файл Excel","", "Excel File (*.xlsx)"
            )

            if file_path:
                df.to_excel(file_path, index=False, engine="openpyxl")
                QMessageBox.information(self,"Успех", "Данные успешно экспортированы в Excel!")

        except Exception as e:
            logging.error(f"Ошибка экспорта в Excel: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка при экспорте в Excel:\n{str(e)}")

    def export_to_pdf(self):
        try:
            from reportlab.lib.pagesizes import A4, landscape
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            from reportlab.lib.units import inch
            import os

        except ImportError as e:
            QMessageBox.critical(self, "Ошибка",
                                f"Не удалось импортировать необходимые библиотеки:\n{str(e)}\n\n"
                                 "Выполните: pip install reportlab"
            )
            return

        try:
            try:
                pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
                font_name = 'DejaVuSans'
            except:
                try:
                    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
                    font_name = 'Arial'
                except:
                    font_name = 'Helvetica'
                    QMessageBox.warning(self, "Предупреждение", "Не найден шрифт с поддержкой кириллицы. Возможны проблемы с отображением русским символов")

            headers = [
                self.flowers_table.horizontalHeaderItem(i).text()
                for i in range(self.flowers_table.columnCount())
            ]

            #собираем данные из таблицы
            data = [headers]
            for row in range(self.flowers_table.rowCount()):
                row_data = []
                for col in range(self.flowers_table.columnCount()):
                    item = self.flowers_table.item(row,col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)

            file_path, _ = QFileDialog.getSaveFileName(
                self, "Сохранить файл PDF","", "PDF Files (*.pdf)"
            )

            if file_path:
                #Создаем PDF документ в той директории что указали
                doc = SimpleDocTemplate(file_path, pagesize=landscape(A4), encoding='utf-8')
                elements = []

                #Настройка стилей
                styles = getSampleStyleSheet()
                style_normal = styles['Normal']
                if font_name != 'Helvetica':
                    style_normal.fontName = font_name
                style_normal.encoding = 'UTF-8'

                #Стиль заголовка
                title_style = styles['Title']
                if font_name != 'Helvetica':
                    title_style.fontName = font_name

                elements.append(Paragraph("Список цветов", title_style))
                elements.append(Spacer(1, 0.2 * inch)) #не помню что делает единица

                col_widths = [2.5 * inch, 1 * inch, 1.5 * inch, 3 * inch]
                table = Table(data, colWidths=col_widths)

                table_style = TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#70b090')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('FONTNAME', (0,0), (-1,-1), font_name),
                    ('FONTSIZE', (0,0),(-1,0), 9),
                    ('BOTTOMPADDING',(0,0), (-1,0), 8),
                    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f5faf8')),
                    ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#c0d0c8')),
                    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ])
                table.setStyle(table_style)
                elements.append(table)

                doc.build(elements)
                QMessageBox.information(self, "Успех!", "Данные успешно экспортированы в PDF!")

        except Exception as e:
            logging.error(f"Ошибка экспорта в PDF: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка при экспорте в PDF:\n{str(e)}")


    def show_stats(self):
        try:
            self.db.cursor.execute("SELECT name, price, quantity FROM flowers")
            all_flowers = self.db.cursor.fetchall()

            if not all_flowers:
                QMessageBox.information(self,"Информация", "Нет данных для отображения статистики")
                return
            #1. Подключение окна
            dialog = ViewStats(self)
            dialog.exec()
            #2. Вкладки с графиками
            tab_widget = QTabWidget()

            #контейнеры для хранения графиков
            self.figures = [] #фигуры matplotlib
            self.canvases = [] #холсты для отображения

            # Вкладкая 1: График цен
            price_tab = QWidget()
            price_layout = QVBoxLayout()

            self.price_fig = Figure(figsize=(10,5))
            self.price_canvas = FigureCanvas(self.price_fig)
            self.figures.append(self.price_fig)
            self.canvases.append(self.price_canvas)

            price_layout.addWidget(self.price_canvas)

            #Кнопка сохранения графика цен
            btn_save_price = QPushButton("Скачать график цен")
            btn_save_price.clicked.connect(lambda: self.save_figure(self.price_fig, "Цены_на_цветы"))
            price_layout.addWidget(btn_save_price, alignment=Qt.AlignmentFlag.AlignRight)

            price_tab.setLayout(price_layout)
            tab_widget.addTab(price_tab, "Цены")


        except Exception as e:
            pass

    def save_figure(self, figure, default_name):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить график", default_name, "PNG Images (*.png);;JPEG Images (*.jpg *.jpeg)"
        )

        if file_path:
            try:
                figure.savefig(file_path, dpi=300, bbox_inches='tight')
                QMessageBox.information(self, "Успех!", "График успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить график:\n{str(e)}")