from time import sleep
import sys


def typewriter(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)


# typewriter("This is a new bit of wicked fucking tettttxtxtxttxtxtxtxxtt")


def new_intro():
    # loads of code
    typewriter(
        "This si the new liffffeeeee for rrrr meeeeeeeeeeeee, and i'm feeeling goood, ba bum, ba bum")


new_intro()
