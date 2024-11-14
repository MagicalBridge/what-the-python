import random


def guess_number_game():
    # 生成一个1到100之间的随机数
    num = random.randint(1, 100)

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字。你有三次机会来猜这个数字。")

    # 第一次猜测
    guess = int(input("请猜一个数字："))
    if guess == num:
        print("恭喜第一次就猜对了呢！")
        return

    # 第二次猜测
    guess = int(input("猜错了，再猜一次："))
    if guess == num:
        print("猜对了！")
        return

    # 第三次猜测
    guess = int(input("猜错了，再猜一次："))
    if guess == num:
        print("恭喜，最后一次机会，你猜对了！")
    else:
        print(f"Sorry，猜错了。正确答案是 {num}。")


guess_number_game()
