my_list = [25, False, [3, 4], "Gosh", 7.2]

def my_type(i):
    for i in range(len(my_list)):
        print(type(my_list[i]))
    return

my_type(my_list)



#-----------------------------------------------------------------------------------------


num = int(input("Введите количество элементов: "))
my_list = []
i = 0
elem = 0
while i < num:
    my_list.append(input("Введите следующее значение списка: "))
    i += 1

for i_elem in range(int(len(my_list)/2)):
    my_list[elem], my_list[elem + 1] = my_list[elem + 1], my_list[elem]
    elem += 2
print(my_list)



#----------------------------------------------------------------------------------------------


month = int(input("Введите порядковый номер месяца: "))

year = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for season, months in year.items():
    if month in months:
        print(season)



#------------------------------------------------------------------------------------------


my_str = input("Введите строку: ")
my_word = []
i = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {i} {my_word [el]}")
        i += 1
    else:
        print(f" {i} {my_word [el] [0:10]}")
        i += 1



#--------------------------------------------------------------------------------------


my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг: {my_list}")
digit = int(input("Введите число: "))
while digit >= 0:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
            break
    print(f"Текущий рейтинг: {my_list}")
    digit = int(input("Введите число: "))