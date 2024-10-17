# Создайте класс ComplexNumber, который будет
# представлять комплексное число и поддерживать операции сложения и вычитания с помощью
# магических методов __add__ и __sub__

#(3 + 4i) # 3 - действительная часть, а 4i - мнимая часть (между ними могут быть только + и -)

class ComplexNumber:
    def __init__(self, real:int, imagi:int) -> None:
        self.real = real
        self.imagi = imagi

    def __add__(self,other):
        return ComplexNumber(self.real + other.real, self.imagi + other.imagi)

    def __sub__(self,other):
        return ComplexNumber(self.real - other.real, self.imagi - other.imagi)

    def __str__(self):
        if self.imagi >= 0:
            return f"{self.real}+{self.imagi}i"
        elif self.imagi < 0:
            return f"{self.real}{self.imagi}i"

def main():
    complex1 = ComplexNumber(3,4)
    complex2 = ComplexNumber(4,2)
    #(3+4i) + (5+6i)
    add_complex_1_and_2 = complex1 + complex2
    sub_complex_1_and_2 = complex1 - complex2
    print(add_complex_1_and_2)
    print(sub_complex_1_and_2)

if __name__ == "__main__":
    main()



#Создайте классы Book и Library. Реализуйте возможность добавления и удаления книг
#из библиотеки через магические методы __len__, __getitem__, __delitem__
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Писатель замечательной книги {self.title} - {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]

    def __delitem__(self, index):
        del self.books[index]

    def output(self):
        print("-----------")
        for book in self.books:
            print(book)

    def add_book(self, book: Book):
        self.books.append(book)


def main():
    library_astr = Library()
    book1 = Book("Евгений Онегин", "Пушкин")
    book2 = Book("Война и мир", "Толстой")
    book3 = Book("Мертвые души", "Гоголь")
    print(book1,book2,book3,sep='\n')

    library_astr.add_book(book1)
    library_astr.add_book(book2)

    library_astr.output()

    print(f"Количество книг в библиотеке: {len(library_astr)}")
    print(f"Первая книга: {library_astr[0]}")
    del library_astr[0]
    print(f"Вы удалили первую книгу")
    print(f"Количество книг в библиотеке: {len(library_astr)}")
    print(f"Первая книга: {library_astr[0]}")

if __name__ == "__main__":
    main()


#3. Создайте класс MaksBank, который будет представлять банковский счет. Реализуйте
# магические методы для сравнения счетов по балансу (__eq__ (==), __lt__(<), __le__(<=))

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __str__(self):
        return f"Владелец карты {self.owner}, имеет баланс на счету {self.balance}"

def main():
    acc1 = BankAccount("Igor", 1000)
    acc2 = BankAccount("Sergey", 3000)
    acc3 = BankAccount("Other", 10000)

    print(acc1 == acc2)
    print(acc1 < acc2)
    print(acc2 <= acc3)
    print(acc1,acc2,acc3,sep="\n")

if __name__ == "__main__":
    main()