#Первый способ

podstr = input('Введите подстроку:')
str1 = input('Введите строку:')
ans = []
if podstr in str1:
    for i in range(len(str1)+1-len(podstr)):
            forTestPodStr = [str1[j] for j in range(i, i+len(podstr))]
            test = ''
            for h in forTestPodStr:
                 test += h
            if podstr == test:
                print(i)
                break
else:
    print(-1)
'''
#Второй способ
podstr = input('введите подстроку:')
str1 = input('Введите строку:')
print(str1.index(podstr))
#3-й способ
podstr = input()
str1 = input()
if podstr in str1:
    list1 = str1.split(podstr)
    print(len(list1[0]))
else:
    print(-1)
'''

# def find_substring(string, sub):
#     sub_l = len(sub)
#     for i in range(len(string) - sub_l):
#         if string[i:i+sub_l] == sub:
#             return i
#     return -1
# print(find_substring('asdfghjasdfghj', 'j'))
