# Factory Method
from abc import ABC, abstractmethod


# Базовый интерфейс Report (Продукт)
class Report(ABC):
   @abstractmethod
   def generate(self) -> str:
       pass


# Конкретные продукты
class PDFReport(Report):
   def generate(self) -> str:
       return "Generating PDF Report..."




# Абстрактная фабрика (Creator)
class ReportFactory(ABC):
   @abstractmethod
   def create_report(self) -> Report:
       pass


   def generate_report(self) -> str:
       report = self.create_report()
       return report.generate()


# Конкретные фабрики (Concrete Creators)
class PDFReportFactory(ReportFactory):
   def create_report(self) -> Report:
       return PDFReport()





# Клиентский код
def client_code(factory: ReportFactory) -> None:
   print(factory.generate_report())


pdf_factory = PDFReportFactory()
client_code(pdf_factory)  # Output: Generating PDF Report...


