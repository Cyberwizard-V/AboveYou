import functions
import time

def main():
    mainscreen = False
    gamestart = True
    gameInventory = []

    while mainscreen:
        #functions.playSound("music/minecraftmusic.mp3", 1)
        functions.clearConsole()
        functions.intro()
        time.sleep(5)
        break
    gamestart = True

    while gamestart:
        y = functions.chooseSys("Egel", "bom", "bom", "checkitems", "quit")
        if y == "Egel":
            userChoose = "Egel"
            gameInventory.append(userChoose)
            functions.typeSys(f"""\nYou have obtained a Item {gameInventory[gameInventory.index(userChoose)]}""", 0.01)
        elif y == "checkitems":
            print(gameInventory)
        elif y == "quit":
            print("quit game")
            break
        else:
            print("Bruh stupid?")
        
main()

#test
#Je bent super dik

#test
