def check_ticket():
    # 获取用户输入的身高
    height = int(input("你的身高是多少："))

    if height > 120:
        print("身高超出限制，不可以免费")
        print("但是，如果vip级别大于3，可以免费")

        # 获取用户输入的vip级别
        vip_level = int(input("你的vip级别是多少："))

        if vip_level > 3:
            print("恭喜你，vip级别达标，可以免费")
        else:
            print("Sorry 你需要买票10元")
    else:
        print("欢迎小朋友，免费游玩。")


check_ticket()

