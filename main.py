print("Welcome")

print("You have three trials to guess a number")

#We import the random module
import random

#We assign a random number to a variable
guess=random.randrange(1,10)

#We assign a boolean value to a variable to help us in looping
test=True

#We assign a incremental value to count th number of guesses made
guesses=1

#We use two parameters to help us in looping
while test and guesses<=3:
    num=int(input("Guess a number between 1 and 10:  "))
    if guess==num:
        print("Excellent, Your answer is",guess)
        test=False
    else:
        print("Wrong guess try again")
        guesses=guesses+1
#We print out to the player that the trials are over
if(guesses>3):
    print("You have exhausted your three trials. Your answer was",guess)

