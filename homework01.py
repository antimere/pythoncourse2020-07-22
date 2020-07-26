# задание1

a = 123
b = 456
c = 789
d = 0
print("Операнты a и b - ", a, b, c, d)
string1 = input("Введите первую строчку ")
number1 = int(input("Введите 1-ое число "))
string2 = input("Введите вторую строчку ")
number2 = int(input("Введите 2-ое число "))
print("Введеные значения - %1s %2d %1s %2d" % (string1, number1, string2, number2))

# задание2

time = int(input("Введите Ваше время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в часах, минутах и секундах:) чч:мм:сс   {hours} : {minutes} : {seconds}")

# задание3

n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)

# задание5

profit = float(input("Введите выручку Вашей компании "))
money: float = float(input("Введите издержки Вашей компании "))
if profit > money:
    print(f"Компания работает с прибылью. Рентабельность выручки = {profit / money:.2f}")
    workers = int(input("Введите количество сотрудников Вашей компании "))
    print(f'Прибыль в расчете на 1-го сторудника составляет {profit / workers:.2f}')
elif profit == money:
    print("Ваша компания работает в ноль")
else:
    print("Ваша компания работает в убыток")

# задание6

a = int(input("Привет! Введи результаты пробежки 1-го дня дня в км "))
b = int(input("Отлично! Теперь введи общий желаемый результат в км "))
want_days = 1
want_km = a
while want_km < b:
        a = a + 0.1 * a
        want_days += 1
        want_km = want_km + a
print(f'Спасибо! Ты достигнешь желаемого результата на %.d день' % want_days)