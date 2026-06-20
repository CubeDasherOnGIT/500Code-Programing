import turtle as pen
t = pen.pen()
import time as waittime
import webbrowser as browser
import os as download
from os.path import join

def startup():
    pen.speed(1)
    t = pen.pen()
    t.speed(pen.speed)
    pen.bgcolor("black")
    print("500 Coding Language")
    print("Made Intirely In Python")
    print("Created By: CubeDasherGD")
    set("penmode", False)
    set("normalmode", True)
    cmd()

def help():
    if penmode == True:
        print("You are currently in pen mode. Type 'normalmode' to exit pen mode and access normal commands.")
        pencmd()
    else:
        browser.open("https://cubedasherongit.github.io/500codehelp/help/basichelp.html/")
        cmd()

def exit():
    print("Exiting...")
    waittime.sleep(1)
    exit

def penmode():
    if penmode == True:
        print("You are currently in pen mode. Type 'normalmode' to exit pen mode and access normal commands.")
        pencmd()
    else:
        print("Entering pen mode...")
        waittime.sleep(1)
        set("penmode", True)
        set("normalmode", False)
        print("Pen mode activated. Normal commands are disabled. Type 'normalmode' to exit pen mode.")
        pencmd()

def normalmode():
    if normalmode == True:
        print("You are currently in normal mode. Type 'penmode' to enter pen mode and access pen mode commands.")
        cmd()
    else:
        print("Exiting pen mode...")
        waittime.sleep(1)
        set("penmode", False)
        set("normalmode", True)
        cmd()

def pencmd():
    pencommand = input()
    if pencommand == "penhelp":
        penhelp()
    elif pencommand == "exit":
        exit()
    elif pencommand == "forward":
        penforward()
    elif pencommand == "backward":
        penbackward()
    elif pencommand == "left":
        penleft()
    elif pencommand == "right":
        penright()
    elif pencommand == "color":
        pencolor()
    elif pencommand == "pensize":
        pensize()
    elif pencommand == "bgcolor":
        bgcolor()
    elif pencommand == "normalmode":
        normalmode()
    else:
        unknownpenmodecommand()

def penhelp():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        browser.open("https://cubedasherongit.github.io/500codehelp/help/penhelp.html/")
        pencmd()

def penforward():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        print("How many pixels do you want to move forward?")
        pixels = int(input())
        t.forward(pixels)
        pencmd()

def penbackward():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        print("How many pixels do you want to move backward?")
        pixels = int(input())
        t.backward(pixels)
        pencmd()

def penleft():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        print("How many degrees do you want to turn left?")
        degrees = int(input())
        t.left(degrees)
        pencmd()

def penright():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        print("How many degrees do you want to turn right?")
        degrees = int(input())
        t.right(degrees)
        pencmd()

def pencolor():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        print("What color do you want to set the pen to?")
        color = input()
        t.color(color)
        pencmd()

def pensize():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        print("What size do you want to set the pen to?")
        size = int(input())
        t.pensize(size)
        pencmd()

def bgcolor():
    if penmode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
        cmd()
    else:
        print("What color do you want to set the background to?")
        color = input()
        t.bgcolor(color)
        pencmd()

def textshow():
    if penmode == True:
        print("What text do you want to show?")
        text = input()
        t.write(text, font=("Arial", 16, "normal"))
        pencmd()
    else:
        print("What text do you want to show?")
        text = input()
        print(text)
        cmd()

def download():
    folderpath = input("Enter folder path: ")
    fileend = ".FiveHundred.py"
    filestart = input("Enter file name: ")
    filename = filestart + fileend
    file_path = join(folderpath, filename)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write("#This Is A FiveHundred Code File. You Can Run The File In Python To Run The Code Written In The File\n")
        file.write("#DONT CHANGE OR DELETE THESE LINES OR THE CODE MAY NOT WORK AS INTENDED\n")
        file.write("import turtle as pen\n")
        file.write("t = pen.pen()\n")
        file.write("import time as waittime\n")
        file.write("import webbrowser as browser\n")
        file.write("import os\n")
        file.write("from os.path import join\n")
        file.write("def exit():\n")
        file.write("   exit\n")
        file.write("\n")
        file.write("#SAFE TO EDIT FROM DOWN HERE\n")
        file.write("#EXAMPLE: TYPE 'print(\"Test\")' FOR DISPLAYING TEXT\n")
        file.write("\n")
        file.write("\n")

def unknowncommand():
    print("Unknown command. Type 'help' for a list of commands.")
    cmd()

def unknownpenmodecommand():
    print("Unknown pen mode command. Type 'penhelp' for a list of pen mode commands.")
    pencmd()

def cmd():
    command = input()
    if command == "help":
        help()
    elif command == "exit":
        exit()
    elif command == "textshow":
        textshow()
    elif command == "penmode":
        penmode()
    else:
        unknowncommand()

startup()