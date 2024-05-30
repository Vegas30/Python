# 6.51. Известны оценки двух учеников по четырем предметам.
# Определить сумму оценок каждого ученика.

def summ_student():
    summ_1 = 0
    for _ in range(4):
        number = int(input("Введите оценку студента - "))
        summ_1 += number
    return summ_1


def main():
    student_1 = summ_student()
    print("Сумма оценок для первого студента: ", student_1)
    student_2 = summ_student()
    print("Сумма оценок для второго студента: ", student_2)


main()
