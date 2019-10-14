# Guess teh number
import simplegui
import random
import math

count = 0
secret_num = 0

def new_game():
    global count, secret_num
    count = 7
    print "New game. Range is from 0, 100"
    print "Number of remaining guesses is " + str(count) + "\n"

# define event handlers for control panel
def range100():
    new_game()
    global count, secret_num
    count = math.ceil(math.log(100, 2))
    secret_num = random.randrange(0, 100)
    
def range1000():
    global count, secret_num
    count = math.ceil(math.log(1000, 2))
    secret_num = random.randrange(0, 1000)
    count = int(count)
    secret_num = int(secret_num)
    print "New game. Range is from 0, 1000"
    print "Number of remaining choices is " + str(count) + "\n"
    
def input_guess(guess):
    global count, secret_num
    guess = int(guess)
    
    secret_num = int(secret_num)
    count = int(count)
    print "Guess was " + str(guess)
    
    count = count - 1
    
    if count == 0:        
        print "Number of remaining guesses is 0"
        if guess == secret_num:
            print "Correct!!"
        else:
            print "You ran out of guesses. The Secret Number was " + str(secret_num) + "\n"
           
        new_game()
    else:
        if guess > secret_num:
            print "Number of remaining guesses is " + str(count)
            print "Lower!" + "\n"
           
        elif guess < secret_num:
            print "you have " + str(count) + " choices"
            print "Higher!!" + "\n"
            
        elif guess == secret_num:
            print "Number of remaining guesses is " + str(count)
            print "Correct!!" + "\n"
            print
            count = 0
            new_game()
            
frame = simplegui.create_frame("Guess num", 400, 400)
frame.add_button("Range is [0, 100)", range100, 100)
frame.add_button("Range is [0, 1000)", range1000, 100)
frame.add_input("Enter the value", input_guess, 100)
frame.start()

new_game()

#Thank you!