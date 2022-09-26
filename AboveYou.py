import functions
import time

def main():
    mainscreen = False
    gamestart = True
    x = []
    while mainscreen:
        functions.clearConsole()
        time.sleep(2)
        functions.intro()
        time.sleep(2)
        break
    gamestart = True
    while gamestart:
        if functions.chooseSys("Egel", "bom", "bom", "bom") == "Egel":
            userChoose = "Egel"
            x.append(userChoose)
            functions.typeSys(f"""You have obtained a Item {x[x.index(userChoose)]}""", 0.01)
        else:
            print("Bruh stupid?")
            break




main()

