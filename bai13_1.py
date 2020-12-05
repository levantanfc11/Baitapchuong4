#Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C và in kết quả ra màn hình
import os
for (root,dirs,files) in os.walk('C:',topdown=True):
    print("Thư mục gốc trong ổ đĩa C:",root)
    print("Thư mục con của thư mục gốc:",dirs)
    print("Các tệp tin từ thư mục gốc và thư mục",files)
    print('--------------------------------')
#Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C và:
for (root,dirs,files) in os.walk('C:', topdown=True):
    list1 = files
    list2 = root  