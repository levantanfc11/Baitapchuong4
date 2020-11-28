import random
n = random.randrange(50,1000)
A = []
for i in range(n):
    rd_str = ''
    for i in range(6):
        rd_str = rd_str + random.choice('abcdefghijklmnopqrstuvwxyz')
        A.append({'name':rd_str.capitalize(), 'age': random.randint(1, 100)})
print(A)
