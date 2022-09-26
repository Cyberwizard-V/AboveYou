import functions
import time

def main():
    mainscreen = True
    gamestart = False
    gameInventory = []
    while mainscreen:
        functions.playSound("music/minecraftmusic.wav", 1)
        functions.clearConsole()
        functions.intro()
        time.sleep(2)
        break
    gamestart = True

    while gamestart:
        y = functions.chooseSys("Egel", "bom", "bom", "checkitems")
        if y == "Egel":
            userChoose = "Egel"
            gameInventory.append(userChoose)
            functions.typeSys(f"""\nYou have obtained a Item {gameInventory[gameInventory.index(userChoose)]}""", 0.01)
        elif y == "checkitems":
            print(gameInventory)
        else:
            print("Bruh stupid?")
            break




main()

#print(functions.chooseSys("Egel", "bom", "bom", "checkitems"))

