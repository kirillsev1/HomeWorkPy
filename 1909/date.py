def ceck():
    day = int(input('Введите день:'))
    month = int(input('Введите месяц:'))
    year = int(input('Введите год:'))
    calendar = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    if year % 100 == 0:
        pass
    elif year % 4 == 0:
        calendar.insert(1, 29)
        del calendar[3]
    if day >= 1 and day <= calendar[month - 1]:
        return True
    else:
        return False
print(ceck())