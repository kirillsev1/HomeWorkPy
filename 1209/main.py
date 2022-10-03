"""main file for function findingpercent."""
from findpercent import findingpercent

if __name__ == '__main__':
    string = str(input())
    answer = str(findingpercent(string, string.split()))
    print(answer)
