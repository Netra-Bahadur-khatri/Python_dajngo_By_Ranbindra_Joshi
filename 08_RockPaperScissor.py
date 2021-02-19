# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def rock_paper_scissor():

    x = input("Enter rock or paper or scissor: \t")
    y = input("Enter rock or paper or scissor: \t")

    if x == "rock" and y == "scissor":
        print("{} wins".format(x)) #netra wins here also
    elif x == "rock" and y == "paper":
        print("{} wins".format(y)) #yagya wins here
    elif x == "paper " and y == "scissor":
        print("{} wins".format(y)) #yagya wins here
    elif x == "paper  " and y == "rock":
        print("{} wins".format(x)) #netra wins here also
    elif x == "scissor" and y == "paper":
        print("{} wins ".format(x)) #netra wins here also
    elif x == "scissor" and y == "rock":
        print("{} wins".format(y)) #yagya wins here
    elif x == y:
        print("Game is tie.")
    else:
        print("Nothing is happens in the rock, paper scissor game.")

if __name__ == "__main__":
    c = rock_paper_scissor()
    print(c)




