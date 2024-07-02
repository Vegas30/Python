# 11.35. Оценки, полученные спортсменом в соревнованиях по
# фигурному катанию (в баллах), хранятся в массиве из 18 элементов. В
# первых шести элементах записаны оценки по обязательной
# программе; седьмом, ..., двенадцатом — по короткой программе; в
# остальных — по произвольной программе. Выяснить, по какому виду
# программы спортсмен показал лучший результат

import random

def main():
    # Создаем массив из 18 случайных оценок от 0 до 10
    scores = [random.randint(0, 10) for _ in range(18)]
    print("Оценки спортсмена:", scores)

    # Разделяем оценки по программам
    compulsory_scores = scores[:6]
    short_program_scores = scores[6:12]
    free_skating_scores = scores[12:]

    # Вычисляем средние оценки
    compulsory_average = sum(compulsory_scores) / len(compulsory_scores)
    short_program_average = sum(short_program_scores) / len(short_program_scores)
    free_skating_average = sum(free_skating_scores) / len(free_skating_scores)

    # Определяем лучший результат
    best_average = max(compulsory_average, short_program_average, free_skating_average)
    if best_average == compulsory_average:
        best_program = "обязательная программа"
    elif best_average == short_program_average:
        best_program = "короткая программа"
    else:
        best_program = "произвольная программа"

    print(f"Лучший результат по {best_program}: {best_average:.2f} балла")

if __name__ == "__main__":
    main()
