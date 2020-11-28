import random
A = {}
rd_str = ''
for i in range(6):
    rd_str = rd_str + random.choice('abcdefghijklmnopqrstuvwxyz')
A['name'] = rd_str.capitalize()
A['age'] = random.randrange(1, 120)
print(A)