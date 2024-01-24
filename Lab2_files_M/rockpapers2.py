from random import randint

count_c = 0
count_u = 0
while (True):
    #Generate the computer's move using the randint function 
    #in the random module.
    #Assume 0 = rock, 1 = paper, and 2 = scissors.
    computerMove = randint(0,2)

    #Prompt the user to enter r for rock, p for paper or s for scissors.
    #Save the user's input in a variable called userMove.

    userMove = input(("Please enter r, p or s for move,x to exit:"))
  

    #Number of times user and computer wins

    #Validate the user's move.
    if (userMove =='r' or userMove == 'p' or userMove == 's'):
        if computerMove == 0 and userMove == "r": 
            print ("Computer is rock. You are rock. It is a tie")
            #Write the if-elif statements to determine outcome of the game.
        elif computerMove == 0 and userMove == "p":
            print ("Computer is rock. You are paper. You win")
            count_u += 1
        elif computerMove == 0 and userMove == "s":
            print ("Computer is rock. You are scissor. Computer wins")
            count_c += 1


        elif computerMove == 1 and userMove == "r": 
            print ("Computer is paper. You are rock. Computer wins")
            count_c += 1
        elif computerMove == 1 and userMove == "p":
            print ("Computer is paper. You are paper. It is a tie")
        elif computerMove == 1 and userMove == "s":
            print ("Computer is paper. You are scissor. You win")
            count_u += 1

        elif computerMove == 2 and userMove == "r": 
            print ("Computer is scissor. You are rock. You win")
            count_u += 1
        elif computerMove == 2 and userMove == "p":
            print ("Computer is scissor. You are paper. Computer wins")
            count_c += 1
        elif computerMove == 2 and userMove == "s":
            print ("Computer is scissor. You are scissor. It is a tie")

    else:
        print(count_c,"wins by computer\n",
              count_u,"wins by user")
    if userMove == "x":
        break
