
# Модель (Model)
class UserModel:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ViewModel
class UserViewModel:
    def __init__(self, user_model):
        self.user_model = user_model
        self.name = user_model.name
        self.age = user_model.age


    def update_name(self, new_name):
        self.user_model.name = new_name
        self.name = new_name


    def update_age(self, new_age):
        if new_age > 0:  # Простая валидация
            self.user_model.age = new_age
            self.age = new_age
        else:
            raise ValueError("Возраст должен быть положительным")


# Представление (View)
class UserView:
    def __init__(self, view_model):
        self.view_model = view_model


    def display(self):
        print(f"Имя: {self.view_model.name}, Возраст: {self.view_model.age}")


    def change_name(self, new_name):
        self.view_model.update_name(new_name)
        self.display()


    def change_age(self, new_age):
        try:
            self.view_model.update_age(new_age)
            self.display()
        except ValueError as e:
            print(f"Ошибка: {e}")


# Использование
if __name__ == "__main__":
    user = UserModel("Анна", 25)
    user_vm = UserViewModel(user)
    user_view = UserView(user_vm)


    user_view.display()  # Имя: Анна, Возраст: 25
    user_view.change_name("Иван")  # Имя: Иван, Возраст: 25
    user_view.change_age(30)  # Имя: Иван, Возраст: 30
    user_view.change_age(-5)  # Ошибка: Возраст должен быть положительным