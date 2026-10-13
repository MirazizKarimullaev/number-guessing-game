import random
def guess_number():
    minimum = int(input("what is the min of the number you want to guess? "))
    maximum = int(input("what is the max? "))
    number = random.randint(minimum,maximum)
    correct = False
    while correct == False:
        print("what is your guess?")
        guess = int(input())
        if guess == number:
            print("You got it :D")
            correct = True
        elif maximum >= guess >= number:
            print("sorry but the number is lower")
        elif minimum <= guess <= number:
            print("sorry but the number is higher")
        else:
            print("not in curent range")
guess_number()
