# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    if(name == "rock"):
        return 0
    elif(name == "Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else :
        return none

def number_to_name(number):
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        return none

def rpsls(player_choice): 
    # Player's choice
    print "Player chosses", player_choice
    player_choice_num = name_to_number(player_choice)
    
    #Computer's choice
    computer_choice_num = random.randrange(0,5)
    computer_choice_name = number_to_name(computer_choice_num)
    print "Computer chooses", computer_choice_name
    
    # Difference between the two taken modulo 5
    difference_between_choices = (computer_choice_num - player_choice_num) % 5
    
    # Decide who winner is
    if(difference_between_choices == 0):
        print "Player and computer tie!"
    elif(difference_between_choices <= 2):
        print "Computer wins!"
    else :
        print "Player wins!"
        
    print

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


