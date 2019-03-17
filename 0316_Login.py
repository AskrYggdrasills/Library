# 用户信息
username = "sjt"
password = "111"
n = 0


while n < 3:
    in_username = input("Username=")
    in_password = input("Password=")
    if in_username == username and in_password == password:
        print("welcome back，", username,"!")
        break
    else:
        print("Login Failed")
    n=n+1
else:
    print("Please Login Later")