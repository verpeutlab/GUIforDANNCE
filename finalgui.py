#all the import functions necessary for thus code
import tkinter as tk
import threading
import imageio
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
from tkinter import ttk
import scipy
from scipy.io import loadmat

#loads the data into terminal/console (depending on ide)
annots = loadmat('/Users/ishaan/Desktop/angles/test.mat')
print(annots)

#defines and captures the first vide angle
video_name = "/Users/ishaan/Desktop/angles/angle1.mp4"
video = imageio.get_reader(video_name)

#this line is necessary for tkinter to function in general 
root = tk.Tk()

#creates an actual place to display the different functions
canvas1 = tk.Canvas(root, width=600, height=600)
#a pack or a grid function is necessary to input whatever function you want into the code (it places it down into the code)
canvas1.pack()

#creates entry boxes for starting point and ending point for frame numbers (the root refers back upto the tkinter function)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

canvas1.create_window(100, 140, window=entry1)
canvas1.create_window(300, 140, window=entry2)
label1 = tk.Label(root, text='Frame From')
canvas1.create_window(100, 100, window=label1)
label2 = tk.Label(root, text='Frame To')
canvas1.create_window(300, 100, window=label2)

my_label = tk.Label(root)
my_label.pack(side="left")


#necessary for streaming the video and displaying it 
def stream(label, x1, x2):
    video_name = video_cb.get()

    video = imageio.get_reader(video_name)
    frame = int(x1)
    frameto = int(x2)
    fcount = 0
    for image in video.iter_data():
        fcount = fcount + 1
        if fcount >= frame and fcount <= frameto:
            image_frame = Image.fromarray(image)
            image_frame = image_frame.resize((400, 400), Image.ANTIALIAS)
            frame_image = ImageTk.PhotoImage(image_frame, "right")
            label.config(image=frame_image)
            label.image = frame_image

#captures or gets number from the user input to display 
def showNumber():
    x1 = entry1.get()
    x2 = entry2.get()
    if __name__ == "__main__":
        thread = threading.Thread(target=stream, args=(my_label, x1, x2))
        thread.daemon = 1
        thread.start()

#additional button to play video (necessary if you want to continuously look at different frames without loading the program again)
button1 = tk.Button(text='Play Video', command=showNumber, height='3', width='20')
canvas1.create_window(58, 200, window=button1)

#allows you to change frames and video 
def video_changed(event):
    msg = f'You selected {video_cb.get()}!'
    video_name = video_cb.get()

#placing the dif videos into na dropdown box 
video_angels = ('/Users/ishaan/Desktop/angles/angle1.mp4', '/Users/ishaan/Desktop/angles/angle2.mp4'
                , '/Users/ishaan/Desktop/angles/angle3.mp4', '/Users/ishaan/Desktop/angles/angle4.mp4'
                , '/Users/ishaan/Desktop/angles/angle5.mp4', ' /Users/ishaan/Desktop/angles/angle6.mp4')
selected_video = tk.StringVar()
video_cb = ttk.Combobox(root, textvariable=selected_video)
video_cb['values'] = video_angels
canvas1.create_window(100, 50, window=video_cb)
video_cb.bind('<<ComboboxSelected>>', video_changed)

#refers back to line 20 and is a necessary function to end the tkinter program and the program overall
root.mainloop()
