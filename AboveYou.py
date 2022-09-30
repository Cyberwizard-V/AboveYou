import functions
import time
from functions import *
from stageHell import stageHell1
from stageLake import stageLake
#\033[93m acitons happening

#Main program function
def main():
    mainscreen = False
    #Mainscreen
    while mainscreen:
        #functions.playSound("music/minecraftmusic.mp3", 1)
        functions.clearConsole()
        functions.intro()
        break
    #Stage hell/red's throne | RED
    #stageHell1()
    #Stage River/Lake        | BLUE
    stageLake()

                            



main()

