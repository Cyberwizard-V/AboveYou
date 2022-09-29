import os
import time
import sys
from time import sleep
from pygame import mixer


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
        Who is this person? Why me? Why is the floor so floory? Right before you die you swore to find out who killed you. """, 0.001)
        time.sleep(2)
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


def chooseSys(Op1, Op2, Op3, Op4, Op5q, mainOptions = "Main"):

    Options = [Op1, Op2, Op3, Op4, Op5q]
    mainOptions = ["Inventory", "Map", "Quit"]

    print(f"1 {Options[0]}: , 2 {Options[1]}: 3 {Options[2]}:, 4 {Options[3]}: 5 {Options[4]}")
    
    try: 
     z = int(input("Choose : "))
     if z == 1 or z == 2 or z == 3 or z == 4 or z == 5:
        text = Options[(z-1)]
        return text
    except:
         print("Not an option loser")
        

def typeSys(xWords, time):
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



