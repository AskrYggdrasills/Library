print ('猜一个在1到100之间的数')
import random
num = random.randint(1,100)
n = 0
while n < 5:
    guess = int(input("请蒙一个数字数字:"))
    if guess == num:
        print('猜对了')
        break
    elif guess < num:
        print ('小了')
    else:
        print ('大了')
    n = n+1
else:
    print ('再猜一次')