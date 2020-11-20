import random
n =int(input("Nhập n="))
list1=[]
for i in range(n):
    a=random.random()
    list1.append(a)
print(list1)
min=list1[0]
for i in range(n):
    if min>list1[i]:
        min=list1[i]
print("giá trị nhỏ nhất là:",min)
print("Chương trình kết thúc")