from re import X
import functions
import time
import climage
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
                functions.typeSys(f"""
You look around, and see\n\n""", 0.001)
                while environmentLake:
                    
                    y = functions.chooseSys("talking fish", "garry", "lake", "grass", "Lakeside")    #fish needs water, doesnt say anything unless you find a aquarium somewhere at lake area (abandoned ship), person 2 says please find a fish bowl for fish
                    if y == "talking fish":                                                          #selecting a npc will show the npc name on top and talk., if you talk you can select multiple conversation types
                        functions.clearConsole()
                        print(f"""
Talking fish
──────────────────""")
                        xfishbowl = "fishbowl"
                        xDivinggear = "diving suit"
                        xmystNote = "mysterious note"
                        if xfishbowl in gameInventory:
                            functions.typeSys("""Thank you for saving me, I was almost out of breath.

It's dangerous to go alone! Take this. \n\n""")
                            functions.clearConsoleEnt()
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
                        xmystNote = "mysterious note"
                        if xDivinggear in gameInventory and xmystNote in gameInventory:
                            image = DrawImage.from_file("images/garry.png", (40, 20))
                            image.draw_image()
                            functions.typeSys("""\n
Thank you for drowning my fish!
Blue always told me to read my notes.
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
                            functions.clearConsoleEnt()
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
                                        functions.typeSys("...\n\n", 0.5)
                                        functions.typeSys("Because he had no body to go with him!!\n\n")
                                        image = DrawImage.from_file("images/skeleton.jpg", (30, 15))
                                        image.draw_image()
                                        functions.clearConsoleEnt()
                        
                                    elif y2 == "Menu":
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
                                    functions.typeSys("A sign is warning you not to enter without directions.\n\n")
                                    warning = input("Would you still like to proceed to enter the dangerous waters? (Y/N) ").lower()
                                    if warning == "n":
                                        functions.clearConsole()
                                        continue
                
                                    elif warning == "y":
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
                                                wrongway0 = True
                                                while wrongway0:
                                                    w0 = functions.chooseMaze("up", "left", "right", "down", "Flooded river")
                                                    functions.clearConsole()
                                                    if w0 == "down":
                                                        functions.clearConsole()
                                                        break
                                                    elif w0 == "up":
                                                        functions.clearConsole()
                                                        print("Not here\n\n")
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        functions.clearConsoleEnt()
                                                    elif w0 == "left":
                                                        functions.clearConsole()
                                                        print("Use your brain\n\n")
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        functions.clearConsoleEnt()
                                                    elif w0 == "right":
                                                        functions.clearConsole()
                                                        print("bruh\n\n")
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        functions.clearConsoleEnt()
                                                    elif w0 == "Menu":
                                                        functions.menu("Inventory", "Status effects", "Map")

                                            elif e1 == "down":
                                                functions.clearConsole()
                                                wrongway1 = True
                                                while wrongway1:
                                                    w1 = functions.chooseMaze("up", "left", "right", "down", "Flooded sea")
                                                    functions.clearConsole()
                                                    if w1 == "down":
                                                        functions.clearConsole()
                                                        print("skill issue\n\n")
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        functions.clearConsoleEnt()
                                                    elif w1 == "up":
                                                        functions.clearConsole()
                                                        break
                                                    elif w1 == "left":
                                                        functions.clearConsole()
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        print("small brain moment\n\n")
                                                        functions.clearConsoleEnt()
                                                    elif w1 == "right":
                                                        functions.clearConsole()
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        print("the end?\n\n")
                                                        functions.clearConsoleEnt()
                                                    elif w1 == "Menu":
                                                        functions.menu("Inventory", "Status effects", "Map")
                                                   
                                            elif e1 == "Menu":
                                                functions.menu("Inventory", "Status effects", "Map")

                                            elif e1 == "left":
                                                functions.clearConsole()
                                                wrongway2 = True
                                                while wrongway2:
                                                    w2 = functions.chooseMaze("up", "left", "right", "down", "Flooded lake")
                                                    functions.clearConsole()
                                                    if w2 == "down":
                                                        functions.clearConsole()
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        print("syke not here\n\n")
                                                        functions.clearConsoleEnt()
                                                    elif w2 == "up":
                                                        functions.clearConsole()
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        print("you fall into the backrooms it isnt here.\n\n")
                                                        functions.clearConsoleEnt()
                                                    elif w2 == "left":
                                                        functions.clearConsole()
                                                        functions.playSound("music/vineboom.mp3", 100)
                                                        print("It looks like a dead end\n\n")
                                                        functions.clearConsoleEnt()
                                                    elif w2 == "right":
                                                        functions.clearConsole()
                                                        break
                                                    elif w2 == "Menu":
                                                        functions.menu("Inventory", "Status effects", "Map")

                                            elif e1 == "right":
                                                exploring2 = True
                                                while exploring2:
                                                    functions.clearConsole()
                                                    e2 = functions.chooseMaze("up", "left", "right", "down", "Unknown waters")
                                                    if e2 =="left":
                                                        functions.clearConsole()
                                                        break

                                                    elif e2 == "Menu":
                                                        functions.menu("Inventory", "Status effects", "Map")    

                                                    elif e2 == "right":
                                                        functions.clearConsole()
                                                        wrongway4 = True
                                                        while wrongway4:
                                                            w4 = functions.chooseMaze("up", "left", "right", "down", "Flooded sea")
                                                            functions.clearConsole()
                                                            if w4 == "down":
                                                                functions.clearConsole()
                                                                functions.playSound("music/vineboom.mp3", 100)
                                                                print("Do you know da wae\n\n")
                                                                functions.clearConsoleEnt()
                                                            elif w4 == "up":
                                                                functions.clearConsole()
                                                                functions.playSound("music/vineboom.mp3", 100)
                                                                print("You dont know da wae\n\n")
                                                                functions.clearConsoleEnt()
                                                            elif w4 == "left":
                                                                functions.clearConsole()
                                                                break
                                                            elif w4 == "right":
                                                                functions.clearConsole()
                                                                functions.playSound("music/vineboom.mp3", 100)
                                                                print("Read the note\n\n")
                                                                functions.clearConsoleEnt()
                                                            elif w4 == "Menu":
                                                                functions.menu("Inventory", "Status effects", "Map")
                                                        
                                                    elif e2 == "down":
                                                        functions.clearConsole()
                                                        wrongway3 = True
                                                        while wrongway3:
                                                            w3 = functions.chooseMaze("up", "left", "right", "down", "Flooded sea")
                                                            functions.clearConsole()
                                                            if w3 == "down":
                                                                functions.clearConsole()
                                                                functions.playSound("music/vineboom.mp3", 100)
                                                                print("get back to home and read the note\n\n")
                                                                functions.clearConsoleEnt()
                                                            elif w3 == "up":
                                                                functions.clearConsole()
                                                                break
                                                            elif w3 == "left":
                                                                functions.clearConsole()
                                                                print("ooooff\n\n")
                                                                functions.clearConsoleEnt()
                                                            elif w3 == "right":
                                                                functions.clearConsole()
                                                                functions.playSound("music/vineboom.mp3", 100)
                                                                print("happy feet? wombo combo it isnt here\n\n")
                                                                functions.clearConsoleEnt()
                                                            elif w3 == "Menu":
                                                                functions.menu("Inventory", "Status effects", "Map")

                                                    elif e2 == "up":
                                                        exploring3 = True
                                                        while exploring3:
                                                            functions.clearConsole()
                                                            e3 = functions.chooseMaze("up", "left", "right", "down", "Familiar waters")
                                                            if e3 == "down":
                                                                functions.clearConsole()
                                                                break

                                                            elif e3 == "Menu":
                                                                functions.menu("Inventory", "Status effects", "Map")

                                                            elif e3 == "right":
                                                                functions.clearConsole()
                                                                wrongway5 = True
                                                                while wrongway5:
                                                                    w5 = functions.chooseMaze("up", "left", "right", "down", "rock bottom")
                                                                    functions.clearConsole()
                                                                    if w5 == "down":
                                                                        functions.clearConsole()
                                                                        functions.playSound("music/vineboom.mp3", 100)
                                                                        print("dead end\n\n")
                                                                        functions.clearConsoleEnt()
                                                                    elif w5 == "up":
                                                                        functions.clearConsole()
                                                                        functions.playSound("music/vineboom.mp3", 100)
                                                                        print("nope not here either\n\n")
                                                                        functions.clearConsoleEnt()
                                                                    elif w5 == "left":
                                                                        functions.clearConsole()
                                                                        break
                                                                    elif w5 == "right":
                                                                        functions.clearConsole()
                                                                        functions.playSound("music/vineboom.mp3", 100)
                                                                        print("you messed up\n\n")
                                                                        functions.clearConsoleEnt()
                                                                    elif w5 == "Menu":
                                                                        functions.menu("Inventory", "Status effects", "Map")

                                                            elif e3 == "up":
                                                                functions.clearConsole()
                                                                wrongway6 = True
                                                                while wrongway6:
                                                                    w6 = functions.chooseMaze("up", "left", "right", "down", "bikini bottom")
                                                                    functions.clearConsole()
                                                                    if w6 == "down":
                                                                        functions.clearConsole()
                                                                        break
                                                                    elif w6 == "up":
                                                                        functions.clearConsole()
                                                                        functions.playSound("music/vineboom.mp3", 100)
                                                                        print("almost there but not here\n\n")
                                                                        functions.clearConsoleEnt()
                                                                    elif w6 == "left":
                                                                        functions.clearConsole()
                                                                        functions.playSound("music/vineboom.mp3", 100)
                                                                        print("nice try but no\n\n")
                                                                        functions.clearConsoleEnt()
                                                                    elif w6 == "right":
                                                                        functions.clearConsole()
                                                                        functions.playSound("music/vineboom.mp3", 100)
                                                                        print("you made it! jk you didnt\n\n")
                                                                        functions.clearConsoleEnt()
                                                                    elif w6 == "Menu":
                                                                        functions.menu("Inventory", "Status effects", "Map")

                                                            elif e3 == "left":
                                                                functions.clearConsole()
                                                                found = True
                                                                functions.typeSys("You found your way out off the waters, you know where you are. you've seen this on tv before...\n\n")
                                                                while found:
                                                                    f1 = functions.chooseSys("pineapple", "crusty crab", "rock", "blue's cave", "Known waters")
                                                                    if f1 == "pineapple":
                                                                        functions.clearConsole()
                                                                        pineapple = climage.convert('images/pineapple.png')
                                                                        print (pineapple)
                                                                        print("It looks like some kind of sponge is living inside...")
                                                                        functions.clearConsoleEnt()
                                                                    elif f1 == "crusty crab":
                                                                        functions.clearConsole()
                                                                        crab = climage.convert('images/crab.png')
                                                                        print (crab)
                                                                        print("it somehow smells like burgers in here...")
                                                                        functions.clearConsoleEnt()
                                                                    elif f1 == "rock":
                                                                        functions.clearConsole()
                                                                        rock = climage.convert('images/rock.png')
                                                                        print (rock)
                                                                        print("The perfect habitat for a starfish")
                                                                        functions.clearConsoleEnt()

                                                                    elif f1 == "blue's cave":
                                                                        functions.clearConsole()
                                                                        print("\033[96mBlue's cave\033[0m")
                                                                        functions.typeSys(f"""\n
Emerging from the scary waters you manage to find blue's cave.
It is moist, full of lush plants and moss down here.
Every step you take excretes a pool of water.
You decide to walk further and look for Blue.\n\n
""")
                                                                        functions.clearConsoleEnt()
                                                                        print("\t\t\t\tNO ONE IS HERE")
                                                                        output = climage.convert('images/noOne.jpg')
                                                                        print(output)
                                                                        print("\t\t\t\tWHAT?")
                                                                        # image = DrawImage.from_file("images/noOne.jpg", (120,50))
                                                                        # image.draw_image()
                                                                        functions.playSound("music/what.mp3", 1)
                                                                        functions.clearConsoleEnt()
                                                                        functions.typeSys(f"""\n
Suddenly Blue emerges from the solid rock floor.\n\n""")
                                                                        functions.clearConsoleEnt()
                                                                        print(f"""
                            WHAT
__________________________________________________________________
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⠊⣉⣉⠉⠉⠉⠙⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠐⢿⣿⣿⣦⡀⠀⠀⠀⠱⢄⠀⠀⠀⠀⡄⠶⠛⠙⠛⠉⠒⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⢀⣈⣅⣤⡤⠶⠒⠛⠛⠳⢯⡷⠶⢶⣾⣷⣆⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡶⠶⠚⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠘⢷⡄⠀⠉⠉⠙⠷⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⠃⠀⠀⠄⠀⠀⠻⢧⡀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠂⠈⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠄⠀⠀⠉⠳⢦⣄⡀⠀⠀⢰⣼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⡐⠀⠀⠁⠀⠄⠀⠀⢀⠈⠀⠀⠄⠀⠀⡀⠀⠀⠂⢀⠀⠀⠉⠉⠛⠳⠛⠻⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠁⠠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠂⠀⠀⠠⠀⢀⠀⠂⡀⠐⠀⠤⢠⡁⠚⢷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢀⠀⠐⠀⠀⠀⠀⠄⠀⠀⠀⠀⠂⠀⡀⠂⠠⠐⠀⠄⠂⢀⠊⠀⣃⢦⢡⠉⠄⠛⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠈⠀⠀⠀⠀⠀⢀⠀⠀⠄⠀⠁⡀⠐⡀⣀⠁⢠⢡⡌⣀⢆⡄⡌⡰⣈⠆⣻⠜⡂⠑⠬⢿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢃⣀⠀⠠⠀⠀⠄⠀⡀⠠⣀⢐⡈⣠⣄⢦⡵⢴⠮⠿⢶⠿⣾⣿⣶⣝⣷⣑⢪⡕⣏⡒⠈⢈⣹⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⢻⣿⣿⣷⣿⡶⠿⠾⠓⠚⠋⠉⠁⠈⣀⠤⣄⣆⢳⡬⡶⢤⢠⢉⠋⠻⣽⢦⣹⣿⢡⠂⠀⢼⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⣀⢶⣰⠾⣶⣷⡾⢿⣾⣸⢷⣹⢿⣿⢷⡏⣰⠀⡀⠰⠈⠱⠀⢀⠸⣾⢿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢶⣦⣜⣦⣻⣞⣷⣯⣶⣷⣿⣷⣿⣾⣟⣾⡝⣧⢟⡾⣿⣿⣿⢧⡝⣦⣒⢤⣀⣦⣠⢾⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣹⢯⣝⣮⢻⡜⣿⣿⣿⣿⣳⣯⣾⣿⣿⢿⣯⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⢏⡿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣻⠶⣭⡗⣞⢧⣿⢿⣿⣿⣿⣿⣿⣿⣟⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣎⠜⣧⡻⣽⢿⣿⣿⣿⣿⣽⣿⣎⣿⣦⣽⡞⣮⢼⣛⢾⡹⢯⣿⣿⣳⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣰⢻⣭⣛⢿⣯⢿⣿⣟⣯⣟⣼⡷⣯⣝⢮⣳⠻⣬⣛⣿⣼⣿⣽⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠎⠠⠙⣯⠓⢮⠛⣾⡹⣷⡻⣯⣟⣾⡷⣟⡷⣯⢯⣷⣻⡷⣿⣾⡿⣟⣿⢸⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣴⡿⠁⠀⠁⠰⣯⠈⠤⡙⢤⠳⣵⣟⡿⣾⣻⣽⣟⣿⣿⣿⣿⣯⣿⣿⣯⣿⡻⢾⡉⢇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢨⣴⠋⠀⠀⠀⠀⠀⣿⠀⡄⠑⢢⢱⡏⣾⣽⢳⡝⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣯⡝⢻⡄⢩⢻⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣀⣴⡟⠉⠀⠠⠁⠀⠀⠀⠘⢷⣄⠑⢢⠙⣼⢣⡽⣻⢷⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣭⢳⠽⢀⠡⢈⠙⢧⠀
⠀⠀⠀⠀⢀⣠⡶⠞⡉⠆⡍⡒⠠⢀⣠⣆⠀⠀⠀⠀⠀⠀⠙⠷⣦⣑⠮⣳⢟⣽⣻⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣞⠯⠊⢄⠘⡠⠈⠊⡷
⠀⠀⠀⣤⠟⡉⠐⡀⢂⡱⢊⣥⣿⢿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠾⢷⣿⣼⣷⣟⣿⣿⣿⡿⠿⠛⠋⠌⠤⣉⠂⠄⠡⢀⠁⡗
⠀⣠⡊⢀⢂⠤⣱⣸⣿⣿⣝⠨⣁⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠂⠀⠄
____________________________________________________________________
                            HOW??""")
                                                                        functions.playSound("music/what.mp3", 1)
                                                                        functions.clearConsoleEnt()
                                                                        print(f"""
\033[96mBlue\033[0m
──────────────────\n""")
                                                                        functions.typeSys(f"""

You said you were looking for White?
The person you are looking for isn't here.
He once made an escape ladder towards my cave.
This ladder will lead directly to the icy mountains.
\n\n""")
                                                                        functions.clearConsoleEnt()

                                                                        functions.typeSys(f"""

It is riddled with cobwebs and insects.
Every step you take up echoes down the tunnel.
It feels like ages climbing this narrow dark ladder.

You climb further into the darkness...
\n\n""")
                                                                        functions.clearConsoleEnt()
                                                                        stageLake = False 
                                                                        exploring1 = False
                                                                        exploring2 = False
                                                                        exploring3 = False
                                                                        found = False
                                                                        lake = False
                                                                        environmentLake = False


                                                                    elif f1 == "Menu":
                                                                        functions.menu("Inventory", "Status effects", "Map")
                                                                    elif f1 == "Back":
                                                                        functions.clearConsoleEnt()
                                                                        break
                                                                    else:
                                                                        functions.clearConsole()
                                                                        functions.typeSys("\nNot a valid option\n\n")
                                                                        functions.clearConsoleEnt()
                                    else:
                                        print("Thats not even a valid option bozo")
                                        functions.clearConsoleEnt()

                                else:
                                    functions.typeSys("\nA sign is warning you not to enter without directions.\n\nIt looks wet\n\n")    #maybe switch case different print function
                                functions.clearConsoleEnt()
                            elif y1 == "Menu":
                                functions.menu("Inventory", "Status effects", "Map")
                            elif y1 == "Back":
                                functions.clearConsoleEnt()
                                break
                            else:
                                functions.clearConsole()
                                functions.typeSys("\nNot a valid option\n\n")
                                functions.clearConsoleEnt()
                                
                    elif y == "Menu":
                        functions.menu("Inventory", "Status effects", "Map")

