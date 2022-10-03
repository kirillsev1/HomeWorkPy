import datetime
def captain(dat, string):
    dat = [int(i) for i in dat.split('.')]
    ans = ''
    for i in range(len(string)):
        ans += str(datetime.date(dat[2], dat[1], dat[0]) + datetime.timedelta(days=i))
        ans += ':' + string[i] + '\n'
    return ans

with open('answer_capitan', 'w') as file:
    file.write(captain(input('Введите дату "день.месяц.год":'), ['завтра 2 января 2033 год, меня наконец то отчислят', 'меня снова не отчислили', 'новый день, до попытки отчисления осталось 364 дня']))
