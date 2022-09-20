def ceck():
    try:
        day = int(input('Введите день:'))
        month = int(input('Введите месяц:'))
        year = int(input('Введите год:'))
    except ValueError:
        return False
    if month >= 1 and month <= 12:
        calendar = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
        if year % 400 == 0 and year % 100 == 0 or year % 4 == 0 and year % 100 != 0:
            calendar[1] = 29
        return day >= 1 and day <= calendar[month - 1]
    else:
        return False
print(ceck())
