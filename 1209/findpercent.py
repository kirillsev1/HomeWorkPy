"""Finding percent of letters in string."""


def findingpercent(string: str) -> str:
    """
    Makes up a string task. Find numbers of low and uppers letters.

    Args:
        string: first string.

    Returns:
        str - made up the task in perc cents.
    """
    ans = 0
    for line in string.split():
        low = 0
        high = 0
        for letter in line:
            if letter.isupper():
                high += 1
            else:
                low += 1
        if high > low:
            ans += 1
    return '{0}%'.format(100 // (len(string.split()) // ans))
