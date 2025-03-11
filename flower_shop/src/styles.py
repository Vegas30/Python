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

    
"""
