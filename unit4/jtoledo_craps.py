import random

def beginning_bank():
    return 100


def rules(bank_amount):
    if bank_amount < 0:
        return "You have nothing!"
    elif bank_amount > 0:
        return input(int(" How much would you like to bet?"))



def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {} so you got {}".format(dice1,dice2,dice_sum))
    return dice_sum

def get_bet(bank_amount):
    bet = int(input("How much would you like to bet?"))
    while True: 
        if bet < 0:
             print ("There's no negative numbers allowed!")
        elif bet <= bank_amount:
            return bet
        elif bet > 100:
            print("You don't have the money!")

def first_roll(player_sum,point_roll):
    if player_sum == 2 or 3 or 12:
        return "player loses"
    elif player_sum == 7 or 11:
        return "player win"



#   function name: update_bank
#   purpose: change bank amount based on wheather the player won or not
#   argument: none 
def craps():
    int(input("how much would you like to bet: "))
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum

    while bank_amount > 0:
        bet = get_bet(bank_amount)
        rol12dice = get_roll2dice()
        dice_sum = roll2dice
        
        if bank_amount < 0:
            return "You have nothing!"
        elif bank_amount > 0:
            return input(int(" How much would you like to bet?")) 

craps()


    







