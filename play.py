from random import randint

import main

def play():
    while True:
        main.cycles += 1
        prizeDoor = randint(0,99)
        firstGuess = randint(0,99)
        eliminateDoor = randint(0,65)
    
        #Determine the prize door:
        if prizeDoor <= 32:
            print("The prize is behind door 1.")
            prizeDoor = 1
        elif prizeDoor > 32 and prizeDoor <= 65:
            print("The prize is behind door 2.")
            prizeDoor = 2
        elif prizeDoor > 65:
            print("The prize is behind door 3.")
            prizeDoor = 3

        #Determine the Initial guess door:
        if firstGuess <= 32:
            print("I guessed door 1.")
            firstGuess = 1
        elif firstGuess > 32 and firstGuess <= 65:
            print("I guessed door 2.")
            firstGuess = 2
        elif firstGuess > 65:
            print("I guessed door 3.")
            firstGuess = 3

        #Eliminiate a non-prize, non-guess door:
        if firstGuess == 1 and prizeDoor == 1:
            if eliminateDoor <= 32:
                eliminateDoor = 2
                print("Door 2 was eliminated!")
            elif eliminateDoor > 32:
                eliminateDoor = 3
                print("Door 3 was eliminated!")
        elif firstGuess == 1 and prizeDoor == 2:
            eliminateDoor = 3
            print("Door 3 was eliminated!")
        elif firstGuess == 1 and prizeDoor == 3:
            eliminateDoor = 2
            print("Door 2 was eliminated!")
        elif firstGuess == 2 and prizeDoor == 2:
            if eliminateDoor <= 32:
                eliminateDoor = 1
                print("Door 1 was eliminated!")
            elif eliminateDoor > 32:
                eliminateDoor = 3
                print("Door 3 was eliminated!")
        elif firstGuess == 2 and prizeDoor == 1:
            eliminateDoor = 3
            print("Door 3 was eliminated!")
        elif firstGuess == 2 and prizeDoor == 3:
            eliminateDoor = 1
            print("Door 1 was eliminated!")
        elif firstGuess == 3 and prizeDoor == 3:
            if eliminateDoor <= 32:
                eliminateDoor = 1
                print("Door 1 was eliminated!")
            elif eliminateDoor > 32:
                eliminateDoor = 2
                print("Door 2 was eliminated!")
        elif firstGuess == 3 and prizeDoor == 2:
            eliminateDoor = 1
            print("Door 1 was eliminated!")
        elif firstGuess == 3 and prizeDoor == 1:
            eliminateDoor = 2
            print("Door 2 was eliminated!")

        #Switch the guess or not:
        if main.switch == "n":
            finalGuess = firstGuess
            print("I didn't switch!")
        elif main.switch == "y":
            if firstGuess == 1 and eliminateDoor == 2:
                finalGuess = 3
                print("I switched to door 3!")
            elif firstGuess == 1 and eliminateDoor == 3:
                finalGuess = 2
                print("I switched to door 2!")
            elif firstGuess == 2 and eliminateDoor == 1:
                finalGuess = 3
                print("I switched to door 3!")
            elif firstGuess == 2 and eliminateDoor == 3:
                finalGuess = 1
                print("I switched to door 1!")
            elif firstGuess == 3 and eliminateDoor == 1:
                finalGuess = 2
                print("I switched to door 2!")
            elif firstGuess == 3 and eliminateDoor == 2:
                finalGuess = 1
                print("I switched to door 1!")
            
        #Determine and print win or loss:
        if finalGuess == prizeDoor:
            print("I won!")
            main.wins += 1   
        else:
            print("I lost...")
            main.losses += 1