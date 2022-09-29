import functions
import time
from functions import *

def main():
    mainscreen = True
    stageHell = False
    hitpoints = 3
    hints = 0
    while mainscreen:
        functions.playSound("music/minecraftmusic.mp3", 1)
        functions.clearConsole()
        functions.intro()
        break
    stageHell = True

    while stageHell:
        functions.typeSys(f"""Warmth is flowing into your body again. 
You open your eyes. Everything you see is engulfed in flames.
It is crimson red and fire seems to be burning eternally. 
It could be a thousand degrees in here. 
Suddenly the stench of burning body’s and sulphur is rushing into your nose. 
I need to find a way out of here. 
You decide to wander around and look for hints to escape this place.\n\n""", 0.001)
        input("Press enter to continue...")

        functions.clearConsole()

        functions.typeSys(f"""It is almost unbearable to walk around properly, due to the temperature.
I should look for something, which can help me against the heat.\n\n""", 0.001)
        input("Press enter to continue...")
        functions.clearConsole()

        functions.typeSys(f"""You look around, and see\n\n""", 0.001)
        options = [0, 0 ,0, 0, 0]
        optionsC = [0, 0 ,0, 0, 0]
        environmentHell = True
        while environmentHell:
            y = functions.chooseSys("sussy chest", "a corpse", "mix tapes", "large door")
            if y == "sussy chest":
                options[0] += 1
                if options[0] > 1:
                    functions.typeSys("Bruh you already chose this dumbass")
                    functions.clearConsoleEnt()
                else:
                    functions.typeSys(f"""You attempt to inspect the sussy chest, the chest starts to smile and show its teeth when you get closer.
Its too late to jump out of the way, you get bitten by the chest. Just like Darksouls.""", 0.001)
                    functions.typeSys("You lost 1 hp")
                    hitpoints -= 1
                    functions.typeSys(f"Your current hp is {hitpoints} hp")
                    functions.clearConsoleEnt()
            elif y == "Back":
                functions.typeSys("You can't go back here.")
                functions.clearConsoleEnt()
            elif y == "mix tapes":
                functions.typeSys("We open this and play a mix tape earrape?, after this you lose 1 hp?")
                functions.clearConsoleEnt()
            elif y == "large door":
                if functions.playerStats[0] == 0:
                    functions.typeSys("Its too hot to touch\n")
                    hints += 1
                    print(hints)
                    if hints > 1:
                        print("\ntip: Because you're retarded we are giving a hint. Look in your inventory for something against the heat\n")
                        print("Its too hot to touch")
                        functions.clearConsoleEnt()
                elif functions.playerStats[0] == 1:
                    while True:
                        functions.typeSys(f"""You get blinded by the light. Your eyes and body get used to the ambience of the room.
You open the large door and reveal a huge throne room in front of you, it looks like someone has been waiting for you""", 0.001)


                        functions.clearConsoleEnt()

                        
            elif y == "a corpse":
                functions.typeSys(f"""The corpse is hanging from the ceiling, it looks like an old man. 
It reminds you of your dad, which went to the market to get milk 10 years ago... 
You look if there is anything to salvage, from his belongings: \n\n""", 0.001)
                corpse = True
                while corpse:
                    functions.typeSys("Choose a item to inspect or pickup: \n")
                    print("─" * 65)
                    y1 = functions.chooseSys("jar of milk", "adoption papers", "car keys", "picture of your mom", "Menu", "Back")
                    if y1 == "jar of milk":
                        optionsC[0] += 1
                        if optionsC[0] > 1:
                            functions.typeSys("You already picked this item up jar of milk.")
                            functions.clearConsoleEnt()
                        else: 
                            functions.gameInventory.append("jar of milk")
                            functions.typeSys(f"""You have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "adoption papers":
                        optionsC[1] += 1
                        if optionsC[1] > 1:
                            functions.typeSys("You already picked this item up.")
                            functions.clearConsoleEnt()
                        else:
                            functions.gameInventory.append("adoption papers")
                            functions.typeSys(f"""You have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "car keys":
                        optionsC[2] += 1
                        if optionsC[2] > 1:
                            functions.typeSys("You already picked this item up.")
                            functions.clearConsoleEnt()
                        else:
                            functions.gameInventory.append("car keys")
                            functions.typeSys(f"""You have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "picture of your mom":
                        optionsC[3] += 1
                        if optionsC[3] > 1:
                            functions.typeSys("You already picked this item up.")
                            functions.clearConsoleEnt()
                        else:
                            functions.gameInventory.append("picture of your mom")
                            functions.typeSys(f"""You have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "Menu":
                            functions.menu("Inventory", "Map")
                    elif y1 == "Back":
                        break
                    else:
                        functions.typeSys("Not a valid option")
                        
            elif y == "Menu":
                    functions.menu("Inventory", "Map")
                
                            
                            # if y2 == "Inventory":
                            #     functions.typeSys(functions.gameInventory)
                            # elif y2 == "Map":
                            #     functions.typeSys(f"You haven't found a map yet")
                            # else:
                            #     functions.typeSys("Break")


        

        # y = functions.chooseSys("Egel", "bom", "bom", "checkInventory", "map", "quit")
        # if y == "Egel":
        #     userChoose = "Egel"
        #     gameInventory.append(userChoose)
        #     functions.typeSys(
        #         f"""\nYou have obtained a Item {gameInventory[gameInventory.index(userChoose)]}""", 0.01)
        # elif y == "checkInventory":
        #     functions.typeSys(gameInventory)
        # elif y == "map":
        #     functions.gameMap(0)
        # elif y == "quit":
        #     functions.typeSys("quit game")
        #     break
        # else:
        #     functions.typeSys("Bruh stupid?")


main()

