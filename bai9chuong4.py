import smtplib
username=input("username:")
password=input("password:")
sendusername=input("email nhan:")
n=int(input("so lan gui n="))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
msg = input("thong diep:")
i=1
while i<=n:
    server.sendmail(username ,sendusername, msg)
    i+=1
server.quit()