import random
import math

def main_program():
    while True:
        try:
            lower_limit = int(input("Enter Lower Limit: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            upper_limit = int(input("Enter Upper Limit: "))
            if upper_limit > lower_limit:
                break
            else:
                print("Upper limit must be greater than the lower limit.")
        except ValueError:
            print("Please enter a valid number.")
        
    max_tries = int(math.log(upper_limit - lower_limit + 1, 2))
    rand_num = random.randrange(lower_limit,(upper_limit + 1))
    i = 0
    while i < max_tries:
        try:
            user_input = int(input(f'Guess a number between {lower_limit} and {upper_limit}: '))
        except ValueError:
            print("Please enter a valid number.")
            continue

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
def main():
    while True:
        main_program()
        play_again = input("Play again? (y/n)").strip().lower()
        if play_again != 'y':
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
   