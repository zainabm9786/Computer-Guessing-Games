#the computer will guess the number and you have to tell whethers its too low, high or correct
import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low!=high:
            guess = int(random.randint(low,high))
        else:
            guess= low #could also be high b/c low==high
        feedback= input(f'Is {guess} to high (H), too low (L) or correct (C)? ')
        if feedback == 'h':
            high=guess-1
        elif feedback =='l':
            low=guess+1
    
    print(f'Yay! The computer guessed your number, {guess}, correctly! ')

computer_guess(10)