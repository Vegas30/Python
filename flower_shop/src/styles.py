APP_STYLESHEET = """
    /* Основное окно */
    QMainWindow {
        background-color: #f5faf8; /* Задний фон */
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    
    QTabBar::tab {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f5faf8, stop:0.4 #e0f0ec,stop: 0.5 #d0e8e4, stop:1 #c0e0dc);
        border:1px solid #a0c0d8; 
        border-radius: 5px;
        min-width: 100px; 
        padding: 10px 20px; /* отступ текста внутри кнопки, внутренний отступ*/
        margin-right: 4px; /* отступ кнопки, внешний отступ*/
        /* margin-left: 10px; */
        color: #405050;  /* цвет текста */
        font-weight: 600;  /* толщина шрифта */
        font-size: 14px; 
    }

    QTableWidget {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f5faf8, stop:0.4 #e0f0ec,stop: 0.5 #d0e8e4, stop:1 #c0e0dc);
        border:1px solid #a0c0d8;
        color: #303030;
        font-size: 14px;
        border: 1px solid #c0d0c8;
        gridline-color: #d0e0dc;
    }

    QTabBar::tab::selected {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:0.4 #c8e8d8, stop: 0.5 #b0e0c8, stop:1 #98d8b8);
        color: #306050;
        border:2px solid #80a098;
    }
    
    QTableWidget::item {
        border_bottom: 2px solid #e0ece8;
        border-right: 2px solid #e0ece8;
    }
    QTableWidget::item:selected {
        background-color: #a0d8c0;
        color: #204030;
    }
    
    /* Заголовки столбцов */
    QHeaderView::section {
        background-color: #70b090;
        color: white;
        padding: 8px;
        font-weight: bold;
        border: none;
    }
    
     QTableWidget::item:first-child {
        font-weight: bold;
        color: #406050;
    }
    
    /* Кнопки */
    QPushButton {
        background-color: #90d0b0;
        border: 1px solid #70a080;
        border-radius: 5px;
        color: white;
        padding: 8px 20px;
        font-size: 14px;
        font-weight: 600;
        min-width: 100px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        transition: all 0.3s ease;  /* не работает */
    }
    
    QPushButton:hover {
        background-color: #a0e0c0;
        border-color: #80b090;
        transform: translateY(-1px);    
    }
    
    QPushButton:pressed {
        background-color: #70a080;
        border-color: #609070;
    }
    
    /* Поля ввода */
    QLineEdit {
        background-color: rgba(255,255,255,,220);
        border: 1px solid #a0b8b0;
        border-radius: 4px;
        padding: 8px 12px;
        color: #405060;
        font-size: 14px;
        selection-background-color: #a0e0c0;
    }
    QLineEdit:focus {
    border: 2px solid #80c8a8;
    background-color: white:
    }
    
"""
