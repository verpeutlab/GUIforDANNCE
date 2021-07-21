import tkinter as tk
import threading
import imageio
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
from tkinter import ttk
import scipy
from scipy.io import loadmat


annots = loadmat('/Users/ishaan/Desktop/angles/test.mat')
print(annots)

video_name = "/Users/ishaan/Desktop/angles/angle1.mp4"
video = imageio.get_reader(video_name)

root = tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=600)
canvas1.pack()

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


def showNumber():
    x1 = entry1.get()
    x2 = entry2.get()
    if __name__ == "__main__":
        thread = threading.Thread(target=stream, args=(my_label, x1, x2))
        thread.daemon = 1
        thread.start()


button1 = tk.Button(text='Play Video', command=showNumber, height='3', width='20')
canvas1.create_window(58, 200, window=button1)

def video_changed(event):
    msg = f'You selected {video_cb.get()}!'
    video_name = video_cb.get()


video_angels = ('/Users/ishaan/Desktop/angles/angle1.mp4', '/Users/ishaan/Desktop/angles/angle2.mp4'
                , '/Users/ishaan/Desktop/angles/angle3.mp4', '/Users/ishaan/Desktop/angles/angle4.mp4'
                , '/Users/ishaan/Desktop/angles/angle5.mp4', ' /Users/ishaan/Desktop/angles/angle6.mp4')
selected_video = tk.StringVar()
video_cb = ttk.Combobox(root, textvariable=selected_video)
video_cb['values'] = video_angels
canvas1.create_window(100, 50, window=video_cb)
video_cb.bind('<<ComboboxSelected>>', video_changed)

root.mainloop()
