# number guessing 
# set up numbers or colors
# generate numbers  or colors
# guess code
# check code  
# game function

import random 
color_to_guess = ['R', 'G', 'B', 'Y', 'P', 'V']
tries = 3
code_length = 4

def generate_code():
    code = []
    for i in range(code_length):
        colors = random.choice(color_to_guess)
        code.append(colors)
    return code


def guess_code():
    # Ask for the code
    # Check the len of the code
    # compare the code guessed
    while True:
        guess = input("Guess Code for an award: ") 
    
        if len(guess) != code_length:
            print(f"You must guess {code_length} colors")
            continue

        for i in guess:
            if i not in color_to_guess:
                print(f"Invalid color: {i}. Try again.")
                break
        else:
            break
        return guess
                

g = guess_code()
print(g)