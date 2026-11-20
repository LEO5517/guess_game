import random

print("【测试】这行代码只在分支里存在")

print("欢迎来到猜数字游戏!")

# 生成一个1⃣1到100之间的随机数
secret_number = random.randint(1,100)
guess = 0

print("我已经想好了一个1到100之间的数字，你猜是多少?")

while guess != secret_number:
    try:
        guess = int(input("请输入你的猜测："))
        if guess < secret_number:
            print("猜小了，再大一点！")
        elif guess > secret_number:
            print("猜大了，再小一点！")
    except ValueError:
        print("请输入一个有效的整数哦！")
print(f"恭喜你猜对了！答案就是{secret_number}。")