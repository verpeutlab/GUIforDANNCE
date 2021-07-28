#necessary imports for this program
import tkinter as tk 
import threading
import imageio
from PIL import Image, ImageTk

#this code only has one video, which is labeled and captured below (change the pathway for your code)
video_name = "/Users/ishaan/Desktop/angles/angle1.mp4"
video = imageio.get_reader(video_name)

#necessary for tkinter prgrams 
root = tk.Tk()

#creates canvas/area to display information
canvas1 = tk.Canvas(root, width = 500, height = 400)
canvas1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
canvas1.create_window(100, 140, window=entry1)
canvas1.create_window(300, 140, window=entry2)

#start and end for frame numbers
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
            
#captures or gets the users entered frame numbers
def showNumber ():
    x1 = entry1.get()
    x2 = entry2.get()
#this code uses threading for the vide although there are other ways to stream the video 
    if __name__=="__main__":
        my_label = tk.Label(root)
        my_label.grid()
        thread = threading.Thread(target=stream,args=(my_label,x1,x2))
        thread.daemon = 1
        thread.start()

#creates play video button
button1 = tk.Button(text='Play Video', command=showNumber)
canvas1.create_window(100,180, window=button1)

#necessary to end tkinter program
root.mainloop()
