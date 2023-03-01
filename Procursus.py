# Procursus Bootstrapping Tool
# by Hephaestus Team
# THIS TOOL IS NOT AFFILIATED WITH THE PROCURSUS TEAM IN ANYWAY
# probably built by PyInstaller module
# uwu

import os
import time
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
from PIL import ImageTk, Image
from applescript import tell
import webbrowser



root = tk.Tk()
canvas = Canvas()
frame = tk.Frame(root, width="475", height="120")
frame.pack(fill=BOTH,expand=True)



root.iconphoto(False, tk.PhotoImage(file='/Applications/Procursus.app/Contents/Resources/logo.png'))



LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""
JBROOTLESS2 = "/Applications/Procursus.app/Contents/Resources/jb.sh"
RESTOREROOTLESS2 = "/Applications/Procursus.app/Contents/Resources/rfs.sh"

root.title('Procursus Bootstrapper')
frame.pack()

def dependencies():

    root.iconphoto(False, tk.PhotoImage(file='/Applications/Procursus.app/Contents/Resources/logo.png'))
    messagebox.showinfo("Procursus Bootstrapper", "NOTE: The dependencies named in dependencies.txt (now on your desktop)\nshould ideally be installed using MacPorts (download link for installer in the text file too).")
    
    os.system("cp /Applications/Procursus.app/Contents/Resources/dependencies.txt /Users/$USER/Desktop/dependencies.txt")

mainText = Label(root, text="Procursus Bootstrapper",font=('Helveticabold', 24))
mainText.place(x=10, y=5)

cButton1 = tk.Button(frame,
                   text="Restore FS",
                   command=lambda: (tell.app( 'Terminal', 'do script "' + RESTOREROOTLESS2 + '"') , tell.app("Terminal", "activate")),
                   state="normal")
cButton1.place(x=10, y=55)

cButton2 = tk.Button(frame,
                   text="Bootstrap",
                   command=lambda: (tell.app( 'Terminal', 'do script "' + JBROOTLESS2 + '"') , tell.app("Terminal", "activate")),
                   state="normal")
cButton2.place(x=120, y=55)

cButton2 = tk.Button(frame,
                   text="Dependencies",
                   command=dependencies,
                   state="normal")
cButton2.place(x=225, y=55)

img2 = Image.open("/Applications/Procursus.app/Contents/Resources/logo.png")
NewIMGSize2 = img2.resize((100,100))
new_image2 = ImageTk.PhotoImage(NewIMGSize2)
label = Label(frame, image = new_image2)
label.place(x=360, y=5)


root.geometry("475x120")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')

root.mainloop()

