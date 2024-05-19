import random
import math

lower_limit = int(input("Enter Lower Limit "))
upper_limit = int(input("Enter Upper Limit "))
user_input = int(input(f'Guess a number between {lower_limit} and {upper_limit} '))
rand_num = random.randrange(lower_limit,(upper_limit + 1))
i = 0
while i < math.log(upper_limit - user_input +1, 2):
    i += 1
    if user_input != rand_num:
        print(f'{user_input} was not correct.', end=" ")
        
        if user_input > rand_num:
            print("The number was lower ")
        if user_input < rand_num:
            print("The number was higher ")

        user_input = int(input("Please Guess Again \n "))
    
        if user_input == rand_num:
            print(f'Congratulations you guessed the number {d} correctly in {i} tries ')

if i >= math.log(upper_limit - user_input + 1, 2):
    print(f'Sorry you were not able to correctly guess the number in {i} tries. The correct answer was {d} \n ')
   #play_again = input("Play again? (y/n)")
    #if (play_again == "y") or (play_again == "Y") :
        #find out how to start code over
   # if (play_again == n) or (play_again == "N"):
       # print("Goodbye")