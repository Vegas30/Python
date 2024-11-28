# Рассмотрим текстовый редактор с функцией "Отмена".
# Хранитель (Memento)
class Memento:
    def __init__(self, state):
        self._state = state


    def get_state(self):
        return self._state


# Оригинатор (Originator)
class TextEditor:
    def __init__(self):
        self._content = ""


    def write(self, text):
        self._content += text


    def get_content(self):
        return self._content


    def save(self):
        return Memento(self._content)


    def restore(self, memento):
        self._content = memento.get_state()


# Опекун (Caretaker)
class Caretaker:
    def __init__(self, editor):
        self._editor = editor
        self._history = []


    def backup(self):
        print("Сохраняем текущее состояние.")
        self._history.append(self._editor.save())


    def undo(self):
        if not self._history:
            print("История пуста.")
            return
        memento = self._history.pop()
        print("Восстанавливаем предыдущее состояние.")
        self._editor.restore(memento)


# Клиентский код
editor = TextEditor()
caretaker = Caretaker(editor)


editor.write("Привет, ")
caretaker.backup()


editor.write("мир!")
caretaker.backup()


print("Текущий текст:", editor.get_content())


caretaker.undo()
print("После отмены:", editor.get_content())


caretaker.undo()
print("После повторной отмены:", editor.get_content())


# Результат выполнения:
# Сохраняем текущее состояние.
# Сохраняем текущее состояние.
# Текущий текст: Привет, мир!
# Восстанавливаем предыдущее состояние.
# После отмены: Привет,
# Восстанавливаем предыдущее состояние.
# После повторной отмены: