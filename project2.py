# You have to write a program which generates a random number and asks the user to guess it.
# - If the player's guess is higher than the actual number, the program displays:
# "Lower number please"
# - If the player's guess is lower than the actual number, the program displays:
# "Higher number please"
# - When the user guesses the correct number, the program displays:
# "You guessed it in X attempts"
# (where X is the number of guesses the user took)
# Hint: Use the random module.


import random
n= random.randint(1,100)
a=-1
guesses = 0
while a!=n: 
    a=int(input("Guess the number: "))
    if a>n:
        print("lower number please")
        guesses +=1
    elif a<n:
        print("higher number please")
        guesses +=1
print(f"You guessed it in", guesses, "attempts")
