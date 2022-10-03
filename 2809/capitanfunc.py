"""function which writes answer into file."""
import datetime

# Окрываем файл из которого читаем строки
with open('input.txt', 'r') as fileinput:
    # Сохраняем строки в список
    strings = fileinput.readlines()


def captain(thedate: str):
    """
    Function gets strings from input.txt and writes answer into the answer_capitan.txt.

    Args:
        thedate: str - input date 'day.month.year'
    """
    # Разделяем дату, месяц, год
    dat = [int(num) for num in thedate.split('.')]
    # Открываем файл для записи
    with open('answer_capitan.txt', 'w') as fileoutput:
        # Обходим строки нумирируя их
        for numline, _ in enumerate(strings):
            # Записываем в строку дату, с каждой строки новая, на один день больше
            ans = '{0}'.format(str(datetime.date(dat[2], dat[1], dat[0]) + datetime.timedelta(days=numline)))
            # Записываем строку
            ans += ': {0}'.format(strings[numline])
            # Записываем строки
            fileoutput.write(ans)
    with open('answer_capitan.txt', 'r') as fileout:
        return fileout.readlines()
