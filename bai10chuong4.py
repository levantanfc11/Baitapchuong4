#thu vien numpy
import numpy as np
_A = [[6,7,8],
      [8,9,4],
      [5,6,7]]
A = np.array(_A)
print(A)
_B = [[6,4,3],
      [7,8,6],
      [8,6,4]]
B = np.array(_B)
print(B)
print("A + B",A + B)
print("A * B",A * B)
print("ma trận chuyển vị của A là :",A.transpose())
#Matplotlib
#barchar
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
plt.bar(x = ['KHDLAI', 'KTTDH', 'KTD'], height = [45, 20, 10], color = 'red')
plt.xlabel('Biểu đồ chỉ thành viên của mỗi lớp')
plt.ylabel('Thành viên của mỗi lớp')
#line
import matplotlib.pyplot as plt
plt.plot([1,5,10,15,20],[1,7,10,16,17],'bD--')
plt.title('biểu đồ tự nghĩ ra')
#boxplot
import matplotlib.pyplot as plt 
import numpy as np  
np.random.seed(10) 
data = np.random.normal(100, 20, 200) 
fig = plt.figure(figsize =(10, 7)) 
plt.boxplot(data) 
plt.show()
#column
import pandas as pd 
data = {'Name':['Tan', 'Tay', 'Hoang', 'Linh'], 
        'Age':[18, 19, 21, 22], 
        'Address':['Hue', 'Da Nang', 'Hue', 'Da Nang']} 
df = pd.DataFrame(data)
print(df[['Name', 'Age','Address']]) 
#Đọc dữ liệu từ file excel (dạng csv) trên máy tính vào bộ nhớ và in ra 10 dòng đầu tiên
import csv
with open('danhsachlop.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['STT','Ten','Tuoi'])
    writer.writerow(['1', 'Tan','18'])
    writer.writerow(['2', 'Tay','19'])
    writer.writerow(['3','Linh','20'])
    writer.writerow(['4','Hoang','21'])
    writer.writerow(['5','Neymar','28'])
    writer.writerow(['6','Son','27'])
    writer.writerow(['7','Messi','32'])
    writer.writerow(['8','Ronaldo','35'])
    writer.writerow(['9', 'Nhan', '18'])
    writer.writerow(['10', 'Y','19'])  
    
import pandas as pd
result = pd.read_csv('danhsachlop.csv')
print(result)
#Đọc dữ liệu từ file excel (dạng csv) trên mạng Internet vào bộ nhớ và in ra 10 dòng đầu tiên
import pandas as pd
ex1 = pd.read_csv('https://raw.githubusercontent.com/levantanfc11/baitapchuong4/main/danhsachlop.csv')
print(ex1.head(10))
#Đọc dữ liệu từ file có định dạng JSON (tren mạng internet) vào bộ nhớ và in ra 10 dòng đầu tiên
import pandas as pd
ex2 = pd.read_json('https://api.github.com/users/voduytuan/repos')
print(ex2.head(10))
