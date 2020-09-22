#-------------------------------------------1-------------------------------------------

my_f = open("test.txt", 'w', encoding="utf-8")
line = input("Введите текст \n")
while line:
    my_f.writelines(line)
    line = input("Введите текст \n")
    if not line:
        break

my_f.close()
my_f = open("test.txt", "r", encoding="utf-8")
content = my_f.readlines()
print(content)
my_f.close()


#----------------------------------------2-----------------------------------------------


my_file = open("test.txt", "r", encoding="utf-8")
content = my_file.read()
print(f"Содержимое файла: \n {content}")
my_file = open("test.txt", "r", encoding="utf-8")
content = my_file.readlines()
print(f"Количество строк в файле - {len(content)}")
my_file = open("test.txt", "r", encoding="utf-8")
content = my_file.readlines()
for i in range(len(content)):
    print(f"Количество символов {i + 1}-ой строки: {len(content[i])}")
my_file = open("test.txt", "r", encoding="utf-8")
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

#-------------------------------------------3--------------------------------------------

with open('text_3.txt', 'r', encoding="utf-8") as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')


#-----------------------------------------4----------------------------------------------


rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("text_4.txt", "r", encoding="utf-8") as file_obj:
    for i in file_obj:
        i = i.split(" ", 1)
        new_file.append(rus[i[0]] + "  " + i[1])
    print(new_file)

with open("text_4_new.txt", "w", encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(new_file)


#-------------------------------------------5-------------------------------------------


def summary():
    try:
        with open("text_5.txt", "w+", encoding="utf-8") as file_obj:
            line = input("Введите цифры через пробел \n")
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Ошибка ввода")
summary()


#---------------------------------------------6------------------------------------------


subj = {}
with open("text_6.txt", "r", encoding="utf-8") as init_f:
    for line in init_f:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or (i >= "0" and i <= "9")]).split()))
        subj[name] = name_sum
    print(f"{subj}")



#-------------------------------------------------7------------------------------------------------------



import json

result = []
with open("text_77.json", "w", encoding="utf-8") as write_f:
    with open("text_7.txt", encoding="utf-8") as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(" ")[0]] = int(line.split(" ")[2]) - int(line.split(" ")[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({"average_profit": round(average_profit)})
    json.dump(result, write_f)
