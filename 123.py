username = "sjt"
password = "111"
n = 0
while n < 3:
    username1 = input("Username=")
    password1 = input("Password=")
    if username1 == username and password1 == password:
        print("welcome back，", username,"!")
        break
    else:
        print("Login again")
    n=n+1
else:
    print("登录失败")
