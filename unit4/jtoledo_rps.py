import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    j = input("1 = Rock\n2 = Paper\n3 = Scissors\n = Enter a number from 1-3: ")
    if j == "1":
        return 's'
    elif j == "2":
        return 'r'
    elif j == "3":  
        return 'p'
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
    if p1move == 'r' and compmove == 's':
        return "player"
    elif p1move == 'p' and compmove == 'r':
       return "player"
    elif p1move == 's' and compmove == 'p':
      return "player"
    elif p1move == 's' and compmove == 'r':
      return "computer"
    elif p1move == 'r' and compmove == 'p':
       return "computer"
    elif p1move == 'p' and compmove == 's':
       return "computer"
    elif p1move == 's' and compmove == 's':
       return "tie"
    elif p1move == 'p' and compmove == 'p':
       return "tie"
    elif p1move == "r" and compmove == 'r':
       return "tie"
    
def get_full_move(shortmove):
    if shortmove == 'r':
        return "Rock"
    if shortmove == 'p':
        return "Paper"
    if shortmove == 's':
        return "Scissors"
        

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    #code here

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():    #code here
rounds = get_rounds()
#function name: tests
p1move = get_p1_move()
compmove = get_comp_move()
#               with 'tests' to run this function instead of the game loop
winner= get_round_winner(p1move,compmove)
if winner == "player":
    print("player won !")
elif winner == "comp":
    print("computer won !")
else:
    print("It's a tie !")
def test():
    #code here

rps()