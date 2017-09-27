#!/Users/ksg/miniconda2/bin/python2.7
from os import path
from Tkinter import *
from os.path import basename
from tkFileDialog import askopenfilename
import speech_recognition as sr #pip install SpeechRecognition
import os
from transcriber import transcribe
import re


class PodSearch:
    
    filename = ""

    #Initialization
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


        #Browse button
        self.browseBtn = Button(frame, text="Browse", command=self.browse)
        self.browseBtn.pack(side=LEFT)

        #Quit button
        self.quitBtn = Button(frame, text="Quit", command=frame.quit)
        self.quitBtn.pack(side=LEFT)

        #Filepath label
        self.pathlabel = Label(master)
        self.pathlabel.pack()

        #Textbox
        self.searchEntry = Entry(master)
        self.searchEntry.pack()
        self.searchEntry.bind('<Return>', lambda _: self.search())

        #Search button
        self.searchBtn = Button(master, text="Search", command=self.search)
        self.searchBtn.pack()

        #Word label
        self.wordlabel = Label(master)
        self.wordlabel.pack()

        #Character label
        self.numberlabel = Label(master)
        self.numberlabel.pack()


    #Browse function
    def browse(self):
        #openfile dialog and put file in filename
        self.filename = askopenfilename()
        #show filename as label
        self.pathlabel.config(text=basename(self.filename))
        #Call transcribe
        tran = transcribe(self.filename)
        #self.signalWave(filename)

    #Search function
    def search(self):


        #Open transcription
        wavePath = basename(self.filename)    
        trans = wavePath.replace(".wav", ".txt")

        with open('transcribed/' + trans, 'r') as f:
            transcription=f.read().replace('\n ', '')

        keyword = self.searchEntry.get()
        
        

        #Split transcription into words
        words = transcription.split(' ')
        if keyword in words:
            pos = words.index(keyword)
        

        lines = transcription.find(keyword)
        
        print("Word number " + str(pos+1))
        print("Charachter number " + str(lines+1))

        #Write result to label
        self.wordlabel.config(text="Word number " + str(pos+1))
        self.numberlabel.config(text="Character number " + str(lines+1))







    # #Generate signal wave
    # def signalWave(self, filename):
    #     spf = wave.open(filename, 'r')
    #     #Extract raw audio from wav file
    #     signal = spf.readframes(-1)
    #     signal = np.fromstring(signal, 'Int16')
    #     #if stereo
    #     if spf.getnchannels() == 2:
    #         print 'Only momo files'
    #         sys.exit(0)

    #     plt.figure(1)
    #     plt.title('signal Wave...')
    #     plt.plot(signal)
    #     plt.show()


root = Tk()
b = PodSearch(root)
root.title("Podcast Searcher")
root.geometry("500x200+150+200")
root.mainloop()