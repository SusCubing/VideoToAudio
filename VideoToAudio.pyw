import tkinter as tk
import os as os
import os.path
import subprocess
from tkinter import filedialog as fd
from PIL import Image, ImageTk
root = tk.Tk()

root.title('Video to Audio Converter')
root.geometry('400x150+300+300')
root.resizable(False,False)
root.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('icon.png')))
w = tk.Label(root,text="")

def convert_video():
    global w
    w.destroy()
    filetypes = (
        ('MP4 files','*.mp4'),
        ('AVI files','*.avi')
    )
    filename = fd.askopenfilename(
        title='Open Video',
        initialdir='/',
        filetypes=filetypes
    )
    if os.path.isfile("ffmpeg.exe"):
        ffmpegcommand = "ffmpeg -i \""+filename+"\" -nostdin -y \""+filename+".mp3\""
        
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.call(ffmpegcommand, startupinfo=si)
        
        w = tk.Label(root,text="Success")
    else:
        w = tk.Label(root,text="Error: ffmpeg.exe not found")
    w.place(relx=0.5,rely=0.7,anchor='center')

tk.Label(root,text="Convert a video to audio").place(relx=0.5,rely=0.3,anchor='center')
tk.Button(root,text='Select Video',command=convert_video).place(relx=0.5,rely=0.5,anchor='center')

root.mainloop()