from re import X
import functions
import time
import climage
from functions import *
from image import DrawImage


def stageHell1():
    stageHell = True



    while stageHell:
            functions.typeSys(f"""
Warmth is flowing into your body again. 
You open your eyes. The area is crimson red and fire seems to be burning eternally. 
Everything you see is engulfed in flames, it could be a thousand degrees in here. 
The stench of burning body’s and sulphur is rushing into your nose. 
I need to find a way out of here. 
You decide to wander around and look for hints to escape this place.\n\n""", 0.001)
            functions.clearConsoleEnt()

            functions.typeSys(f"""
It is unbearable to properly walk around, due to the temperature.
I should look for something, which can help me against the heat.\n\n""", 0.001)
            functions.clearConsoleEnt()

            options = [0, 0 ,0, 0, 0]
            optionsC = [0, 0 ,0, 0, 0]
            environmentHell = True
            while environmentHell:
                functions.typeSys(f"""You look around, and see\n\n""", 0.001)
                y = functions.chooseSys("sussy chest", "a corpse", "skeleton", "large door", "surroundings")
                if y == "sussy chest":
                    functions.clearConsole()
                    print(f"""
Sussy chest
──────────────────""")
                    options[0] += 1
                    if options[0] > 1:
                        functions.typeSys("Bruh you already chose this dumbass\n\n")
                        functions.clearConsoleEnt()
                    else:
                        functions.typeSys(f"""\n
You attempt to inspect the sussy chest, the chest starts to smile and show it's teeth when you get closer.
It's too late to jump out of the way, you get bitten by the chest. Just like Darksouls.\n\n""", 0.001)
                        functions.typeSys("You lost 1 \033[91mhp\033[0m\n\n")
                        functions.hitpoints -= 1
                        functions.typeSys(f"current \033[91mhp\033[0m: {functions.hitpoints}\n\n")
                        functions.clearConsoleEnt()
                elif y == "Back":
                    functions.clearConsole()
                    functions.typeSys("\n\nYou can't go back here.\n\n")
                    functions.clearConsoleEnt()
                elif y == "skeleton":
                    functions.clearConsole()
                    print(f"""
Funny skeleton!!
──────────────────""")
                    functions.typeSys("What do skelletons order at restaurants?\n\n")
                    functions.typeSys("...\n\n", 0.5)
                    functions.typeSys("Spare ribs\n\n")
                    image = DrawImage.from_file("images/skeleton.jpg", (30, 15))
                    image.draw_image()
                    functions.clearConsoleEnt()

                elif y == "large door":
                    functions.clearConsole()
                    print(f"""
Large door
──────────────────""")
                    if functions.playerStats[0] == 0:
                        functions.typeSys("It's too hot to touch\n\n")
                        functions.hints += 1
                        functions.clearConsoleEnt()
                        if functions.hints > 1:
                            print("\ntip: Because you're retarded we are giving a hint. Look in your inventory for something against the heat\n")
                            print("It's too hot to touch\n\n")
                            functions.clearConsoleEnt()
                    elif functions.playerStats[0] == 1:
                            functions.clearConsole()
                            print("\033[91mRed's throne room\033[0m")
                            functions.typeSys(f"""
You get blinded by the light. Your eyes and body get used to the ambience of the room.
You open the large door and reveal a huge throne room in front of you, it looks like someone has been waiting for you\n\n""", 0.001)
                            functions.clearConsoleEnt()
                            print(f"""
\033[91mRed\033[0m
──────────────────""")
                            functions.typeSys(f"""\n
Welcome back, I've been expecting you. I know you have questions about \033[93mwho killed you\033[0m.
However, I do not have such answers. 
The only thing i know is that White has been sending lots of people here.
Sadly, I do not have time to \033[93mpunish him\033[0m. 
Please go out and find him for me, send him my regards.""")
                            functions.typeSys("\033[93m\n\nA magical door opens in front of you\033[0m\n\n")
                            functions.typeSys("You enter the door and it disappears behind you.\n\n")
                            functions.clearConsoleEnt()
                            environmentHell = False
                            stageHell = False
                            break

                elif y == "a corpse":
                    clearConsole()
                    functions.typeSys(f"""\n
The corpse is hanging from the ceiling, it looks like an old man. 
It reminds you of your dad, which went to the market to get milk 10 years ago... 
You look if there is anything to salvage, from his belongings: \n\n""", 0.001)
                    functions.clearConsoleEnt()
                    corpse = True
                    while corpse:
                        functions.typeSys("Choose a item to inspect or pickup: \n")
                        y1 = functions.chooseSys("jar of milk", "adoption papers", "car keys", "picture of your mom", "Corpse")
                        if y1 == "jar of milk":
                            functions.clearConsole()
                            optionsC[0] += 1
                            if optionsC[0] > 1:
                                functions.typeSys("You already picked this item up, bitch.\n\n")
                                functions.clearConsoleEnt()
                            else: 
                                functions.gameInventory.append("jar of milk")
                                functions.typeSys(f"""\n\033[93mYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n\033[0m""", 0.01)
                                functions.clearConsoleEnt()
                        elif y1 == "adoption papers":
                            functions.clearConsole()
                            optionsC[1] += 1
                            if optionsC[1] > 1:
                                functions.typeSys("You already picked this item up, bitch.\n\n")
                                functions.clearConsoleEnt()
                            else:
                                functions.gameInventory.append("adoption papers")
                                functions.typeSys(f"""\n\033[93mYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n\033[0m""", 0.01)
                                functions.clearConsoleEnt()
                        elif y1 == "car keys":
                            functions.clearConsole()
                            optionsC[2] += 1
                            if optionsC[2] > 1:
                                functions.typeSys("You already picked this item up, bitch.\n\n")
                                functions.clearConsoleEnt()
                            else:
                                functions.gameInventory.append("car keys")
                                functions.typeSys(f"""\n\033[93mYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n\033[0m""", 0.01)
                                functions.clearConsoleEnt()
                        elif y1 == "picture of your mom":
                            functions.clearConsole()
                            optionsC[3] += 1
                            if optionsC[3] > 1:
                                functions.typeSys("You already picked this item up, bitch.\n\n")
                                functions.clearConsoleEnt()
                            else:
                                functions.gameInventory.append("picture of your mom")
                                functions.typeSys(f"""\n\033[93mYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(y1)]}\n\n\n\033[0m""", 0.01)
                                functions.clearConsoleEnt()
                        elif y1 == "Menu":
                            functions.menu("Inventory", "Status effects", "Map")
                        elif y1 == "Back":
                            print("")
                            functions.clearConsoleEnt()
                            break
                        else:
                            functions.clearConsole()
                            functions.typeSys("\nNot a valid option\n\n")
                            functions.clearConsoleEnt()
                            
                elif y == "Menu":
                    functions.menu("Inventory", "Status effects", "Map")