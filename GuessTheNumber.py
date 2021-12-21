from random import *
bot=randint(1,100)
s=0
print(bot)
print('Lets play a game. Bot has just thought of a number between 1 and 100. You will have 10 attempts to guess.')
print("You can only type a number. Bot will tell you, if your number is higher or lower than the given. Good luck!")

for i in range(10):
    N=int(input("Type your number "))
    if N==bot:
        print("Wow! You've won! It was your attempt №",i)
        s=1
        break
    elif N<bot:
        print("Lower")
    else:
        print("higher")
if s==0:
    print("You didn't win. That's a shame")
