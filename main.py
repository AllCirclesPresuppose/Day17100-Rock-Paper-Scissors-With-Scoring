from getpass import getpass as input

print("Better Rock! Paper! Scissors! Game!")
print("Best of 3!")
print()
print()
playerOneScore = 0
playerTwoScore = 0
while True:
    print("Player 1!")
    playerOne = input("select your move (R, P or S) ")
    print("Player 2!")
    playerTwo = input("select your move (R, P or S) ")

    if playerOne == "R":
        if playerTwo == "R":
            print("Boulders! It's a tie!")
        elif playerTwo == "P":
            print("Player two's paper smothers player one's rock!")
            playerTwoScore += 1
        elif playerTwo == "S":
            print("Player one's rock crushes player two's scissors!")
            playerOneScore += 1
    elif playerOne == "P":
        if playerTwo == "R":
            print("Player one's paper smothers player two's rock!")
            playerOneScore += 1
        elif playerTwo == "P":
            print("Papers everywhere, it's a tie!")
        elif playerTwo == "S":
            print("Player two's scissors slices player one's paper!")
            playerTwoScore += 1
    elif playerOne == "S":
        if playerTwo == "R":
            print("Player two's rock crushes player one's scissors!")
            playerTwoScore += 1
        elif playerTwo == "P":
            print("Player one's scissors slices player two's paper!")
            playerOneScore += 1
        elif playerTwo == "S":
            print("Dice it all, it's a tie!")
    if playerOneScore == 3 or playerTwoScore == 3:
        if playerOneScore > playerTwoScore:
            print("Player one scored " + str(playerOneScore) +
                  " and player two scored " + str(playerTwoScore) +
                  "! Player one wins!")
        else:
            print("Player one scored " + str(playerOneScore) +
                  " and player two scored " + str(playerTwoScore) +
                  "! Player two wins!")
        exit()
    else:
        continue
