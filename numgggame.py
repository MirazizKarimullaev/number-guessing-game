import random
import time
def guess_number():
    minimum = int(input("what is the min of the number you want to guess? "))
    maximum = int(input("what is the max? "))
    number = random.randint(minimum,maximum)
    rrange = maximum - minimum
    correct = False
    guesses = 0
    guess_list = []
    while correct == False:
        print("what is your guess?")
        guess = int(input())
        guesses +=1
        guess_list.append(guess)
        if guess == number:
            print("You got it :D")
            if guesses > 1:
                print(f"You made {guesses} guesses in the order {guess_list}")
            elif guesses == 1 and rrange > 24:
                print(f"Dang, one guess? that's crazy lucky you guessed {guess}")
            correct = True
        elif maximum >= guess >= number:
            print("sorry but the number is lower")
            time.sleep(.5)
        elif minimum <= guess <= number:
            print("sorry but the number is higher")
            time.sleep(.5)
        else:
            print("not in curent range")
            time.sleep(.5)
guess_number()
