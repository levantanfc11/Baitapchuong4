import os 
tenthumuc = input("nhập tên thư mục cần tạo:")
tenteptin = input("nhập tên tệp tin cần tạo:")
os.mkdir(tenthumuc)
tenteptin = os.path.join(os.getcwd(),tenthumuc,tenteptin)
os.mkdir(tenteptin)