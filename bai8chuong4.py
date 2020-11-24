import os
import time
check = input("Ban co muon tat may tinh cua ban khong ? (y/n) :")

if(check == "y"):
    os.system('shutdown /s /t 1')
else: 
    time.sleep(30)
    check = input("Ban co muon tat may tinh cua ban khong ? (y/n) :")


