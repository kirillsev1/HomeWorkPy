"""Finding percent of letters in string."""


def findingpercent(string: str) -> str:
    """
    Makes up a string task. Find numbers of low and uppers letters.

    Args:
        string: str - first string.

    Returns:
        str: str - made up the task in percents.
    """
    ans = 0
    # Берем подстроку из строки
    for line in string.split():
        # Объявляем меременные подсчета
        low = 0
        high = 0
        # Смотрим на букву
        for letter in line:
            # Проверяем букву
            if letter.isupper():
                high += 1
            else:
                low += 1
        # Добавляем к делителю 1
        if high > low:
            ans += 1
    # Возвращаем ответ
    return '{0}%'.format(100 // (len(string.split()) // ans))
