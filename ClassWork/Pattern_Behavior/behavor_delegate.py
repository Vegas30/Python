from abc import ABC, abstractmethod


# Общий интерфейс делегата
class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass


# Делегат для форматирования в Markdown
class MarkdownFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return f"**{text}**"  # Пример: жирный текст в Markdown


# Делегат для форматирования в HTML
class HTMLFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return f"<strong>{text}</strong>"  # Пример: жирный текст в HTML


# Делегатор
class TextEditor:
    def __init__(self, formatter: TextFormatter):
        self.formatter = formatter

    def set_formatter(self, formatter: TextFormatter):
        self.formatter = formatter

    def display_text(self, text: str):
        print(self.formatter.format(text))


# Клиентский код
if __name__ == "__main__":
    editor = TextEditor(MarkdownFormatter())
    editor.display_text("Hello, world!")  # Форматирование в Markdown

    editor.set_formatter(HTMLFormatter())
    editor.display_text("Hello, world!")  # Форматирование в HTML
