import random
player = 0
computer = 0


print("=====================")
print(" Rock Paper Scissors")
print("=====================")
print("1) ✊ ")
print("2) ✋")
print("3) ✌️")

player = int(input("Select a number between 1 and 3:"))
computer = random.randint(1,3)

if player == 1:
    print ("You chose:✊")
elif player ==2:
    print ("you chose:✋")
elif player ==3:
    print("you chose:✌️")
else:
    print("wring choice")


if computer == 1:
    print ("CPU chose:✊")
elif computer == 2:
    print ("CPU Chose:✋")
else:
    print("CPU chose:✌️")




if player == computer:
    print("tie")
elif (player ==2 and computer == 1) or (player ==3 and computer == 2) or (player == 1 and computer ==3):
    print("The palyer won")
elif (player ==1 and computer == 2) or (player ==2 and computer == 3) or (player == 3 and computer ==1):
    print("The computer won")

