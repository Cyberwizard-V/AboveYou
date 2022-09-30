import functions
import time
from functions import *
#\033[93m acitons happening

def main():
    mainscreen = True
    stageHell = False
    hints = 0
    while mainscreen:
        functions.playSound("music/minecraftmusic.mp3", 1)
        functions.clearConsole()
        functions.intro()
        break
    stageHell = True

    while stageHell:
        functions.typeSys(f"""Warmth is flowing into your body again. 
You open your eyes. It is crimson red and fire seems to be burning eternally. 
Everything you see is engulfed in flames, it could be a thousand degrees in here. 
The stench of burning body’s and sulphur is rushing into your nose. 
I need to find a way out of here. 
You decide to wander around and look for hints to escape this place.\n\n""", 0.001)
        functions.clearConsoleEnt()

        functions.typeSys(f"""It is unbearable to properly walk around, due to the temperature.
I should look for something, which can help me against the heat.\n\n""", 0.001)
        functions.clearConsoleEnt()

        options = [0, 0 ,0, 0, 0]
        optionsC = [0, 0 ,0, 0, 0]
        environmentHell = True
        while environmentHell:
            functions.typeSys(f"""You look around, and see\n\n""", 0.001)
            y = functions.chooseSys("sussy chest", "a corpse", "mix tapes", "large door", "surroundings")
            if y == "sussy chest":
                options[0] += 1
                if options[0] > 1:
                    functions.typeSys("Bruh you already chose this dumbass\n\n")
                    functions.clearConsoleEnt()
                else:
                    functions.typeSys(f"""\nYou attempt to inspect the sussy chest, the chest starts to smile and show its teeth when you get closer.
Its too late to jump out of the way, you get bitten by the chest. Just like Darksouls.\n\n""", 0.001)
                    functions.typeSys("You lost 1 \033[91mhp\033[0m\n\n")
                    functions.hitpoints -= 1
                    functions.typeSys(f"current \033[91mhp\033[0m: {functions.hitpoints}\n\n")
                    functions.clearConsoleEnt()
            elif y == "Back":
                functions.clearConsole()
                functions.typeSys("\n\nYou can't go back here.\n\n")
                functions.clearConsoleEnt()
            elif y == "mix tapes":
                functions.typeSys("We open this and play a mix tape earrape?, after this you lose 1 hp?\n\n")
                functions.clearConsoleEnt()
            elif y == "large door":
                if functions.playerStats[0] == 0:
                    functions.typeSys("Its too hot to touch\n")
                    hints += 1
                    if hints > 1:
                        print("\ntip: Because you're retarded we are giving a hint. Look in your inventory for something against the heat\n")
                        print("Its too hot to touch\n\n")
                        functions.clearConsoleEnt()
                elif functions.playerStats[0] == 1:
                        functions.clearConsole()
                        print("\033[91mRed's throne room\033[0m")
                        functions.typeSys(f"""You get blinded by the light. Your eyes and body get used to the ambience of the room.
You open the large door and reveal a huge throne room in front of you, it looks like someone has been waiting for you\n\n""", 0.001)
                        functions.typeSys("\033[91mRed:\033[0m")
                        functions.typeSys(f"""\nWelcome back, I've been expecting you. I know you have questions about \033[93mwho killed you\033[0m.
However, I do not have such answers. 
The only thing i know is that Green has been sending lots of people here.
Sadly, I do not have time to \033[93mpunish him\033[0m. 
Please go out and find him for me, send him my regards.""")
                        functions.typeSys("\033[93m\n\nA magical door opens in front of you\033[0m\n\n")
                        functions.typeSys("You enter the door and it disappears behind you.\n\n")
                        functions.clearConsoleEnt()
                        environmentHell = False
                        stageHell = False
                        break

            elif y == "a corpse":
                functions.typeSys(f"""\nThe corpse is hanging from the ceiling, it looks like an old man. 
It reminds you of your dad, which went to the market to get milk 10 years ago... 
You look if there is anything to salvage, from his belongings: \n\n""", 0.001)
                functions.clearConsoleEnt()
                corpse = True
                while corpse:
                    functions.typeSys("Choose a item to inspect or pickup: \n")
                    print("─" * 65)
                    y1 = functions.chooseSys("jar of milk", "adoption papers", "car keys", "picture of your mom", "Corpse")
                    if y1 == "jar of milk":
                        optionsC[0] += 1
                        if optionsC[0] > 1:
                            functions.typeSys("You already picked this item up, bitch.\n\n")
                            functions.clearConsoleEnt()
                        else: 
                            functions.gameInventory.append("jar of milk")
                            functions.typeSys(f"""\nYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "adoption papers":
                        optionsC[1] += 1
                        if optionsC[1] > 1:
                            functions.typeSys("You already picked this item up, bitch.\n\n")
                            functions.clearConsoleEnt()
                        else:
                            functions.gameInventory.append("adoption papers")
                            functions.typeSys(f"""\nYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "car keys":
                        optionsC[2] += 1
                        if optionsC[2] > 1:
                            functions.typeSys("You already picked this item up, bitch.\n\n")
                            functions.clearConsoleEnt()
                        else:
                            functions.gameInventory.append("car keys")
                            functions.typeSys(f"""\nYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "picture of your mom":
                        optionsC[3] += 1
                        if optionsC[3] > 1:
                            functions.typeSys("You already picked this item up, bitch.\n\n")
                            functions.clearConsoleEnt()
                        else:
                            functions.gameInventory.append("picture of your mom")
                            functions.typeSys(f"""\nYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n\n""", 0.01)
                            functions.clearConsoleEnt()
                    elif y1 == "Me":
                        functions.menu("Inventory", "Status effects", "Map")
                    elif y1 == "Back":
                        functions.clearConsoleEnt()
                        break
                    else:
                        functions.typeSys("Not a valid option")
                        
            elif y == "Me":
                functions.menu("Inventory", "Status effects", "Map")
                
                            
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

