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
Eventually the steps become slippery with ice.\n\n""", 0.001)
        functions.clearConsoleEnt()
        functions.typeSys(f"""
You bump your head against a hard surface.
It is a hatch leading to the outside, you push the hatch open...\n\n""", 0.001)
        functions.clearConsoleEnt()
        functions.typeSys(f"""
Cold air rushes down the hole you came from.
The entire environment has changed from dark and moist to dry and cloudy.
The air feels thin and it is harder to breathe.

I should look for White's whereabouts. \n\n""", 0.001)
        functions.clearConsoleEnt()