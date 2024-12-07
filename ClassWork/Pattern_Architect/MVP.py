
# Модель
class Model:
    def __init__(self):
        self.data = "Привет, MVP!"


    def get_data(self):
        return self.data


# Представление
class View:
    def __init__(self, presenter):
        self.presenter = presenter


    def show_data(self, data):
        print(f"Данные: {data}")


    def user_input(self, new_data):
        self.presenter.update_data(new_data)


# Посредник
class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view


    def load_data(self):
        data = self.model.get_data()
        self.view.show_data(data)


    def update_data(self, new_data):
        self.model.data = new_data
        self.load_data()


# Использование
if __name__ == "__main__":
    model = Model()
    presenter = Presenter(model, None)
    view = View(presenter)
    presenter.view = view


    presenter.load_data()  # Отображает: Данные: Привет, MVP!
    view.user_input("Обновленные данные!")  # Отображает: Данные: Обновленные данные!
