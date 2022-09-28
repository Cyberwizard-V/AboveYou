import functions
import time

def main():
    mainscreen = False
    stageHell = True
    gameInventory = []
    hitpoints = 3

    while mainscreen:
        #functions.playSound("music/minecraftmusic.mp3", 1)
        functions.clearConsole()
        functions.intro()
        time.sleep(5)
        break
    stageHell = True

    while stageHell:
#         functions.typeSys(f"""Warmth is flowing into your body again. 
# You open your eyes. Everything you see is engulfed in flames.
# It is crimson red and fire seems to be burning eternally. 
# It could be a thousand degrees in here. 
# Suddenly the stench of burning body’s and sulphur is rushing into your nose. 
# I need to find a way out of here. 
# You decide to wander around and look for hints to escape this place.""", 0.001)
#         time.sleep(1)
#         functions.clearConsole()

        functions.typeSys(f"""It is almost unbearable to walk around properly, due to the temperature.
I should look for something, which can help me against the heat.""", 0.001)
        time.sleep(0)
        functions.clearConsole()

        functions.typeSys(f"""You look around, and see\n""", 0.001)
        
        options = [0, 0 ,0, 0, 0]

        while True:
            y = functions.chooseSys("suspicious chest", "a corpse", "lost soul", "mix tapes", "a wall", "Main")
            if y == "suspicious chest":
                options[0] += 1
                if options[0] > 1:
                    print("Bruh you already chose this dumbass")
                else:
                    
                    functions.typeSys(f"""You attempt to inspect the suspicious chest, the chest starts to smile and show its teeth when you get closer.
Its too late to jump out of the way, you get bitten by the chest. Just like Darksouls.""", 0.001)
                    print("You lost 1 hp")
                    hitpoints -= 1
                    print(f"Your current hp is {hitpoints} hp")
            elif y == "a corpse":
                functions.typeSys(f"""The corpse is hanging from the ceiling, it looks like an old man. 
It reminds you of your dad, which went to the market to get milk 10 years ago... 
You look if there is anything to salvage, from his belongings: \n""", 0.001)

                optionsC = [0,0,0,0]
                time.sleep(1)
                while True:
                    functions.clearConsole()
                    print("Choose a item to inspect or pickup:")
                    print("#"* 100)
                    y1 = functions.chooseSys("jar of milk", "addoption papers", "car keys", "picture of your mom", "Intestines")
                    if y1 == "jar of milk":
                        optionsC[0] += 1
                        if optionsC[0] > 1:
                            print("You already picked this item up.")
                        else: 
                            gameInventory.append("jar of milk")
                            functions.typeSys(f"""You have obtained a Item {gameInventory[gameInventory.index(y1)]}\n""", 0.01)
                    if y1 == "addoption papers":
                        optionsC[1] += 1
                        if optionsC[1] > 1:
                            print("You already picked this item up.")
                        gameInventory.append("addoption papers")
                        functions.typeSys(f"""You have obtained a Item {gameInventory[gameInventory.index(y1)]}\n""", 0.01)
                    if y1 == "car keys":
                        optionsC[2] += 1
                        if optionsC[2] > 1:
                            print("You already picked this item up.")
                        gameInventory.append("car keys")
                        functions.typeSys(f"""You have obtained a Item {gameInventory[gameInventory.index(y1)]}\n""", 0.01)
                    if y1 == "picture of your mom":
                        optionsC[3] += 1
                        if optionsC[3] > 1:
                            print("You already picked this item up.")
                        gameInventory.append("picture of your mom")
                        functions.typeSys(f"""You have obtained a Item {gameInventory[gameInventory.index(y1)]}\n""", 0.01)
                    if y1 == "Intestines":
                        optionsC[4] += 1
                        if optionsC[4] > 1:
                            print("AGAIN, nothing to find here.")
                        else: 
                            print("Nothing to find here...")
            elif y == "map":
                functions.gameMap(0)
            elif y == "quit":
                print("quit game") 
                break
            else:
                print("Bruh stupid?")
        

        # y = functions.chooseSys("Egel", "bom", "bom", "checkInventory", "map", "quit")
        # if y == "Egel":
        #     userChoose = "Egel"
        #     gameInventory.append(userChoose)
        #     functions.typeSys(
        #         f"""\nYou have obtained a Item {gameInventory[gameInventory.index(userChoose)]}""", 0.01)
        # elif y == "checkInventory":
        #     print(gameInventory)
        # elif y == "map":
        #     functions.gameMap(0)
        # elif y == "quit":
        #     print("quit game")
        #     break
        # else:
        #     print("Bruh stupid?")


main()

