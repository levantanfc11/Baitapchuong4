import random
n =int(input("Nhập n="))
list1=[]
for i in range(n):
    a=random.random()
    list1.append(a)
print(list1)
max=list1[0]
for i in range(n):
    if max<list1[i]:
        max=list1[i]
print("Giá trị lớn nhất là:",max)
print("Chương trình kết thúc")

