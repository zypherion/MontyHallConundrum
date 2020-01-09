from time import sleep

import main

def results():
    while True:
        #Show Results:
        if main.wins > 0 and main.losses > 0:
            winRate = 100*(main.wins/main.cycles)
            print("Wins:",main.wins, "losses:",main.losses)
            print("I've won %d percent of %d games...\n\n" % (winRate, main.cycles))

        #Wait, then clear the screen:
        sleep(.05)
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')