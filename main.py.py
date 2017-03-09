#The Camel game by Pvrpl

# -*- coding: utf-8 -*-

import random
print("You just stole a camel! You have a few options.") 
# 你偷了一只骆驼！你现在有几个选项
print("A. Drink from your Canteen.") 
# 从你的水壶喝水
print("B. Ahead moderate speed.") 
# 中速前进
print("C. Ahead full speed.") 
# 全速前进
print("D. Stop for the night.") 
# 停下来休息一晚
print("E. Status Check.") 
# 检查状态
print("Q. Quit.") 
# 离开游戏


done = False
miles = 0 # Distance traveled in miles.               行进的总距离
now_miles = 0 # The distance traveled at this moment. 此次行进的距离
tiredness = 0 # The camel's tiredness.                骆驼的疲惫值
thirst = 0 # Thirst level.                            缺水程度
nativemiles = 20 # Distance of natives.               当地人的距离

canteen = 3 # Three drinks in the canteen.            水壶的3份水

def game():
    global done
    global miles # Distance traveled in miles.               行进的距离
    global now_miles # The Distance traveled at this moment. 此次行进的距离
    global tiredness # The camel's tiredness.                骆驼的疲惫值
    global thirst # Thirst level.                            缺水程度
    global nativemiles # Distance of natives.                当地人的距离
    global canteen # Three drinks in the canteen.            水壶的水

    user_choice = input("What would you like to do?") # 你想做什么？
    if nativemiles <= 0:
        done = True
    elif thirst >= 5:
        done = True
    elif miles >= 100:
        done = True
    while not done:
        if user_choice == "Q" or  user_choice == "q":
                print("You are now done with the game! Goodbye!") 
                # 你离开了游戏! Goodbye!
                done = True
        elif user_choice == "E" or user_choice == "e":
                print("You've traveled", miles,"miles") 
                # 你走过了多少英里
                print("You have", canteen, "drinks in your canteen left and have a thirst value of", thirst) 
                # 你有几份份水在你的水壶里，缺水程度为多少
                print("The natives are", nativemiles, "miles behind.") 
                # 当地人距离你多少英里
                done = False
        elif user_choice == "D" or user_choice == "d":
            print("You rest and gain your energy back. Your camel is happy!")
            # 你通过休息恢复了你的体力，你的骆驼看起来很高兴！
            tiredness = 0
            nativemiles = nativemiles - random.randrange(0,8)
            done = False
        elif user_choice == "C" or user_choice == "c":
            print("You chose to move on full speed ahead.")
            # 你选择全速前进
            now_miles = random.randrange(9,21)
            miles = miles + now_miles
            tiredness = tiredness + random.randrange(0,4)
            thirst = thirst + 2
            nativemiles = nativemiles - random.randrange(7,14) + now_miles
            done = False
        elif user_choice == "B" or user_choice == "b":
            print("You chose to move on at moderate speed.")
            # 你选择以中等速度前进
            now_miles = random.randrange(4,13)
            miles = miles + now_miles
            tiredness = tiredness + 1
            thirst = thirst + 1
            nativemiles = nativemiles - random.randrange(7,14) + now_miles
            done = False
        elif user_choice == "A" or user_choice == "a":
            print("You chose to take a drink")
            # 你选择喝一杯水
            if canteen <= 0:
                print("You don't have any drinks left!")
                # 你已经没有水了!
                done = False
            else:
                canteen = canteen - 1
                thirst = 0
                done = False
        else:
            print("You input an incorrect option! Try again!")
            # 您输入的选项不正确！再试一次！
            return
        break
while not done:
        if nativemiles <= 0:
            done = True
            print("You are caught, waiting for your will be a tragic fate!")
            # 你被抓住了，等待你的将会是悲惨的命运！
        elif thirst >= 5:
            done = True
            print("You have a long time did not drink water, and began to feel that they slowly lose consciousness...")
            # 你已经好长时间没有喝过水了，开始感觉自己慢慢失去意识...
        elif miles >= 100:
            done = True
            print("You have fled,the locals have been unable to find you!")
            # 你已经逃的够远了，那些当地人再也找不到你了！
        else:
            game()