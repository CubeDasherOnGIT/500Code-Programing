import turtle as pen
t = pen.Turtle()
import time as waittime
import webbrowser as browser
import os as download
from os.path import join
import sys

def startup():
    pen.speed(1)
    t.speed(1)
    pen.bgcolor("black")
    print("500 Coding Language")
    print("Made Intirely In Python")
    print("Created By: CubeDasherGD")
    global is_pen_mode; is_pen_mode = False
    global is_normal_mode; is_normal_mode = True
    cmd()

def help():
    if is_pen_mode == True:
        print("You are currently in pen mode. Type 'normalmode' to exit pen mode and access normal commands.")
    else:
        browser.open("https://cubedasherongit.github.io/500Code-Programing/help/basichelp.html/")

def exit_program():
    print("Exiting...")
    waittime.sleep(1)
    sys.exit()

def penmode():
    global is_pen_mode, is_normal_mode
    if is_pen_mode == True:
        print("You are currently in pen mode. Type 'normalmode' to exit pen mode and access normal commands.")
    else:
        print("Entering pen mode...")
        waittime.sleep(1)
        is_pen_mode = True
        is_normal_mode = False
        print("Pen mode activated. Normal commands are disabled. Type 'normalmode' to exit pen mode.")
        pencmd()

def normalmode():
    global is_pen_mode, is_normal_mode
    if is_normal_mode == True:
        print("You are currently in normal mode. Type 'penmode' to enter pen mode and access pen mode commands.")
    else:
        print("Exiting pen mode...")
        waittime.sleep(1)
        is_pen_mode = False
        is_normal_mode = True
        cmd()

def pencmd():
    while True:
        pencommand = input("PEN> ")
        if pencommand == "penhelp":
            penhelp()
        elif pencommand == "textshow":
            textshow()
        elif pencommand == "pendown":
            pendown()
        elif pencommand == "penup":
            penup()
        elif pencommand == "exit":
            exit_program()
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
            break
        else:
            unknownpenmodecommand()

def penhelp():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        browser.open("https://cubedasherongit.github.io/500Code-Programing/help/penhelp.html/")

def pendown():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        t.pendown()

def penup():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        t.penup()

def penforward():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        print("How many pixels do you want to move forward?")
        pixels = int(input())
        t.forward(pixels)

def penbackward():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        print("How many pixels do you want to move backward?")
        pixels = int(input())
        t.backward(pixels)

def penleft():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        print("How many degrees do you want to turn left?")
        degrees = int(input())
        t.left(degrees)

def penright():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        print("How many degrees do you want to turn right?")
        degrees = int(input())
        t.right(degrees)

def pencolor():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        print("What color do you want to set the pen to?")
        color = input()
        t.color(color)

def pensize():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        print("What size do you want to set the pen to?")
        size = int(input())
        t.pensize(size)

def bgcolor():
    if is_pen_mode == False:
        print("Pen mode is not activated. Type 'penmode' to enter pen mode.")
    else:
        print("What color do you want to set the background to?")
        color = input()
        pen.bgcolor(color)

def textshow():
    if is_pen_mode == True:
        print("What text do you want to show?")
        text = input()
        t.write(text, font=("Arial", 16, "normal"))
    else:
        print("What text do you want to show?")
        text = input()
        print(text)

def dwld():
    folderpath = input("Enter folder path: ")
    fileend = ".FiveHundred.py"
    filestart = input("Enter file name: ")
    filename = filestart + fileend
    file_path = join(folderpath, filename)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write("#This Is A FiveHundred Code File. You Can Run The File In Python To Run The Code Written In The File\n")
        file.write("#DONT CHANGE OR DELETE THESE LINES OR THE CODE MAY NOT WORK AS INTENDED\n")
        file.write("import turtle as pen\n")
        file.write("t = pen.Turtle()\n")
        file.write("import time as waittime\n")
        file.write("import webbrowser as browser\n")
        file.write("import os\n")
        file.write("from os.path import join\n")
        file.write("def exit():\n")
        file.write("   exit()\n")
        file.write("\n")
        file.write("#SAFE TO EDIT FROM DOWN HERE\n")
        file.write("#EXAMPLE: TYPE 'print(\"Test\")' FOR DISPLAYING TEXT\n")
        file.write("\n")
        file.write("\n")

def unknowncommand():
    print("Unknown command. Type 'help' for a list of commands.")

def unknownpenmodecommand():
    print("Unknown pen mode command. Type 'penhelp' for a list of pen mode commands.")

def cmd():
    while True:
        command = input("CMD> ")
        if command == "help":
            help()
        elif command == "exit":
            exit_program()
        elif command == "textshow":
            textshow()
        elif command == "download":
            dwld()
        elif command == "penmode":
            penmode()
            break
        else:
            unknowncommand()

startup()
