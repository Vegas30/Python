from abc import ABC, abstractmethod


# Абстрактный класс посетителя
class Visitor(ABC):
    @abstractmethod
    def visit_html(self, element):
        pass

    @abstractmethod
    def visit_pdf(self, element):
        pass


# Абстрактный элемент
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


# Конкретные элементы
class HtmlDocument(DocumentElement):
    def accept(self, visitor: Visitor):
        visitor.visit_html(self)


class PdfDocument(DocumentElement):
    def accept(self, visitor: Visitor):
        visitor.visit_pdf(self)


# Конкретный посетитель
class ExportVisitor(Visitor):
    def visit_html(self, element):
        print("Экспортирование HTML документа...")

    def visit_pdf(self, element):
        print("Экспортирование PDF документа...")


class RenderVisitor(Visitor):
    def visit_html(self, element):
        print("Рендеринг HTML документа...")

    def visit_pdf(self, element):
        print("Рендеринг PDF документа...")


# Клиентский код
if __name__ == "__main__":
    documents = [HtmlDocument(), PdfDocument()]

    print("Экспорт документов:")
    export_visitor = ExportVisitor()
    for doc in documents:
        doc.accept(export_visitor)

    print("\nРендеринг документов:")
    render_visitor = RenderVisitor()
    for doc in documents:
        doc.accept(render_visitor)

# Результат выполнения:
# Экспорт документов:
# Экспортирование HTML документа...
# Экспортирование PDF документа...
#
#
# Рендеринг документов:
# Рендеринг HTML документа...
# Рендеринг PDF документа...
