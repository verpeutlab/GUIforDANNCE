from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Drop Down Box')


def comboclick():
    myLabel = Label(root, text=myCombo.get())
    myLabel.grid(row=0, column=50)

def selected(event):
    myLabel = Label(root, text=clicked.get())
    myLabel.grid(row =50, column=0)

options = [
    "Camera 1",
    "Camera 2",
    "Camera 3",
    "Camera 4",
    "Camera 5",
    "Camera 6",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.grid(row=0, column=0)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo

import tkinter as tk 
import threading
import imageio
from PIL import Image, ImageTk

video_name = "/Users/ishaan/Desktop/angles/angle1.mp4"
video = imageio.get_reader(video_name)

canvas1 = tk.Canvas(root, width = 500, height = 400)
canvas1.grid(row=500, column=9900)   

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
canvas1.create_window(100, 140, window=entry1)
canvas1.create_window(300, 140, window=entry2)

def stream(label,x1,x2):

    framef = int(x1)
    framet = int(x2)
    frame = framef
    for image in video.iter_data():
        frame = frame + 1
        image_frame = Image.fromarray(image)
        frame_image = ImageTk.PhotoImage(image_frame)
        label.config(image=frame_image)
        label.image = frame_image
        if frame == framet: break

def showNumber ():
    x1 = entry1.get()
    x2 = entry2.get()

    if __name__=="__main__":
        my_label = tk.Label(root)
        my_label.grid(row=180, column=100)
        thread = threading.Thread(target=stream,args=(my_label,x1,x2))
        thread.daemon = 1
        thread.start()

button1 = tk.Button(text='Play Video', command=showNumber)
canvas1.create_window(100,180, window=button1)

root.title('DANNCE GUI')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()

c =Checkbutton(root, text="Left Ear", variable=var1)
c.grid(row=600, column=0)
c =Checkbutton(root, text="Right Ear", variable=var2)
c.grid(row=650, column=0)
c =Checkbutton(root, text="Snout", variable=var3)
c.grid(row=700, column=0)
c =Checkbutton(root, text="Spine F", variable=var4)
c.grid(row=750, column=0)
c =Checkbutton(root, text="Spine M", variable=var5)
c.grid(row=800, column=0)
c =Checkbutton(root, text="Tail Base", variable=var6)
c.grid(row=850, column=0)
c =Checkbutton(root, text="Tail Mid", variable=var7)
c.grid(row=900, column=0)
c =Checkbutton(root, text="Tail End", variable=var8)
c.grid(row=950, column=0)
c =Checkbutton(root, text="Left Firepaw", variable=var9)
c.grid(row=1000, column=0)
c =Checkbutton(root, text="Left Wrist", variable=var10)
c.grid(row=1050, column=0)
c =Checkbutton(root, text="Left Elbow", variable=var11)
c.grid(row=1100, column=0)
c =Checkbutton(root, text="Left Shoulder", variable=var12)
c.grid(row=600, column=100)
c =Checkbutton(root, text="Right Forepaw", variable=var13)
c.grid(row=650, column=100)
c =Checkbutton(root, text="Right Wrist", variable=var14)
c.grid(row=700, column=100)
c =Checkbutton(root, text="Right Elbow", variable=var15)
c.grid(row=750, column=100)
c =Checkbutton(root, text="Right Shoulder", variable=var16)
c.grid(row=800, column=100)
c =Checkbutton(root, text="Left Hindpaw", variable=var17)
c.grid(row=850, column=100)
c =Checkbutton(root, text="Left Ankle", variable=var18)
c.grid(row=900, column=100)
c =Checkbutton(root, text="Left Knee", variable=var19)
c.grid(row=950, column=100)
c =Checkbutton(root, text="Right Hindpaw", variable=var20)
c.grid(row=1000, column=100)
c =Checkbutton(root, text="Right Ankle", variable=var21)
c.grid(row=1050, column=100)
c =Checkbutton(root, text="Right Knee", variable=var22)
c.grid(row=1100, column=100)

root.mainloop()
