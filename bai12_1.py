import  random
n=random.randrange(50,1000)
print(n)
#sotunhien=list()
#for i in range(n):
    #sotunhien.append(input('nhap phan tu'))
#print(sotunhien)
print('Hết câu 1')
sotunhien2=list()
for i in range(n):
    sotunhien2.append(random.randrange(-1000,1000))
print(sotunhien2)
print('Hết câu 2')
sotunhien2=list()
for i in range(n):
    sotunhien2.append(random.triangular(-1000.0,1000.0))
print(sotunhien2)
print('Hết câu 3')