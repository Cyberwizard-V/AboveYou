from re import X
import functions
import time
from functions import *
from image import DrawImage

#\033[0m ending quote for color
def stageLake():
    stageLake = True

    while stageLake:
                print("\033[96mStage Lake\033[0m")
                functions.typeSys(f"""
The sun is shining bright, its been a while since you've seen the outside world.
The atmosphere feels pleasant, you breath in some fresh air. 
It smells exactly like that smell when it starts to rain.
Wait, what am I doing. I should go find white\n\n""", 0.001)
                functions.clearConsoleEnt()

                functions.typeSys(f"""
You hear the birds whistle and you feel the wind blowing around you. 
Suddenly you hear someone in distress at the lakeside. 
You are curious and walk towards the sound...\n\n""", 0.001)
                functions.clearConsoleEnt()

                options = [0, 0 ,0, 0, 0]
                optionsC = [0, 0 ,0, 0, 0]
                environmentLake = True
                while environmentLake:
                    functions.typeSys(f"""You look around, and see\n\n""", 0.001)
                    y = functions.chooseSys("talking fish", "garry", "lake", "grass", "Lakeside")    #fish needs water, doesnt say anything unless you find a aquarium somewhere at lake area (abandoned ship), person 2 says please find a fish bowl for fish
                    if y == "talking fish":                                                          #selecting a npc will show the npc name on top and talk., if you talk you can select multiple conversation types
                        functions.clearConsoleEnt()
                        print(f"""
Talking fish
──────────────────""")
                        xfishbowl = "fishbowl"
                        xDivinggear = "diving suit"
                        xmystNote = "mysterious note"
                        if xfishbowl in gameInventory:
                            functions.typeSys("""Thank you for saving me, I was almost out of breath.

It's dangerous to go alone! Take this. """)
                            functions.gameInventory.append("diving suit")
                            print(f'''\n\n\033[93mYou've received the item "diving suit" \033[0m\n\n''')
                            functions.gameInventory.remove("fishbowl")
                            functions.clearConsoleEnt()
                        elif xDivinggear in gameInventory:
                            image = DrawImage.from_file("images/fishl.png", (50, 10))
                            image.draw_image()
                            functions.typeSys("happy fish sounds\n\n")
                            functions.clearConsoleEnt()
                        else:
                            image = DrawImage.from_file("images/fish.png", (50, 10))
                            image.draw_image()
                            functions.typeSys("dying fish sounds\n\n")
                            functions.clearConsoleEnt()
                    elif y == "Back":
                        functions.clearConsole()
                        functions.typeSys("\n\nYou can't go back here.\n\n")
                        functions.clearConsoleEnt()
                    elif y == "garry":
                        xDivinggear = "diving suit"
                        functions.clearConsole()
                        print(f"""
Garry
──────────────────""")
                        if xDivinggear in gameInventory and xmystNote in gameInventory:
                            image = DrawImage.from_file("images/garry.png", (40, 20))
                            image.draw_image()
                            functions.typeSys("""\n
Thank you for drowning my fish!
Blue always told me to read notes.
            \n\n""")
                            functions.clearConsoleEnt() 
                        elif xmystNote in gameInventory:
                            image = DrawImage.from_file("images/garry.png", (40, 20))
                            image.draw_image()
                            functions.typeSys("\nMy fish doesnt work, please find a working fish bowl.\n\n")
                            functions.clearConsoleEnt() 

                        else:
                            image = DrawImage.from_file("images/garry.png", (40, 20))
                            image.draw_image()
                            functions.typeSys("\nmeow!\n\n")
                            functions.gameInventory.append("mysterious note")
                            print(f'''\n\n\033[93mYou've received a "mysterious note" \033[0m\n\n''')
                            functions.clearConsoleEnt() 

                    elif y == "grass":
                        functions.clearConsole()
                        print(f"""
Grass
──────────────────""")
                        options[0] += 1
                        if options[0] > 1:
                            functions.typeSys("Bruh you already unlocked the touching grass achievement, stupid\n\n")
                            functions.clearConsoleEnt()
                        else:
                            functions.typeSys("\nYou touched some grass.\n\n")
                            functions.typeSys("You regained 1 \033[92mhp\033[0m\n\n")
                            functions.hitpoints += 1
                            functions.typeSys(f"current \033[92mhp\033[0m: {functions.hitpoints}\n\n")
                            functions.clearConsoleEnt()


                    elif y == "lake":
                        functions.clearConsole()
                        functions.typeSys(f"""\n
You walk towards the lake, \n\n""", 0.001)
                        functions.clearConsoleEnt()
                        lake = True
                        while lake:
                            functions.typeSys("You are looking around and see... : \n")
                            y1 = functions.chooseSys("abandoned ship", "sand", "sign", "water", "Lake")
                            if y1 == "abandoned ship":
                                functions.clearConsole()
                                functions.typeSys(f"""\n
You walk towards the spooky scarry abandoned ship.
Upon walking closer to the ship a deteriorated name becomes clearer.
It says: The Titanic.\n\n""", 0.001)
                                functions.clearConsoleEnt()
                                while True:
                                    y2 = functions.tinyChooseSys("fishbowl", "skeleton","Abandoned Titanic")
                                    if y2 == "fishbowl":
                                        functions.clearConsole()
                                        optionsC[0] += 1
                                        if optionsC[0] > 1:
                                            functions.typeSys("You already picked this item up, bitch.\n\n")
                                            functions.clearConsoleEnt()
                                        else: 
                                            functions.gameInventory.append("fishbowl")
                                            functions.typeSys(f"""\n\033[93mYou have obtained a Item {functions.gameInventory[functions.gameInventory.index("fishbowl")]}\033[0m\n\n""", 0.01)
                                            functions.clearConsoleEnt()
                                    elif y2 == "skeleton":
                                        functions.clearConsole()
                                        print(f"""
Funny skeleton...
──────────────────""")
                                        functions.typeSys("Why did the skeleton go to the party alone?...\n\n")
                                        functions.typeSys("Because he had no body to go with him!!\n\n")
                                        image = DrawImage.from_file("images/skeleton.jpg", (30,15))
                                        image.draw_image()
                                        functions.clearConsoleEnt()
                                    elif y2 == "Me":
                                        functions.menu("Inventory", "Status effects", "Map")
                                    elif y2 == "Back":
                                        functions.clearConsoleEnt()
                                        break
                                    else:
                                        functions.clearConsole()
                                        functions.typeSys("\nNot a valid option\n\n")
                                        functions.clearConsoleEnt()
                                            
                            elif y1 == "sand":
                                functions.clearConsole()
                                print(f"""
Quick sand
──────────────────""")
                                optionsC[1] += 1
                                if optionsC[1] > 1:
                                    functions.typeSys("Don't try that anymore, jesus.\n\n")
                                    functions.clearConsoleEnt()
                                else:
                                    functions.typeSys(f"""\n
You see sand and walk over it... you slowly start sinking... 
after struggling for an hour you finally manage to get out\n\n""", 0.001)
                                    functions.typeSys("You lost 1 \033[91mhp\033[0m\n\n")
                                    functions.hitpoints -= 1
                                    functions.typeSys(f"current \033[91mhp\033[0m: {functions.hitpoints}\n\n")
                                    functions.clearConsoleEnt()
                            elif y1 == "sign":
                                functions.clearConsole()
                                print(f"""
Sign
──────────────────────
North-
Titanic
            East-
            Blue's cave
South-
Lakeside   

Red was here
──────────────────────
 """)
                                
                                functions.clearConsoleEnt()
                            elif y1 == "water":
                                functions.clearConsole()
                                print(f"""
Water
──────────────────""")
                                optionsC[3] += 1
                                xDivinggear = "diving suit"
                                if xDivinggear in gameInventory:
                                    functions.clearConsole()
                                    functions.typeSys("A sign is warning you not to enter without directions")
                                    warning = input("Would you still like to proceed to enter the dangerous waters? (Y/N) ").lower()
                                    if warning == "n":
                                        functions.clearConsole()
                                        continue
                
                                    if warning == "y":
                                        functions.typeSys("""\n
You dive in the water with your diving gear.
Every corner seems to be the same down here.
I should look for a way out!\n\n""")
                                        
                                        functions.clearConsoleEnt()
                                        exploring1 = True

                                        while exploring1:
                                            functions.clearConsole()
                                            functions.typeSys("Try to find a way out... \n")                                #player needs to go right up left if talk to garry after diving suit he tells a hint
                                            e1 = functions.chooseMaze("up", "left", "right", "down", "Random waters")
                                            if e1 == "up":
                                                functions.clearConsole()
                                                print("It looks like a dead end\n\n")
                                                functions.clearConsoleEnt()
                                            elif e1 == "down":
                                                functions.clearConsole()
                                                print("It looks like a dead end\n\n")
                                                functions.clearConsoleEnt()
                                            elif e1 == "left":
                                                functions.clearConsole()
                                                print("It looks like a dead end\n\n")
                                                functions.clearConsoleEnt()


                                            elif e1 == "right":
                                                exploring2 = True
                                                while exploring2:
                                                    functions.clearConsole()
                                                    e2 = functions.chooseMaze("up", "left", "right", "down", "Random waters?")
                                                    if e2 =="left":
                                                        functions.clearConsole()
                                                        break
                                                        
                                                    elif e2 == "right":
                                                        functions.clearConsole()
                                                        print("It looks like a dead end\n\n")
                                                        functions.clearConsoleEnt()
                                                    elif e2 == "down":
                                                        functions.clearConsole()
                                                        print("It looks like a dead end\n\n")
                                                        functions.clearConsoleEnt()

                                                    elif e2 == "up":
                                                        exploring3 = True
                                                        while exploring3:
                                                            functions.clearConsole()
                                                            e3 = functions.chooseMaze("up", "left", "right", "down", "Random waters!")

                                                            if e3 == "down":
                                                                functions.clearConsole()
                                                                break
                                                            elif e3 == "left":
                                                                functions.clearConsole()
                                                                e3 = functions.chooseSys("pineapple", "blob fish", "rock", "blue's cave", "Familiar waters")
                                    else:
                                        functions.clearConsole()
                                        print("That's not even a choice bruh")
                                        functions.clearConsoleEnt()


                                else:
                                    functions.typeSys("\nA sign is warning you not to enter without directions.\n\nIt looks wet\n\n")    #maybe switch case different print function
                                functions.clearConsoleEnt()
                            elif y1 == "Me":
                                functions.menu("Inventory", "Status effects", "Map")
                            elif y1 == "Back":
                                functions.clearConsoleEnt()
                                break
                            else:
                                functions.clearConsole()
                                functions.typeSys("\nNot a valid option\n\n")
                                functions.clearConsoleEnt()
                                
                    elif y == "Me":
                        functions.menu("Inventory", "Status effects", "Map")

