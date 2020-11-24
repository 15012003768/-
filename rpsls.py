#目标：完成RPSLS游戏
#作者：杨培象import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print ("Error:No Correct Name")

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print ("Error-number_to_name")

    # convert number to a name using if/elif/else
    # don't forget to return the result!


import random

def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    print ("===============================")
    print ("Player chooses",player_choice)
    play_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print ("Computer chooses",comp_choice)

    n = (play_number - comp_number) % 5

    if n==1 or n==2:
        print ("Player wins!")
    elif n==3 or n==4:
        print ("Computer wins!")
    elif n==0:
        print ("Draw")
    else:
        print ("Error")

    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()

    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

# always remember to check your completed program against the grading rubric
print("欢迎使用RPSLS游戏")
print("-----------------")
print("请输入你的选择")
chioce_name=input()
rpsls(chioce_name)