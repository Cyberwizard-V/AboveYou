from re import X
import functions
import time
import climage
from functions import *
from image import DrawImage

#\033[0m ending quote for color


def stageMountain():
    stageMountain = True

    while stageMountain:
        print("\033[96mStage Ice mountain\033[0m")
        functions.typeSys(f"""
Every step you take keeps getting colder and colder.
Eventually the steps become slippery with ice.)
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
        optionsM = [0, 0 ,0, 0, 0]
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
                        print(f"""
Melting snowman
──────────────────""")
                        functions.typeSys(f"""
I am running out of time
\n\n""")
                        functions.clearConsoleEnt()
                elif b1 == "tree trunk":                                #examine tree trunk? idk find a lab coat?
                        functions.clearConsole()
                        print(f"""
Tree trunk
──────────────────""")
                        functions.typeSys(f"""
Looks hollow here.
\n\n""")
                        functions.clearConsoleEnt()
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
                        mountainPass = True
                        while mountainPass:
                                p1 = functions.chooseSys("deranged scientist", "butterfly", "white's lab", "more stairs", "Mountain pass")
                                if p1 == "deranged scientist":                                            #It is white talking gibberish, got deranged by vial
                                        functions.clearConsole()
                                        print(f"""
Deranged scientist
──────────────────""")
                                        functions.typeSys(f"""
Bla bla bla bla bla                                                     
\n\n""")                                                                                                #enter random gibberish and accidentally leak the password for his lab?
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
The typical looking at a lab on a mountain cutscene...
""")
                                        functions.clearConsoleEnt()
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
                                        mountainTop = True
                                        while mountainTop:
                                                t1 = functions.chooseSys("snow", "cones", "clouds", "ravine", "Mountain top")
                                                if t1 == "snow":                                                #pick up any snow for snowman?                              
                                                        functions.clearConsole()
                                                        print(f"""
Snow                    
──────────────────""")
                                                        functions.typeSys(f"""
All kind of snow colors, the yellow snow looks tasty...                                                  
\n\n""")                                                                                               
                                                        functions.clearConsoleEnt()    
                                                elif t1 == "cones":                                            
                                                        functions.clearConsole()
                                                        print(f"""
Cones
──────────────────""")
                                                        functions.typeSys(f"""
Perfect to scoop some yellow and brown snow with                                                 
\n\n""")                                                                                               
                                                        functions.clearConsoleEnt() 
                                                elif t1 == "clouds":                                            # idk yet heal yourself or something                               
                                                        functions.clearConsole()
                                                        print(f"""
Clouds
──────────────────""")
                                                        functions.typeSys(f"""
You are on cloud9, chase the clout                                             
\n\n""")                                                                                               
                                                        functions.clearConsoleEnt() 
                                                elif p1 == "Me":
                                                        functions.clearConsole()
                                                        functions.menu("Inventory", "Status effects", "Map")
                                                elif p1 == "Back":
                                                        functions.clearConsole()
                                                        break
                                                elif t1 == "ravine":                                           # fall down if you proceed with yes, breaks loop                    
                                                        functions.clearConsole()
                                                        print(f"""
Ravine
──────────────────""")
                                                        functions.typeSys(f"""
A huge ravine is in front of you.
I can see my home from here!                                              
\n\n""")                                                                                               
                                                        functions.clearConsoleEnt() 
                                                        break
                                                
                                        

