# 3.31. Записать условие, которое является истинным, когда:
# а) целое N кратно пяти или семи;
# б) целое N кратно четырем и не оканчивается нулем.

N = int(input())

res_1 = N % 5 == 0 or N % 7 == 0
res_2 = N % 4 == 0 and N % 10 != 0

print(res_1, res_2, sep="\n")

x = int(input())
y = int(input())

# ж)
res_3 = (1 <= x <= 3) and (-1 >= y >= -2)
