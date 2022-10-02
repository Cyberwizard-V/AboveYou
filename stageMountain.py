from re import X
import functions
import time
import climage
from functions import *
from image import DrawImage

#\033[0m ending quote for color
optionsM = [0, 0 ,0, 0, 0]
xsecret = "lab coat"
xGun = "Gun"
def stageMountain():
    stageMountain = True
    mountainTop = True
    insideLab = True
    mountainPass = True
    rocketship = True
    mountainPass = True
    environmentMountain = True

    while stageMountain:
        print("\033[1mStage Ice mountain\033[0m")
        functions.typeSys(f"""
Every step you take keeps getting colder and colder.
Eventually the steps become slippery with ice.
You bump your head against a hard surface.
It is a hatch leading outside, 
you push the hatch open...\n\n""", 0.001)
        functions.clearConsoleEnt()
        functions.typeSys(f"""
Cold air rushes down the hole you came from.
The entire environment has changed from dark and moist to dry and cloudy.
The air feels thin and it is harder to breathe. It looks like we are at the base of a mountain.

It is cold, I should quickly look for White's whereabouts. \n\n""", 0.001)
        functions.clearConsoleEnt()

        functions.typeSys(f"""
The mountain looks huge. I dont want to take those the stairs...
 \n""", 0.001)
        
        environmentMountain = True
        while environmentMountain:
                b1 = functions.chooseSys("tree trunk", "snowman", "boombox", "stairs", "Mountain base")
                if b1 == "boombox":
                        functions.clearConsole()
                        print(f"""
Boombox
──────────────────""")
                        functions.typeSys(f"""
It looks like it has been used recently.
It seems that it has a few song options available.\n\n""")
                        functions.clearConsoleEnt()
                        xboomBox = True
                        while xboomBox:
                                bb = functions.chooseSys("song 1", "song 2", "song 3", "song 4", "Boombox")
                                if bb == "song 1":
                                        functions.clearConsole()
                                        functions.typeSys(f"""
A song starts playinig...\n\n""")
                                        functions.playSound("music/chad.mp3", 1)
                                        functions.clearConsoleEnt()
                                elif bb == "song 2":
                                        functions.clearConsole()
                                        functions.typeSys(f"""
A song starts playinig...\n\n""")
                                        functions.playSound("music/sigma.mp3", 1)
                                        functions.clearConsoleEnt()
                                elif bb == "song 3":
                                        functions.clearConsole()
                                        functions.typeSys(f"""
A song starts playinig...\n\n""")
                                        functions.playSound("music/megalovania.mp3", 1)
                                        functions.clearConsoleEnt()
                                        functions.typeSys(f"""
        \033[93mYou are filled with determination\033[0m\n\n""")
                                        functions.playerStats[2] += 1
                                        functions.clearConsoleEnt()
                                elif bb == "song 4":
                                        functions.clearConsole()
                                        functions.typeSys(f"""
A song starts playinig...\n\n""")
                                        functions.playSound("music/ok.mp3", 1)
                                        functions.clearConsoleEnt()
                                elif bb == "Me":
                                        functions.clearConsole()
                                        functions.menu("Inventory", "Status effects", "Map")
                                elif bb == "Back":
                                        functions.clearConsoleEnt()
                                        break
                elif b1 == "snowman":                                   #make questline bring him snow he will give you the answer to enter whites lab
                        functions.clearConsole()

                        xNote = "notebook"
                        if gameInventory.count("snow") >= 5:
                                print(f"""Thanks for finding me \033[96msnow!\033[0m """)
                                count = 0
                                while count < 5:
                                        count += 1
                                        gameInventory.remove("snow")
                                functions.gameInventory.append(xNote)
                                functions.clearConsoleEnt()
                                print(f'''\n\n\033[93mYou've received the item "{xNote}" \033[0m\n\n''')
                                functions.clearConsoleEnt()
                        elif xNote in gameInventory:
                                print(f"""Thanks for finding me \033[96msnow!\033[0m """)
                                print(f"""Please read the \033[96mnotebook\033[0m ;)""")
                        else:
                                print(f"""
Melting snowman
──────────────────""")
                                functions.typeSys(f"""
        I am running out of time.. please find some snow for me...
        \n\n""")
                                print(f""" Quest: Find \033[96m({gameInventory.count("snow")}/5)\033[0m snow for the snowman """)


                        functions.clearConsoleEnt()
                elif b1 == "tree trunk":                               
                        functions.clearConsole()
                        print(f"""
Wise tree trunk
──────────────────""")
                        functions.typeSys(f"""
Looks hollow, someone carved a message in the wood.

What is always in front of you but can’t be seen
                Viktor 💘 Jeffrey

It looks like a love letter?

\n\n""")
                        
                        secret = input("Press enter to continue? ").lower()
                        if "future" in secret:   
                                functions.gameInventory.append(xsecret)
                                functions.clearConsoleEnt()
                                print(f'''\n\n\033[93mYou've received the item "{xsecret}" \033[0m\n\n''')
                                functions.clearConsoleEnt()
                        else:
                                functions.playSound("music/oofsucky.mp3", 100)
                                print("bruh you stupid...")

                                
                elif b1 == "Me":
                        functions.clearConsole()
                        functions.menu("Inventory", "Status effects", "Map")
                elif b1 == "Back":
                        functions.clearConsole()
                        functions.typeSys("\n\nYou can't go back here.\n\n")
                        functions.clearConsoleEnt()

                elif b1 == "stairs":
                        functions.clearConsole()
                        functions.typeSys(f"""
You slowly make your way up the stairs.\n\n""")
                        functions.clearConsoleEnt()
                        
                        while mountainPass:
                                functions.typeSys("I should try and enter the lab for more clues about White and who killed me.")
                                p1 = functions.chooseSys("deranged scientist", "butterfly", "white's lab", "more stairs", "Mountain pass")
                                if p1 == "deranged scientist":                                            #It is white talking gibberish, got deranged by vial
                                        functions.clearConsole()
                                        print(f"""
Deranged scientist
──────────────────""")
                                        functions.typeSys(f"""
Tffh i,diislth hoawtselgwmlmueo b,ahdtodytm nrr to eto  ;aawteeun  eWan eioten,nncdoslhgou no  akt sc myetr en a irmtns rt hsf eo: t'haitouobiyba pgh,oss   tesn ,slafdrdastudo easouhw  habnsef rnetewvasehhdtc?o  t  usr ,ir;ohusn les eacnn ottm   rfr eeefdrtreereenahtlaregese                                           
\n\n""")                       
                                        functions.typeSys("What is wrong with him? Probably took some of his weird experiments\n\n\n")                                                                     
                                        functions.clearConsoleEnt()
                                elif p1 == "butterfly":
                                        functions.clearConsole()
                                        bird = climage.convert('images/bird.png')
                                        print(bird)
                                        print("\t\t\t\tIs this a pigeon?")
                                        functions.clearConsoleEnt()                     
                                elif p1 == "white's lab":                                               #make game in order to enter his lab, simon says/ hangman?
                                        functions.clearConsole()
                                        print(f"""
White's lab
──────────────────""")
                                        functions.typeSys(f"""
*Insert lightning*
The typical looking at a lab on a mountain cutscene...\n\n
""")                                    
                                        functions.clearConsoleEnt()
                                        whitesLab = True
                                        while whitesLab:
                                                if xsecret in gameInventory:
                                                        functions.typeSys(f"""beep boop. Welcome back professor beep boop\n\n""")
                                                        functions.clearConsoleEnt()
                                                elif xsecret not in gameInventory:
                                                        password = input("beep boop. Please enter the password. Beep boop: ").lower()
                                                        if password == "jazz":
                                                                functions.clearConsole()
                                                                functions.typeSys(f"""beep boop. Welcome back professor. beep boop\n\n""")
                                                                functions.clearConsoleEnt()
                                                else: 
                                                        functions.clearConsole()
                                                        functions.tinyChooseSys("Incorrect password, I like jazz")
                                                        functions.clearConsoleEnt()
                                                        break

                                                
                                                while insideLab:
                                                        l1 = functions.chooseSys("rocketship", "flight manual", "strange vial", "gun", "White's Lab")
                                                        if l1 == "strange vial":
                                                                functions.clearConsole() 
                                                                print(f"""
Strange vial
──────────────────""")
                                                                functions.clearConsole()
                                                                optionsM[1] += 1
                                                                if optionsM[1] > 1:
                                                                        functions.typeSys("Dont be greedy, leave some for other players bitch.\n\n")
                                                                        functions.clearConsoleEnt()
                                                                else: 
                                                                        functions.gameInventory.append("strange vial")
                                                                        functions.typeSys(f"""\n\033[93mYou have obtained a Item {functions.gameInventory[functions.gameInventory.index(l1)]}\n\n\033[0m""", 0.01)
                                                                        functions.clearConsoleEnt()
                                                        elif l1 == "flight manual":
                                                                functions.clearConsole()
                                                                print(f"""
Flight manual
──────────────────""")
                                                                image = DrawImage.from_file("images/flightmanual1.png", (40, 20))
                                                                image.draw_image()
                                                                print("cool rocket it works")
                                                                functions.clearConsoleEnt()
                                                                image = DrawImage.from_file("images/flightmanual2.png", (40, 20))
                                                                image.draw_image()
                                                                print("To start the rocket i need to press this button...")
                                                                functions.clearConsoleEnt()
                                                                image = DrawImage.from_file("images/flightmanual3.png", (40, 20))
                                                                print("To open the door it is that button...")
                                                                image.draw_image()
                                                                functions.clearConsoleEnt()
                                                                image = DrawImage.from_file("images/flightmanual4.png", (40, 20))
                                                                print("cool, I believe I know how a rocket works now ")
                                                                image.draw_image()
                                                                functions.clearConsoleEnt()
                                                                functions.playerStats[3] += 1
                                                        elif l1 == "gun":
                                                                functions.clearConsole()
                                                                if xGun in gameInventory:
                                                                        print(f'''\n\n\033[93mYou've already received the item "{xGun}", shoot yourself \033[0m\n\n''')
                                                                        functions.clearConsoleEnt()

                                                                else:
                                                                        print(f"""
Gun.
──────────────────""")   
                                                                        functions.gameInventory.append(xGun)
                                                                        functions.clearConsoleEnt()
                                                                        print(f'''\n\n\033[93mbang bang is a  "{xGun}" you received \033[0m\n\n''')
                                                                        functions.clearConsoleEnt()
                                                        elif l1 == "Me":
                                                                functions.clearConsole()
                                                                functions.menu("Inventory", "Status effects", "Map")
                                                        elif l1 == "Back":
                                                                functions.clearConsole()
                                                                print("Can't go back...")
                                                                functions.clearConsoleEnt()
                                                        elif l1 == "rocketship":
                                                                functions.clearConsole()
                                                                if functions.playerStats[3] != 1:
                                                                        print(f"""Please read the manual first !""")
                                                                else:
                                                                        while rocketship:
                                                                                functions.typeSys(f"""\n
When entering the rocket ship you suddenly see white running towards the rocketship,
It was the deranged scientist after all! Red told me to catch him! """, 0.01)
                                                                                functions.typeSys(f"""\n
White is mad that you entered his lab without permission. 
You try to press all the buttons of the ship to open the door and catch him for Red.""", 0.01)
                                                                                input("\nPress the buttons... (enter)")
                                                                                functions.typeSys(f"""
You accidentally launch the spaceship while trying to open the door.
Even after reading the manual you didnt know which buttons to press.
skill issue ...\n\n""", 0.05)
                                                                                break
                                                                        for i in range(3,0, -1):
                                                                                print(f"{i} seconds until launch", end="\r", flush=True)
                                                                                image = DrawImage.from_file(f"images/{i}letter.jpg", (40, 20))
                                                                                image.draw_image()
                                                                                time.sleep(1)
                                                                                if i == 1:
                                                                                        print(f"""
                                                                                                                                                                                                                                                                                
            ░░                                                                  ░░      
                                                                                        
                                                                                        
      ░░                                ░░  ██                                          
  ░░                                        ██                              ░░░░        
                                            ██                                          
                                          ▓▓▓▓▓▓                                        
                                        ▓▓▓▓▓▓▓▓▓▓                                      
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▒▒▓▓▓▓▒▒▓▓▓▓                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ░░░░▒▒░░░░░░░░                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▒▒▒▒▓▓▒▒▒▒▓▓                                    
                                      ▓▓▒▒▒▒██▒▒▒▒▓▓                                    
                                    ████▓▓▓▓▓▓██▓▓▓▓██      ░░                          
                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                
                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                              
                                ▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              
        ░░                      ▓▓▓▓▓▓░░████████████░░████                        ░░    
                                ▓▓     ░░░░░░▓▓░░░░░   ▓▓                              
                                        ░░░░░░░░░░░                                               
                                          ░░░░░░░                                             
                                            ░░░░                                           
                                             ░░                                          
                        ▒▒                ▒▒            ▒▒          ▒▒    ▒▒   
                                                                                        """)

                                                                        mountainTop = False 
                                                                        insideLab = False
                                                                        mountainPass = False
                                                                        rocketship = False
                                                                        whitesLab = False
                                                                        environmentMountain = False
                                                                        stageMountain = False
                                                                        break

                                elif p1 == "Me":
                                        functions.clearConsole()
                                        functions.menu("Inventory", "Status effects", "Map")
                                elif p1 == "Back":
                                        functions.clearConsole()
                                        break

                                elif p1 == "more stairs":
                                        functions.clearConsole()
                                        functions.typeSys(f"""
Another stairs, but this one is even bigger...\n\n""")
                                        functions.clearConsoleEnt()
                                        while mountainTop:
                                                t1 = functions.chooseSys("snow", "cones", "clouds", "ravine", "Mountain top")
                                                if t1 == "snow":                                                               
                                                        functions.clearConsole()
                                                        print(f"""
Snow                    
──────────────────""")
                                                        functions.typeSys(f"""
The yellow snow looks tasty...                                                  
\n\n""")                                                            
                                                        xSnow = "snow"
                                                        functions.gameInventory.append(xSnow)
                                                        functions.clearConsoleEnt()
                                                        print(f'''\n\n\033[93mYou've received the item "{xSnow}" \033[0m\n\n''')
                                                        functions.clearConsoleEnt()   
                                                elif t1 == "cones":                                            
                                                        functions.clearConsole()
                                                        print(f"""
Cones
──────────────────""")
                                                        functions.typeSys(f"""
Perfect to scoop some yellow and brown snow with.                                                 
\n\n""")                                                                                               
                                                        functions.clearConsoleEnt() 
                                                elif t1 == "clouds":                                                                
                                                        functions.clearConsole()
                                                        print(f"""
Clouds
──────────────────""")
                                                        functions.typeSys(f"""
You are on cloud9, chase that clout                                             
\n\n""")                                                                                               
                                                        functions.clearConsoleEnt() 
                                                elif t1 == "Me":
                                                        functions.clearConsole()
                                                        functions.menu("Inventory", "Status effects", "Map")
                                                elif t1 == "Back":
                                                        functions.clearConsole()
                                                        break
                                                elif t1 == "ravine":                                                      
                                                        functions.clearConsole()
                                                        print(f"""
Ravine
──────────────────""")
                                                        functions.typeSys(f"""
A huge ravine is in front of you.
I can see my home from here!                                              
\n\n""")                                                
                                                        functions.typeSys("A sign is warning you not to take the shortcut.\n\n")
                                                        warning = input("Would you like to take the shortcut? (Y/N) ").lower()
                                                        if warning == "y":                           
                                                                functions.clearConsole()
                                                                functions.typeSys("\nYou take a dive head first down to the mountain base...\n\n")
                                                                mountainTop = False
                                                                mountainPass = False
                                                                functions.typeSys("You nearly broke your neck, you lost 1 \033[91mhp\033[0m\n\n")
                                                                functions.hitpoints -= 1
                                                                functions.typeSys(f"current \033[91mhp\033[0m: {functions.hitpoints}\n\n")
                                                                functions.clearConsoleEnt()
                                                                break
                                                        elif warning == "n":
                                                                functions.typeSys("\nYou decide not to take the leap of faith.")
                                                                functions.clearConsoleEnt()
                                                                continue
                                                        else:
                                                                print("??????????\n\n")
                                                                functions.clearConsoleEnt()
                                        

