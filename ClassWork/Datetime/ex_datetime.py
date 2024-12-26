# Задача:
# Напишите программу, которая рассчитывает общее количество рабочих часов, проведенных сотрудником на проекте. У каждого сотрудника есть записи о начале и окончании рабочего дня. Данные хранятся в файле work_log.txt в следующем формате:
#
# 2024-12-20 09:00:00, 2024-12-20 17:00:00
# 2024-12-21 10:00:00, 2024-12-21 15:00:00
# 2024-12-22 08:30:00, 2024-12-22 16:45:00
# Каждая строка содержит две даты и времени: время начала работы и окончания работы. Программа должна:
#
# Прочитать файл.
# Рассчитать общее количество отработанных часов (с точностью до минут).
# Вывести итог в виде:
# Общее время: 22 часов и 45 минут.

from datetime import datetime, timedelta

def calculate_work_hours(filename):
    total_time = timedelta()
    try:
        with open(filename, "r") as file:
            for line in file:
                start_time, end_time = line.strip().split(", ")
                start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
                end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

                work_time = end - start
                total_time += work_time

            total_hours = total_time.total_seconds() // 3600
            total_minutes = (total_time.total_seconds() % 3600) // 60
            print(total_hours, total_minutes)
            print(f"Общее время {int(total_hours)} часов и {int(total_minutes)} минут")

    except Exception as e:
        print("Ошибка", e)

filename = "work_log.txt"
calculate_work_hours(filename)