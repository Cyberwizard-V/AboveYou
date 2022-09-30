from re import X
import functions
import time
from functions import *
from image import DrawImage

def stageLake():
    stageLake = True

    while stageLake:
                print("\033[96mStage Lake\033[0m")
                functions.typeSys(f"""
The sun is shining bright, its been a while since you've seen the outside world.
The atmosphere feels pleasant, you breath in some fresh air. 
It smells exactly like that smell when it starts to rain.\n\n""", 0.001)
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
                    y = functions.chooseSys("talking fish", "garry", "lake", "grass", "lakeside")    #fish needs water, doesnt say anything unless you find a aquarium somewhere at lake area (abandoned ship), person 2 says please find a fish bowl for fish
                    if y == "talking fish":                                                          #selecting a npc will show the npc name on top and talk., if you talk you can select multiple conversation types
                        functions.clearConsoleEnt()
                        print(f"""
Talking fish
──────────────────""")
                        xfishbowl = "fishbowl"
                        if xfishbowl in gameInventory:
                            functions.typeSys("""Thank you for saving me, I was almost out of breath.
It's dangerous to go alone! Take this. """)
                            functions.gameInventory.append("Diving suit")
                            print(f'''\033[93mYou've received the item "Diving suit" \033[0m\n\n''')
                            functions.gameInventory.remove("fishbowl")
                            functions.clearConsoleEnt()
                        else:
                            functions.typeSys("fish sounds\n\n")
                            image = DrawImage.from_file("images/fish.png", (50, 10))
                            image.draw_image()
                            functions.clearConsoleEnt()
                    elif y == "Back":
                        functions.clearConsole()
                        functions.typeSys("\n\nYou can't go back here.\n\n")
                        functions.clearConsoleEnt()
                    elif y == "garry":
                        functions.clearConsole()
                        print(f"""
Garry
──────────────────""")
                        functions.typeSys("\nMy fish doesnt work, please find a fish bowl.\n\n")
                        functions.clearConsoleEnt()     
                    elif y == "grass":
                        functions.clearConsole()
                        print(f"""
Grass
──────────────────""")
                        functions.typeSys("\nYou touched some grass.\n\n")
                        functions.typeSys("You regained 1 \033[92mhp\033[0m\n\n")
                        functions.hitpoints += 1
                        functions.typeSys(f"current \033[92mhp\033[0m: {functions.hitpoints}\n\n")
                        functions.clearConsoleEnt()

                        functions.clearConsoleEnt()
                    elif y == "lake":
                        functions.clearConsole()
                        functions.typeSys(f"""\n
You walk towards the lake, \n\n""", 0.001)
                        functions.clearConsoleEnt()
                        lake = True
                        while lake:
                            functions.typeSys("You are looking around and see... : \n")
                            y1 = functions.chooseSys("abandoned ship", "sand", "sign", "water", "lake")
                            if y1 == "abandoned ship":
                                functions.clearConsole()
                                functions.typeSys(f"""\n
You walk towards the spooky scarry abandoned ship \n\n""", 0.001)
                                functions.clearConsoleEnt()
                                print(f"""
Abandoned ship
──────────────────""")
                                while True:
                                    y2 = functions.tinyChooseSys("fishbowl", "skeleton")
                                    if y2 == "fishbowl":
                                        functions.clearConsole()
                                        optionsC[0] += 1
                                        if optionsC[0] > 1:
                                            functions.typeSys("You already picked this item up, bitch.\n\n")
                                            functions.clearConsoleEnt()
                                        else: 
                                            functions.gameInventory.append("fishbowl")
                                            functions.typeSys(f"""\nYou have obtained a Item {functions.gameInventory[functions.gameInventory.index("fishbowl")]}\n\n""", 0.01)
                                            functions.clearConsoleEnt()
                                    elif y2 == "skeleton":
                                        functions.clearConsole()
                                        print("He has been here for very long.... >.>")
                                    elif y2 == "Me":
                                        functions.menu("Inventory", "Status effects", "Map")
                                    elif y2 == "Back":
                                        functions.clearConsoleEnt()
                                        break
                                    else:
                                        functions.typeSys("Not a valid option")
                                            
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
──────────────────""")
                                
                                functions.typeSys("North - Lakeside ;.\n\n")
                                functions.clearConsoleEnt()
                            elif y1 == "water":
                                optionsC[3] += 1
                                xDivinggear = "Diving suit"
                                if xDivinggear in gameInventory:
                                    functions.typeSys("""\n──────────────────""")
                                else:
                                    functions.typeSys("It looks wet")    #maybe switch case different print function
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

