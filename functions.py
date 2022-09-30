import os
import time
import sys
from time import sleep
from pygame import mixer


gameInventory = []
playerStats = [0, 0]
hitpoints = 3
hints = 0


def intro():
    typeSys(f"""   
      __    ____  _____  _  _  ____    _  _  _____  __  __ 
     /__\  (  _ \(  _  )( \/ )( ___)  ( \/ )(  _  )(  )(  )
    /(__)\  ) _ < )(_)(  \  /  )__)    \  /  )(_)(  )(__)( 
   (__)(__)(____/(_____)  \/  (____)   (__) (_____)(______)""", 0.0001)

    playerName = input("\n Please input your name : ")
    if playerName.isalpha():
        clearConsole()
        typeSys(f"\nWelcome to the game {playerName}", 0.01)
        typeSys(f"""\n  
You suddenly feel a warm feeling in your back and collapse to the floor. 
Your view is getting hazy and slowly fading away. The only thing you see before the last lights 
go out is a silhouette of a person running away. A million questions rush into your head. 
Who is this person? Why me? Why is the floor so floory? Right before you die you swore to find out who killed you. \n\n\n""", 0.001)
        input("Press enter to continue...")
        clearConsole()
    else:
        print("Invalid name; please use characters only!")
        playerName = input("Please input your name : ")



# Console clearen voor de woord rader
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def clearConsoleEnt():
    input("\nPress enter to continue...")
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def chooseSys(Op1, Op2, Op3, Op4, Choices="Choices", Menu="Me", Back="Back" ):

    Options = [Op1, Op2, Op3, Op4, Menu, Back]

    print(f"""                      
\033[1m{Choices} \033[0m                   
 \033[1m─────────────────────────     \033[0m               
\033[1m\033[95m1\033[0m {Options[0]}\t\t     \033[0m     
\033[1m\033[96m2\033[0m {Options[1]}\t\t    \033[0m      
\033[1m\033[93m3\033[0m {Options[2]}\t\t   \033[0m               
\033[1m\033[91m4\033[0m {Options[3]}\t\t\033[0m
 \033[1m─────────────────────────\n\033[0m
\033[1m5 {Options[4]}\t\t    6 {Options[5]} \033[0m
 \033[1m─────────────────────────\n\033[0m

 """, )
    
    try: 
     z = int(input("Enter a number you'd like to choose: "))
     if z == 1 or z == 2 or z == 3 or z == 4 or z == 5 or z == 6:
        text = Options[(z-1)]
        return text
    except:
         print("Not an option loser")

def menu(Op1 = "Inventory", Op2 = "playerStatus",Op3 = "Map", op4 = "Back"):

    menuOptions = [Op1, Op2, Op3, op4]
    while True:
        clearConsole()
        print(f"""
Me    |Health: {hitpoints}
──────────────────
\033[95m1\033[0m {menuOptions[0]}
\033[96m2\033[0m {menuOptions[1]} 
\033[93m3\033[0m {menuOptions[2]}
──────────────────
\033[1m4\033[0m {menuOptions[3]}\n
""")
        z = input("Type the option you want: ").lower()
        if z == "inventory" or z == "1":
            clearConsole()
            while True:
                print(f"""
Inventory
──────────────────""")
                print(f"{gameInventory}")
                inventoryCheck = input("Type the item name you'd like to inspect or enter q to quit inventory: ").lower()
                if inventoryCheck == "q":
                        break
                if inventoryCheck in gameInventory:
                    if inventoryCheck == "adoption papers":
                        print("It is a picture of me in the adoption papers!\n\n")
                        print("You become sad.")
                        gameInventory.remove("adoption papers")
                        print("\nYou discard the adoption papers")
                        playerStats[1] += 1
                    elif inventoryCheck == "car keys":
                        print("I wish I had a car\n\n")
                        clearConsoleEnt()
                    elif inventoryCheck == "picture of your mom":
                        print("She looks oddly familiar...")
                        clearConsoleEnt()
                    elif inventoryCheck == "jar of milk":
                        inputInventory = input("\nThe jar of milk seems to be glowing bright, would you like to drink it? (Y/N) ").lower()
                        print("\n")
                        clearConsoleEnt()
                        if inputInventory == "y":
                            gameInventory.remove("jar of milk")
                            playerStats[0] += 1
                            print("You feel the power of the milk flowing through your bloodstream. You have gained fire resistance\n")
                            print("\033[93mjar of milk has been removed from your inventory\033[0m\n\n")
                            clearConsoleEnt()
                        elif inputInventory == "n":
                            continue
                        else:
                            print("L bozo, this is not a valid input")
                CQuit = input("Do you want continue looking in your inventory? (Y/N) ").lower()
                if CQuit == "y":
                    clearConsole()
                    continue
                else:
                    break
        elif z == "status effect" or z == "2":
            clearConsole()
            print(f"""
Status effects
──────────────────
""")
            if playerStats[0] == 1:
                print("Fire resistance")
            if playerStats[1] == 1:
                print("Sad")

            clearConsoleEnt()
        elif z == "map" or z == "3":
            clearConsole()
            print(f"\nYou havent found a map yet\n\n")
            clearConsoleEnt()
            continue
        elif z == "back" or z == "4":
            clearConsole()
            break
        else:
            print("Not a valid option")

        

def typeSys(xWords, time = 0.0):
    for char in xWords:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()

def gameMap(location):
    maps = [f"""    #######    /##################################################### #####                                                                    
########                                                            
    (#                                                                               #/                                                            
    (#                                                                               #/                                                            
    ##                                                                               ##                                                            
    ##                                                                               ##                                                            
##/                                                                               (##                                                           
##                                                                                 ##                                                           
##                                                                                 ##                                                           
##                                      /                                          ##                                                           
##                                    ,*///                                        ##                                                           
##                                    ///////                                      ##                                                           
##                                    ////////                                     ##                                                           
##                                    /////////                                    ##                                                           
##                /,                /*/////////*/                                  ##                                                           
##/               //                //////////////                                /##                                                           
###              ///               ///////////////*/     ///                      ###                                                           
###            .////               /////***//////////   ////*                     ###                                                           
###           ./////   //////     //////****//////////  /////                     ###                                                           
###           //////  ////////// //////******.////////////////                    ###                                                           
*##         ///////////////////////////******,,///////////////,/   ,/       /.    ##*                                                           
*#/       .///////////////////////////*********////////////////// ////     ///    (#,                                                           
    #.      /*//////**//////////////////*************/***/////////////////.  ////*/   #                                                            
    ##    /,////////***//////*////////*******************,*//*******//////////////*/ ##                                                            
    ##  /*////////******,///,**/,****,*****************************************//////##                                                            
    (# //////////********,,.***************************************************.*/////#                                                            
    *##(##********************************************************************#*##(/                                                            
            ,   *#*******************************************************(######.                                                                  
                    ,(#########################################(/.                  """,  f""" map 2"""]
    print(maps[location])


def playSound(soundPath, volume = 0.01):
    #Instantiate mixer
    mixer.init()
    #Load audio file
    mixer.music.load(soundPath)
    mixer.music.set_volume(volume)
    print("music started playing....")
    #Play the music
    mixer.music.play()
    



# hidden status effect, gameplay chaanges based on actions. 