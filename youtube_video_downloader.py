from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('700x400')
root.title('RJ YouTube Downloader')
root.iconbitmap(r'C:\Users\Rediet\Downloads\photo_2020-09-07_16-35-23.jpg')


Label_1=Label(root, text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=120, y=20)

mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140,y=80)
def downloadVideo():
    x=str(mylink.get())
    ytvideo= YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    ytvideo.download('./coursera py')
Button(root,text="Click Here to Download", width=20, bg='red', fg="white", command=downloadVideo).place(x=220, y=110)

root.mainloop()
