
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin =0

question1 = int(input("Do you like Dawn or Dusk: 1)Dawn 2)Dusk"))
if question1 == 1:
    gryffindor += 1 
    ravenclaw += 1
elif question1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")

question2 = int(input("When i'm dead, i want people to remember me as: 1)The good 2)The Great 3)The wise 4) The Bold "))
if question2 == 1:
    hufflepuff += 2
elif question2 == 2:
    slytherin += 2
elif question2 == 3:
    ravenclaw += 2
elif question2 == 4:
    gryffindor += 2
else:
    print("Wrong input")

question3 = int(input("Which kind of instrument most pleases your ear: 1)The violin 2)The trumpet 3) The piano 4)The drum"))
if question3 == 1:
    slytherin += 4
elif question3 == 2:
    hufflepuff += 4
elif question3 ==3:
    ravenclaw +=4
elif question3 == 4:
    gryffindor +=4
else:
    print("Wrong input")

if gryffindor > hufflepuff and gryffindor> ravenclaw and gryffindor > slytherin:
    print ("You are in Gryffindor")
elif hufflepuff > gryffindor and hufflepuff >ravenclaw and hufflepuff> slytherin:
    print ("You are in Hufflepuff")
elif ravenclaw > gryffindor and ravenclaw > slytherin and ravenclaw > hufflepuff:
    print (" You are in Ravenclaw")
else:
    print ("you are in slytherin")

