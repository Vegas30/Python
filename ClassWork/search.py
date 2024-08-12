# Дано натуральное число. Определить:
# а) количество цифр 3 в нем;

#import random
#from random import randint
import random as r

number = r.randint(1000000,10000000000)
print(number)
#1.
count = 0
for i in str(number):
    if i == '3':
        count += 1
else:
    if count > 0:
        print(count)
    else:
        print("Троек нет")

#2.
result = str(number).count('3')
print(result)

#3.
str_number = list(str(number))
result = len(list(filter(lambda x: x == '3', str_number)))
print(result)

#4.
str_number = sum(1 for i in str(number) if int(i) == 3)

#5.
number1 = number
count = 0
while number1 > 0:
    if number1 % 10 == 3:
        count += 1
    number1 //= 10
print(count)

#6.
dict1 = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
str_number = str(number)
for i in str_number:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)
print(dict1['3'])

dict1 = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for i in str_number:
    dict1[i] = dict1.get(i,0) + 1
print(dict1)
print(dict1['3'])