import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    j = input("1 = Rock\n2 = Paper\n3 = Scissors\n = Enter a number from 1-3: ")
    if j == "1":
        return 'r'
    elif j == "2":
        return 'p'
    elif j == "3":  
        return 's'
#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == "1":
        return "r"
    elif comp_move == "2":
        return "p"
    else:
        return "s"

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    number_of_rounds = input("How many rounds would you like to play?")    
    return int(number_of_rounds)

def get_round_winner(p1move, cmove):
    if p1move == 'r' and cmove == 's':
        return "player"
    elif p1move == 'p' and cmove == 'r':
      return "player"
    elif p1move == 's' and cmove == 'p': 
      return "player"
    elif p1move == 's' and cmove == 'r':
      return "computer"
    elif p1move == 'r' and cmove == 'p':
      return "computer"
    elif p1move == 'p' and cmove == 's':
      return "computer"
    elif p1move == 's' and cmove == 's':
      return "tie"
    elif p1move == 'p' and cmove == 'p':
      return "tie"
    elif p1move == "r" and cmove == 'r':
      return "tie"
    
def get_full_move(shortmove):
    if shortmove == 'r':
        return "Rock"
    if shortmove == 'p':
        return "Paper"
    if shortmove == 's':
        return "Scissors"
        

#function name: print_score
def print_score(pscore, cscore, ties):
    print("you have to {} points \n the computer has {} points \n you guys are tied {} times:". format(pscore,cscore,ties))
    
    
    


#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    rounds = get_rounds()
    p1move = get_p1_move()
    compmove = get_comp_move() 
    winner= get_round_winner(p1move,compmove)
    print("you chose {}".format(p1move))
    print("the computer chose {}".format(compmove))
    if winner == "player":
         print("player won !")
    elif winner == "computer":
        print("computer won !")
    else:
        print("It's a tie !")


rps()