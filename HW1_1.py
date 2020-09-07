a = 4
print(a)
age = int(input("Enter your age: "))
print(age)
name = input("Enter your name: ")
print(name)


num = int(input("Enter how many seconds you want to convert: "))
hh = num // 3600
mm = (num % 3600) // 60
ss = num % 60
print(f"{hh:02} : {mm:02} : {ss:02}")


n = input("Enter your number: ")
total = (n + int(n + n) + int(n + n + n))
print(total)


n = int(input("Enter your number: "))
n1 = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > n1:
        n1 = n % 10
    if n > 9:
        continue
    else:
        print(n1)
        break


profit = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила: {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
