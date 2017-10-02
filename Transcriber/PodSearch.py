#!/Users/ksg/miniconda2/bin/python2.7
'''This module is the GUI and some functions'''
from Tkinter import Tk, Button, Frame, Label, LEFT, Entry
from os.path import basename
from tkFileDialog import askopenfilename
from transcriber import transcribe

class PodSearch(object):
    '''This is the GUI class'''
    filename = ""

    #Initialization
    def __init__(self, master):
        '''Init of the GUI'''
        frame = Frame(master)
        frame.pack()

        #Browse button
        self.browsebtn = Button(frame, text="Browse", command=self.browse)
        self.browsebtn.pack(side=LEFT)

        #Quit button
        self.quitbtn = Button(frame, text="Quit", command=frame.quit)
        self.quitbtn.pack(side=LEFT)

        #Filepath label
        self.pathlabel = Label(master)
        self.pathlabel.pack()

        #Textbox
        self.searchentry = Entry(master)
        self.searchentry.pack()
        self.searchentry.bind('<Return>', lambda _: self.search())

        #Search button
        self.searchbtn = Button(master, text="Search", command=self.search)
        self.searchbtn.pack()

        #Word label
        self.wordlabel = Label(master)
        self.wordlabel.pack()

        #Character label
        self.numberlabel = Label(master)
        self.numberlabel.pack()

    #Browse function
    def browse(self):
        '''browse for file'''
        self.filename = askopenfilename()                  #openfile dialog and put file in filename
        self.pathlabel.config(text=basename(self.filename)) #show filename as label
        transcribe(self.filename)                          #Call transcribe
        self.numberlabel.config(text="")                   #Clears "No file selected" label

    #Search function
    def search(self):
        '''Search in transcription'''
        #Open transcription
        wavepath = basename(self.filename)
        trans = wavepath.replace(".wav", ".txt")

        if not trans == '':
            if not self.searchentry.get() == '':
                with open('transcribed/' + trans, 'r') as fn:        #Open transcribed file
                    transcription = fn.read().replace('\n ', '')

                keyword = self.searchentry.get()                    #Get entry from textbox
                words = transcription.split(' ')                    #Split transcription into words

                #Find number of character
                charlabel = "Character number"
                for i, _ in enumerate(transcription):
                    if transcription[i:i + len(keyword)].lower() == keyword.lower():
                        charpos = i+1
                        charlabel += " " + str(charpos) + ","

                #Find number of word
                wordlabel = "Word number"
                for i, _ in enumerate(words):
                    if keyword.lower() in _.lower():
                        wordpos = i+1
                        wordlabel += " " + str(wordpos) + ","

                #Write result to label
                if wordlabel != "Word number":
                    self.wordlabel.config(text=wordlabel)
                    self.numberlabel.config(text=charlabel)
                else:
                    self.wordlabel.config(text="")
                    self.numberlabel.config(text="Word not found")
            else:
                self.numberlabel.config(text="Enter word in search field")

        else:
            self.numberlabel.config(text="No file selected")


root = Tk()
b = PodSearch(root)
root.title("Podcast Searcher")
root.geometry("500x200+150+200")
root.mainloop()
