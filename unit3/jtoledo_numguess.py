import random
#computer picks a number
correct_number = random.randint(1,100)
# print(correct_number)
user_guess = 200
guesses = 0

while user_guess != correct_number:
    #computer ask player what number did they choose (repeat)
    user_guess = int(input("pick a number between 1 and 100: "))
    guesses = guesses + 1
    #if the player chooses a number greater than the correct number then the computer would tell the player to pick a lower number (repeat)
    if user_guess > correct_number:
        print("pick a lower number")
    #if the player chooses a number less than the correct number then the computer would tell the player to pick a higher number (repeat)
    if user_guess < correct_number:
        print("pick a higher number")
    # if the player chooses the correct number then the computer will tell the player that the player got it correct and the game ends (repeat)
    if user_guess == correct_number:
        print("you won!")
        print("you have guessed {} times".format(guesses))


