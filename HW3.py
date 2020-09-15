def my_func(*args):
    try:
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        sum = num_1 / num_2

    except ZeroDivisionError:
        return print("Ошибка! На ноль делить нельзя!")

    return sum


print(my_func())



#------------------------------------------------------------------------------------------------------


def my_func(name, surname, year, city, email, tel):
    print(
        f"имя: {name}; фамилия - {surname}; год рождения - {year}; город проживания - {city}; e-mail - {email}; телефон - {tel}")


my_func(name="Сергей", surname="Нештапов", year="1993", city="Москва", email="mail@mail.ru", tel="8-915-555-44-33")



#-------------------------------------------------------------------------------------------------------


def my_func(arg_1, arg_2, arg_3):
    if arg_1 > arg_3 and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3



print(my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: "))))



#--------------------------------------------------------------------------------------------------------------------------


def my_func(x, y):
    s = x ** y
    return s


print(my_func(int(input("Введите число: ")), int(input("Введите степень: "))))


#-----------------------------------------------------------------------------------------------------------



def my_func():
    sum_res = 0
    ex = False
    while ex == False:
        number = input("Введите числа через пробел (для выхода нажмите q): ").split()

        res = 0
        for el in range(len(number)):
            if number[el] == "q" or number[el] == "Q":
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Текущая сумма: {sum_res}")
    print(f"Окончательная сумма: {sum_res}")


my_func()



#------------------------------------------------------------------------------------


def int_func():
    t = (input("Введите текст: "))
    return t.title()

print(int_func())
