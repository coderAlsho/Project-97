import random

number = random.randint(1, 9)

chances = 0
print("guess a number between 1-10")
while chances < 5:
        guessNumber = int(input('enter a number between 1-9: '))

        if(guessNumber == number):
            print('lets go, you win mate')
            break
        elif(guessNumber < number):
            print("i am sorry but that was a bit to low, guess a little higher", guessNumber)
        else:
            print("this time, that guess was a bit to high, try again", guessNumber)

        chances=chances+1
        if not chances > 5:
            print("I am sorry but you lose",number)





