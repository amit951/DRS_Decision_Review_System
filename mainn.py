import tkinter #inbuilt package
import PIL.Image, PIL.ImageTk
import cv2
import numpy 
from functools import partial
import threading
import imutils 
import time
stream=cv2.VideoCapture("clip.mkv")

def play(speed):
    print(f"You clicked play, Speed is {speed}. ")

    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed, frame =stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    canvas.create_text(120,25,fill="White", font="Times 20 italic bold", text="Decision Pending")


def pending(decision):
    #display decision pending img
    frame=cv2.cvtColor(cv2.imread("decisionpending.JPG"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    
    #wait 1 sec
    time.sleep(1)

    #display sponsor img
    frame=cv2.cvtColor(cv2.imread("sponsor.JPG"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #wait 1 sec
    time.sleep(1.5)

    #display out/notout
    if decision=="out":
        decisionimg="out.JPG"
    else:
        decisionimg="notout.JPG"
    frame=cv2.cvtColor(cv2.imread(decisionimg),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


def out():
    thread=threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start()
    print("Player is out")  

def not_out():
    thread=threading.Thread(target=pending,args=("Not out",))
    thread.daemon=1
    thread.start()
    print("Player is not out")

SET_WIDTH=1000
SET_HEIGHT=500

window=tkinter.Tk()
window.title("Third Umpire DRS System")
cv_img=cv2.cvtColor(cv2.imread("home.JPG"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()

btn=tkinter.Button(window,text="<< Previous fast", width=60, command=partial(play,-10))
btn.pack()

btn=tkinter.Button(window,text="<< Previous slow", width=60, command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="Next slow >>", width=60, command=partial(play,+2))
btn.pack()

btn=tkinter.Button(window,text="Next fast >>", width=60, command=partial(play,+10))
btn.pack()

btn=tkinter.Button(window,text="Give Out", width=60, command=out)
btn.pack()

btn=tkinter.Button(window,text="Give Not Out", width=60, command=not_out)
btn.pack()

window.mainloop()




