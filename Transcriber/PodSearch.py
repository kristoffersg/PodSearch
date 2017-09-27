#!/Users/ksg/miniconda2/bin/python2.7
from os import path
from Tkinter import *
from os.path import basename
from tkFileDialog import askopenfilename
import speech_recognition as sr #pip install SpeechRecognition
import os
from transcriber import transcribe


class PodSearch:
    
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

        #Search button
        self.searchBtn = Button(master, text="Search", command=self.search)
        self.searchBtn.pack()


    #Browse function
    def browse(self):
        #openfile dialog and put file in filename
        filename = askopenfilename()
        #show filename as label
        self.pathlabel.config(text=basename(filename))
        #Call transcribe
        tran = transcribe(filename)
        #self.signalWave(filename)

    #Search function
    def search(filename):
        f = open(filename)







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