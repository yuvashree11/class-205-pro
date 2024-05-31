import platform
import socket
from tkinter import *
from  threading import Thread
import random
from tkinter import ttk
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None
playerName = None

canvas1 = None

nameEntry = None
gameWindow = None
ticketGrid = []
currentNumberList = []
nameWindow = None
canvas2 = None 
screen_width = None
screen_height = None
winingMessage = None
resetButton = None
canvas1 = None

def createTicket():
    global gameWindow
    global ticketGrid

    mainLable = Label(gameWindow, width=65,height=16,relief='ridge',borderwidth=5,bg='white')
    mainLable.place(x=95,y=119)

    xpos = 105
    ypos = 130
    for row in range(0,3):
        rowList = []
        for col in range(0,9):
            if(platform.system() == 'Darwin'):

                boxButton = Button (gameWindow,
                font = ("Chalkboard SE",18),
                borderwidth=3,
                pady=23,
                padx = -22,
                bg = "#fff176",
                highlightbackground='#fff176',activebackground='#c5ela5')

                boxButton.place(x=xpos,y=ypos)

            else:
                boxButton = Tk.Button(gameWindow,font = ("Chalkboard SE",30),width=3, height=2 ,border=5,bg = "#fff176")
                boxButton.place(x=xpos,y=ypos)

            rowList.append(boxButton)
            xpos += 64

        ticketGrid.append(rowList)
        xpos = 105
        ypos += 82






def placeNumber():
    global ticketGrid 
    global currentNumberList

    for row in range (0.3):
        randomCollList = []
        counter = 0 

        while counter <= 4:
            randomCol = random.randint(0,8)
            if (randomCol not in randomCollList):
                randomCollList.append(randomCol)
                counter+=1

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())
    gameWindow()
    



def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow  = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.geometry('800x600')


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/4.5,screen_height/8, text = "Enter Name", font=("Chalkboard SE",60), fill="black")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 30), bd=5, bg='white')
    nameEntry.place(x = screen_width/7, y=screen_height/5.5 )


    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=11, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/6, y=screen_height/4)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def gameWindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global ticketGrid
    global winingMessage
    global resetButton


    gameWindow = Tk()
    gameWindow.title("Tambola")
    gameWindow.attributes('-fullscreen',True)
    
    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas2 = Canvas( gameWindow, width = 2500,height = 2500)
    canvas2.pack(fill = "both", expand = True)

    # Display image
    canvas2.create_image( 0, 0, image = bg, anchor = "nw")

    # Add Text
    canvas2.create_text( screen_width/2, screen_height/10, text = "Tambola", font=("Chalkboard SE",100),fill="white" )
    createTicket()
    placeNumber()
    gameWindow.mainloop()
    gameWindow.resizeable(True,True)

    # ------------ Boilerplate Code

    # Declaring Wining Message
    winingMessage = canvas2.create_text(screen_width/2 + 10, screen_height/2 + 250, text = "", font=("Chalkboard SE",100), fill='#fff176')

    # Creating Reset Button
    resetButton =  Button(gameWindow,text="Reset Game", fg='black', font=("Chalkboard SE", 15), bg="grey",command=restGame, width=20, height=5)

    # ------------ Boilerplate End

def restGame():
    global SERVER
    SERVER.send("reset game".encode())



def recivedMsg():
    global gameWindow
    global ticketGrid
    pass



def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=recivedMsg)
    thread.start()

    askPlayerName()


setup()
