str1 = input()
lsstr = str1.split()
ans = 0
de = len(lsstr)
for i in lsstr:
    low = 0
    high = 0
    for j in i:
        if j.isupper():
            low += 1
        else:
            high += 1
    if high > low:
        ans += 1
print('{0}%'.format(100 - (100//(de // ans))))
