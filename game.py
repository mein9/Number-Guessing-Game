import random
import math

lower_limit = int(input("Enter Lower Limit "))
upper_limit = int(input("Enter Upper Limit "))

max_tries = int(math.log(upper_limit - lower_limit + 1, 2))
rand_num = random.randrange(lower_limit,(upper_limit + 1))
i = 0
while i < max_tries:
    user_input = int(input(f'Guess a number between {lower_limit} and {upper_limit}: '))
    i += 1
    if user_input == rand_num:
        print(f'Congratulations! You guessed the number {rand_num} correctly in {i} tries.')
        break
    else:
        print(f'{user_input} was not correct.', end=" ")
        if user_input > rand_num:
            print("The number is lower.")
        else:
            print("The number is higher.")
        

else:
    print(f'Sorry you were not able to correctly guess the number in {i} tries. The correct answer was {rand_num} \n ')
   #FIXME figure out how to make this outline work lol
   #play_again = input("Play again? (y/n)")
    #if (play_again == "y") or (play_again == "Y") :
        #find out how to start code over
   # if (play_again == "n") or (play_again == "N"):
       # print("Goodbye")