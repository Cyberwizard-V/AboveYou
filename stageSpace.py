# in space ship you explore trying to get back, you read the papers white left behind about his experiment,  couldnt controll it killed you.
# truth is red sent white to make an experiment to kill people for him
# there is a return to earth button, but isnt labeled correctly -> shoots you in space instead

#if you didnt drink the vial -> the end you died in space
# if you did drink the vial you will drift away in space for eternity 
# if gun and drink the vial you can shoot yourself if you select gun in inventory. if you shoot yourself you go back to hell to kill red

from re import X
import functions
import time
import climage
from functions import *
from image import DrawImage

def stageSpace():
    note1 = False
    note2 = False

    print("\033[1;30;40m Stage Space      \033[0m")
    functions.typeSys(f"""
You blasted yourself into space. The answer was so close yet so far.
I get the feeling that white exactly knew what happened to me.
It is pretty much impossible to solve the mystery now...\n\n""", 0.001)
    functions.clearConsoleEnt()
    functions.typeSys(f"""
You decide and look for a way to get you back to earth and find more information about your death.\n\n""", 0.001)
    functions.clearConsoleEnt()
    environmentSpace = True
    while environmentSpace:

            s1 = functions.chooseMaze("note 1", "note 2", "big red button", "hard socks", "Spaceship")
            if s1 == "note 1":
                note1 = True
                functions.clearConsole()
                functions.typeSys(f"""
White's notes
──────────────────

Day 1
Yesterday Red asked me to make a deadly beast for him. The purpose of the beast is to kill people.
Red is getting lazy and putting his workload on me. He just wants to watch the beast killing people for him.

Day 6
Red offered me a spot in heaven if i made this beast. It is a very tempting idea...

                  """, 0.001)
                playerStats[5] += 1
                functions.clearConsoleEnt()
            elif s1 == "note 2":
                note2 = True
                functions.clearConsole()
                functions.typeSys(f"""
White's notes
──────────────────

Day 23
I managed to make the beast. 

Day 33
It seems i can't control this beast anymore. I don't wanna take the responsibility of this wild beast.

Day 35
This will be the last day.. i can't take this anymore... I will end myself with this mysterious vial

Day 36
&*#)!kjfisdofns ihdajooplajfduioq3hr ioudfienfouf akdpafhw pehfouashfipasfhui heiouehf9ahfpiasjfj
fhasoifjsia siofasiofj aopfhjioasfjopasif miasjfi ah fio jasifshiof asufha f uasfoas f
asfj fkasfjkh asfajf 

Me
It seems like he got braindead from the vial lol

                  """, 0.001)
                playerStats[5] += 1
                functions.clearConsoleEnt()
            elif s1 == "big red button":
                functions.clearConsole()
                functions.typeSys(f"""
The big red button is labled "Back to earth"

I quickly press it without thinking...\n""")

                functions.typeSys(f"""
The doors suddenly open up and shoots me into space.


        ~+

                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +         ඞ                +
        O      *        '       .

""", 0.001)
                functions.clearConsoleEnt()
                
                if playerStats[4] and "gun" in gameInventory and playerStats[5]:
                    functions.clearConsole()
                    functions.typeSys(f"""
You slowly drift away in space for eternity...
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ?ඞඞඞඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam

""", 0.001)
                    functions.clearConsoleEnt()
                    functions.typeSys(
                        "You remember you still had the gun from white's lab...\n\n")
                    death = input(
                        "Would you like to use the gun? (Y/N) ").lower()
                    if death == "y":
                        functions.clearConsole()
                        functions.playSound("music/gun.mp3", 1)
                        functions.clearConsoleEnt()
                        functions.playSound("music/what.mp3", 1)
                        print(f"""
                    A WORKING GUN AND SOUNDS IN SPACE?
────────────────────────────────────────────────────────────────────────
        
        
                       _   _                                  _    
                      | | (_)                                | |   
  __ _ _   _  ___  ___| |_ _  ___  _ __  _ __ ___   __ _ _ __| | __
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \| '_ ` _ \ / _` | '__| |/ /
| (_| | |_| |  __/\__ \ |_| | (_) | | | | | | | | | (_| | |  |   < 
 \__, |\__,_|\___||___/\__|_|\___/|_| |_|_| |_| |_|\__,_|_|  |_|\_\ 
    | |                                                            
    |_|                                                            



─────────────────────────────────────────────────────────────────────────
                                HOW??   
                    \n\n""")
                        functions.clearConsoleEnt()
                        functions.typeSys("You shot yourself...\n\n")
                        functions.clearConsoleEnt()
                        functions.typeSys(
                            "You open your eyes and find yourself back in hell...\n\n")
                        functions.clearConsoleEnt()
                        print(f"""
\033[91mRed\033[0m
──────────────────""")
                        functions.typeSys(f"""\n
Welcome back, I've been expecti-.\n\n""")
                        functions.clearConsoleEnt()
                        print("haha gun goes brrrrr\n\n")
                        functions.playSound("music/gun.mp3", 1)
                        time.sleep(1)
                        functions.playSound("music/gun.mp3", 1)
                        time.sleep(1)
                        functions.playSound("music/gun.mp3", 1)
                        time.sleep(1)
                        functions.playSound("music/gun.mp3", 1)
                        functions.clearConsoleEnt()
                        functions.typeSys(f"""
You killed red and take over his role...
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ඞඞඞඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam
Thanks for playing.
\n\n""", 0.001)

                    if death == "n":
                        functions.clearConsole()
                        functions.typeSys(f"""
You slowly drift away in space for eternity...
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ?ඞඞඞඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam
Thanks for playing.
\n\n""", 0.001)
                        input("Press enter to quit...")
                        break
            
                elif playerStats[4] and "gun" in gameInventory:
                    functions.clearConsole()
                    functions.typeSys(f"""
You slowly drift away in space for eternity...
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ? ඞඞඞඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam

""", 0.001)         
                    functions.clearConsoleEnt()
                    functions.typeSys("You remember you still had the gun from white's lab...\n\n")
                    death = input("Would you like to use the gun? (Y/N) ").lower()
                    if death == "y":
                        functions.clearConsole()
                        functions.playSound("music/gun.mp3", 1)
                        functions.clearConsoleEnt()
                        functions.playSound("music/what.mp3", 1)
                        print(f"""
                    A WORKING GUN AND SOUNDS IN SPACE?
────────────────────────────────────────────────────────────────────────
        
        
                       _   _                                  _    
                      | | (_)                                | |   
  __ _ _   _  ___  ___| |_ _  ___  _ __  _ __ ___   __ _ _ __| | __
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \| '_ ` _ \ / _` | '__| |/ /
| (_| | |_| |  __/\__ \ |_| | (_) | | | | | | | | | (_| | |  |   < 
 \__, |\__,_|\___||___/\__|_|\___/|_| |_|_| |_| |_|\__,_|_|  |_|\_\ 
    | |                                                            
    |_|                                                            



─────────────────────────────────────────────────────────────────────────
                                HOW??   
                    \n\n""")
                        functions.clearConsoleEnt()
                        functions.typeSys("You shot yourself to end the missery...")
                    if death == "n":
                        functions.clearConsole()
                        functions.typeSys(f"""
You slowly drift away in space for eternity...
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ? ඞඞඞඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam
Thanks for playing.
\n\n""", 0.001)
                        input("Press enter to quit...")
                        break

                
                elif playerStats[4]:
                    functions.clearConsole()
                    functions.typeSys(f"""
You slowly drift away in space for eternity... 

 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ? ඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam

""", 0.001)
                    input("Press enter to quit...")
                    break

                else:
                    functions.clearConsole()
                    functions.typeSys(f"""
massive skill issue
you died accidentally shot yourself into space...
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ?ඞඞඞඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam

""", 0.001)
                input("Press enter to quit...")
                break
    


            
            elif s1 == "hard socks":
                functions.clearConsole()
                print("Pervert")
                functions.clearConsoleEnt()
            elif s1 == "Menu":
                functions.menu("Inventory", "Status effects", "Map")
            else: 
                functions.clearConsole()
                functions.typeSys(f"""

 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ?ඞඞඞඞ
                                                                                   
Credits: ඞJeffrey Yeh, ඞViktor Stam

""", 0.001)
                input("Press enter to quit...")
                break
