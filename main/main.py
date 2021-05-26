#!/bin/env python
from red import red
from blue import blue
from yellow import yellow
from custom import custom
from treshold import treshold
from video import run as video
from cam import run as cam

def banner():
    print("""
     ▄████▄     ▓█████▄ ▓█████▄▄▄█████▓▓█████ ▄████▄  ▄▄▄█████▓
     ▒██▀ ▀█     ▒██▀ ██▌▓█   ▀▓  ██▒ ▓▒▓█   ▀▒██▀ ▀█  ▓  ██▒ ▓▒
     ▒▓█    ▄    ░██   █▌▒███  ▒ ▓██░ ▒░▒███  ▒▓█    ▄ ▒ ▓██░ ▒░
     ▒▓▓▄ ▄██▒   ░▓█▄   ▌▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄▒▓▓▄ ▄██▒░ ▓██▓ ░ 
     ▒ ▓███▀ ░   ░▒████▓ ░▒████▒ ▒██▒ ░ ░▒████▒ ▓███▀ ░  ▒██▒ ░ 
     ░ ░▒ ▒  ░    ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░   ░░ ▒░ ░ ░▒ ▒  ░  ▒ ░░   
       ░  ▒       ░ ▒  ▒  ░ ░  ░   ░     ░ ░  ░ ░  ▒       ░    
       ░            ░ ░  ░    ░    ░         ░  ░          ░      
       ░ ░            ░       ░  ░           ░  ░ ░               
       ░            ░                           ░                 
""")

def menu():
    print("""
    1. Red 
    2. Green
    3. Blue
    4. Yellow
    5. Custom
    6. Find your own value
    7. Load Video
    8. Load your cam
    """)
    uInput = int(input("Choose an option: "))
    if(uInput == 1):
        imageInput = input("Path to image: ")
        red(imageInput.strip())
    elif(uInput == 2):
        imageInput = input("Path to image: ")
        green(imageInput.strip())
    elif(uInput == 3):
        imageInput = input("Path to image: ")
        blue(imageInput.strip())
    elif(uInput == 4):
        imageInput = input("Path to image: ")
        yellow(imageInput.strip())
    elif(uInput == 5):
        imageInput = input("Path to image: ")
        hMin = int(input("Enter H minimum: "))
        sMin = int(input("Enter S minimum: "))
        vMin = int(input("Enter V minimum: "))
        hMax = int(input("Enter H maximum: "))
        sMax = int(input("Enter S maximum: "))
        vMax = int(input("Enter V maximum: "))
        lower = [hMin,sMin,vMin]
        higher = [hMax,sMax,vMax]
        custom(imageInput.strip(),lower,higher)
    elif(uInput == 6):
        imageInput = input("Path to image: ")
        treshold(imageInput.strip())
    elif(uInput == 7):
        imageInput = input("Path to video: ")
        video(imageInput.strip())
    elif(uInput == 8):
        cam()
    

if __name__ == "__main__":
    banner()
    menu()
    
