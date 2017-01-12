import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice1 = random.randint(1,6)
    # generate another random number from 1 to 6
    dice2 = random.randint(1,6)
    # get the sum of the two rolls
    dice_sum = dice1 + dice2
    # print the sum
    print("Rolled {} and {}, total: {}".format(dice1, dice2, dice_sum))
    # return the sum
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
   
    # if player's bet is more than they have
    #   available in bank, then get new bet
   
    # if player's bet is valid, then return
    #   the bet
 
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    # if the sum is over 7, return "over7"
    if dice_sum > 7:
   
    # if the sum is under 7, return "under7"
   elif dice_sum < 7:
       return "under7"
    # if the sum is 7, return "equal7"
 else:
        return "equal7"
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
    print("choose from the following")
    print("1. over 7 /n2. under 7 \n3. equal to 7")
   
    # return their choice
 return input("choose_range")
# function for the main game
def overunder7():
    bank = 100 
    while bank > 0:
        bet = get_bet(bank):
        user_range = choose_range()
        dice = roll2dice()
        round_range = get_range(dice)
        if user_range == round_range: #user won
        print("you win!")
        if user_range == "equal7":
            bank = bank + 4 * bet
            else:
                bank = bank + bet
                
                else: #user lost 
                print("you lost")
                bank = bank - bet
                
                #print new bank value
                print("your balance is ${}".format(bank))
                
                #ask if they want to do another round
                new_round = input("do you want to contuniue? [y|n]").lower()
                if new_round != "y":
            break
        
        print("Game over, you have ${} in your bank".format(bank))
        
        overunder7()
        
            
            
        