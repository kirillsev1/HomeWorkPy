"""Testing date for truth."""


divider = 400
monthlimit = 12


def check(thedate: str) -> bool:
    """
    Function which testing existence of date.

    Args:
        thedate: str - variable which rebuild into day, month, year.

    Returns:
        bool: bool - True or False if date is existence.

    Raise:
        ValueError: An error when we could not get int value.
    """
    # Попытка получить int дня, месяца, года из строки
    try:
        day, month, year = map(int, list(thedate.split('.')))
    except ValueError:
        return False
    # Проверка месяца
    if 1 <= month <= monthlimit:
        # Список с количеством дней, под индексом(номером месяца -1)
        calendar = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
        # Проверка высокосного года
        if year % divider == 0 and year % 100 == 0 or year % 4 == 0 and year % 100 != 0:
            # Замена дня в высокосный день
            calendar[1] = 29
        # Проверка кол-ва дней в месяце
        return 1 <= day <= calendar[month - 1]
    return False
