#Viết chương trình lặp giải phương trình bậc nhất n lần với các tham số nhập vào từ bàn phím
#vòng lặp while
i = 1 
n = int(input("Nhập n ="))
a = int(input("Nhập a ="))
b = int(input("Nhập b ="))
while i <= n :
    if a==0:
        if b==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm là :",(-b/a))
    i=i+1
#vòng lặp for
for i in range(n):
    if a==0:
        if b==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm là:",(-b/a))
    i = i + 1
print("Kết thúc chương trình")
    