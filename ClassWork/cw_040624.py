import math

list1 = [1, 2, 3, 4]
result = sum(list1)
result2 = math.fsum(list1)
print(result)
print(result2)
summ = 0
for item in list1:
    summ += item
print(summ)

list2 = ["!", "@", "#"]
list2.sort(reverse=True)
print(list2)

list3 = [1, 2, 3, 4, [2, 3]]
list4 = list3.copy()
list4.append(5)
list4[4].append(6)
list4[4][-1] = 7
print(list3, list4)

