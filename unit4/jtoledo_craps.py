import random
bank_amount = 100


def rules(bank_amount):
    if bank_amount < 0:
        return "You have nothing!"
    elif bank_amount > 0:
        return input(int(" How much would you like to bet?"))



def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum

roll2dice()

 


#   function name: update_bank
#   purpose: change bank amount based on wheather the player won or not
#   argument: none 








