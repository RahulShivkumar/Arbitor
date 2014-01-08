from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
import os
import hashlib
import urllib2
import Tkinter

#Setup Tkinter root
root = Tkinter.Tk()

#Function called when button is clicked
def fileUpload(message):
    Tk().withdraw()
    path = askopenfilename()
    downloadSubTitle(path, message)

#Given hash function for The SubDB's API
def hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

#Function that actually downloads the subtitle file and handles errors
def downloadSubTitle(path, message):
    message.set('Searching.............')
    root.update_idletasks()
    #These are required extensions of movie files
    extension = ['.avi', '.mp4', '.mkv', '.mpg', '.mpeg', '.rmbv']
    completePath = path
    #Assume that the file is NOT in proper format
    properFormat = False

    for content in extension:
        #Strip path of its extension
        path = path.replace(content,'')

    #If path has been changed, then it had a proper extension
    if len(path) < len(completePath):
        properFormat = True

    #If the subtitle file is NOT present and if the file was in proper format, hash it and download the subtitle
    if not os.path.exists(path+'.srt') and properFormat:
        #hashing
        hashedParam = hash(completePath)
        #This is the required url and params for The SubDB's API
        params = { 'User-Agent' : 'SubDB/1.0 (Arbitor/1.0; http://github.com/RahulShivkumar/Arbitor)' }
        url = 'http://api.thesubdb.com/?action=download&hash='+hashedParam+'&language=en'
        req = urllib2.Request(url, '', params)

        #404 errors can be caught for when the subtitle file for given movie is NOT present
        try:
            res = urllib2.urlopen(req).read()
            subtitle = open (path+'.srt','wb')
            subtitle.write(res)
            message.set('Subtitle successfully downloaded!')
            root.update_idletasks()
        except urllib2.HTTPError, error:
            message.set('Subtitle could not be found.')
            root.update_idletasks()

    #Run proper messages if the file is invalid or if the subtitle file is already present.
    else:
        if not properFormat:
            message.set('Invalid File.')
            root.update_idletasks()
        else:
            message.set('Subtitle already present.')
            root.update_idletasks()

#Setup the basic root size and background
root.title('Arbitor')
root.geometry('400x200')
root.configure(background = '#ccc')

#message variable created for the textBox label
message = StringVar()
message.set('Welcome to Arbitor!')

#Style created for the 'flat' button
style = ttk.Style()
style.configure('TButton', relief = FLAT, padding = 6, background= '#ccc')

#textBox and button both created with respective params
textBox = Tkinter.Label(root, textvariable = message, bg = '#ccc')
button = ttk.Button(root, text = 'Choose File', command = lambda:fileUpload(message), style = 'TButton')

#textBox and button are both aligned
textBox.place(relx = 0.5, rely = 0.3, anchor = CENTER)
button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#Keeps the program running till it is physically quit
root.mainloop()





