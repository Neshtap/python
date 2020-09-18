#-------------------------------------1---------------------------------------------


from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f"Заработная плата сотрудника  {res}")
except ValueError:
    print("Введите число!")


#-----------------------------------------2-----------------------------------------

my_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f"Исходный список {my_list}")
print(f"Новый список {my_new_list}")


#-------------------------------------------3-----------------------------------------------


print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])


#------------------------------------------------4-------------------------------------------


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)


#-----------------------------------------------5-----------------------------------------------


from functools import reduce

print(f"Сумма {reduce(lambda num1, num2: num1 * num2, [i for i in range(100, 1001) if i % 2 == 0])}")


#-------------------------------------------6--------------------------------------------------


from itertools import count

for el in count(3):
    print(el)
    if el == 10:
        break


from itertools import cycle

my_list = [False, "ABC", 123, "АБВ"]
q = 0
for el in cycle(my_list):
    if q > 20:
        break
    print(el)
    q += 1


#--------------------------------------------7--------------------------------------------

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break