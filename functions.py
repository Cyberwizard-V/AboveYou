import os
import time
import sys
from time import sleep
def intro():
    print(f"""   
      __    ____  _____  _  _  ____    _  _  _____  __  __ 
     /__\  (  _ \(  _  )( \/ )( ___)  ( \/ )(  _  )(  )(  )
    /(__)\  ) _ < )(_)(  \  /  )__)    \  /  )(_)(  )(__)( 
   (__)(__)(____/(_____)  \/  (____)   (__) (_____)(______)""")

    playerName = input("Please input your name : ")
    if playerName.isalpha():
        clearConsole()
        typeSys(f"Welcome to the game {playerName}")
        typeSys(f"""  """)
        time.sleep(20)
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


def chooseSys(Op1, Op2, Op3, Op4):
    Options = [Op1,Op2,Op3,Op4]
    print("Please choose your options;")
    print(f"1 {Options[0]}: , 2 {Options[1]}: 3 {Options[2]}:, 4 {Options[3]}:" )
    try: 
     z = int(input("Choose : "))
     if z == 1 or z == 2 or z == 3 or z == 4:
        text = Options[(z-1)]
        return text
    except:
         print("Not an option loser")

def typeSys(xWords, time):
    print(f"\n###############################\n")
    for char in xWords:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(f"\n###############################\n")




