#!/Users/ksg/miniconda2/bin/python2.7
from os import path
from Tkinter import *
from os.path import basename
from tkFileDialog import askopenfilename
import speech_recognition as sr #pip install SpeechRecognition
import os
#import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


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


    #Browse function
    def browse(self):
        #openfile dialog and put file in filename
        filename = askopenfilename()
        #show filename as label
        self.pathlabel.config(text=basename(filename))
        #Call transcribe
        self.transcribe(filename)
        self.signalWave(filename)


    #Transcribe selected file
    def transcribe(self, filename):
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)
        
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
        transcription = r.recognize_google(audio)
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`

            #Create file and write the transscription into it
            text_file = open(basename(os.path.splitext(filename)[0]) + ".txt", "w")
            text_file.write(transcription)
            text_file.close()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #Generate signal wave
    def signalWave(self, filename):
        print("0")
        spf = wave.open(filename, 'r')
        print("1")
        #Extract raw audio from wav file
        signal = spf.readframes(-1)
        print("2")
        signal = np.fromstring(signal, 'Int16')
        print("3")
        #if stereo
        if spf.getnchannels() == 2:
            print 'Only momo files'
            sys.exit(0)

        print("4")
        plt.figure(1)
        plt.title('signal Wave...')
        plt.plot(signal)
        plt.show()


root = Tk()
b = PodSearch(root)
root.title("Podcast Searcher")
root.geometry("500x200+150+200")
root.mainloop()