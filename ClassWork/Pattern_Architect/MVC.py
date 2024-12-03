# Модель
class Model:
    def __init__(self):
        self.data = "Привет, мир!"


    def get_data(self):
        return self.data


    def set_data(self, new_data):
        self.data = new_data


# Представление
class View:
    def display(self, data):
        print(f"Данные: {data}")


# Контроллер
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view


    def update_data(self, new_data):
        self.model.set_data(new_data)


    def display_data(self):
        data = self.model.get_data()
        self.view.display(data)


if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)


    controller.display_data()  # Отображает: Данные: Привет, мир!
    controller.update_data("Добрый день!")
    controller.display_data()  # Отображает: Данные: Добрый день!