import random
import math

a = int(input("Enter Lower Limit "))
b = int(input("Enter Upper Limit "))
c = int(input(f'Guess a number between {a} and {b} '))
d = random.randrange(a,(b + 1))
i = 1
tries = 6
while i in range(6):
    if c != d:
        print(f'{c} was not correct. You have {tries} more tries.\n')
        tries -= 1
        if c > d:
            print("The number was lower \n")
        if c < d:
            print("The number was higher \n")
        c = int(input("Please Guess Again \n "))
    
        if c == d:
            print(f'Congratulations you guessed the number {d} correctly \n')

else:
    print("Sorry you were not able to correctly guess the number in 7 tries. Please try again. /n")