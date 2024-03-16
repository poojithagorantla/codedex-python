import random
magic8ball = random.randint (1,9)

if magic8ball == 1:
    answer = "yes -definetly"
elif magic8ball ==2:
    answer = "It is decidedly so"
elif magic8ball == 3:
    answer ="Without a doubt"
elif magic8ball == 4:
    answer ="Reply hazy, try again"
elif magic8ball == 5:
    answer = "Ask again later"
elif magic8ball == 6:
    answer = "Better not tell you now"
elif magic8ball == 7:
    answer = "My sources say no"
elif magic8ball == 8:
    answer= "outlook not so good"
elif magic8ball ==9:
    answer ="very doubtful"
else:
    answer = "error"

Question = input ("Question :")
print("Magic 8 Ball:" + answer)






