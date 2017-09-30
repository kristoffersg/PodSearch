#!/Users/ksg/miniconda2/bin/python2.7
from Tkinter import Tk, Button, Frame, Label, LEFT, Entry
from os.path import basename
from tkFileDialog import askopenfilename
from transcriber import transcribe

class PodSearch(object):    
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
        self.filename = askopenfilename()                           #openfile dialog and put file in filename
        self.pathlabel.config(text=basename(self.filename))         #show filename as label
        transcribe(self.filename)                                   #Call transcribe
        self.numberlabel.config(text="")                            #Clears "No file selected" label

    #Search function
    def search(self):
        #Open transcription
        wavePath = basename(self.filename)    
        trans = wavePath.replace(".wav", ".txt")

        if not trans == '':
            if not self.searchEntry.get() == '':
                with open('transcribed/' + trans, 'r') as f:                #Open transcribed file
                    transcription = f.read().replace('\n ', '')

                keyword = self.searchEntry.get()                            #Get entry from textbox
                words = transcription.split(' ')                            #Split transcription into words

                #Find number of character
                charLabel = "Character number "
                for i, _ in enumerate(transcription):
                    if transcription[i:i + len(keyword)] == keyword:
                        charPos = i+1
                        charLabel += " " + str(charPos) + ","

                #Find number of word
                wordLabel = " Word number"
                for i, _ in enumerate(words):
                    if keyword in _:
                        wordPos = i+1
                        wordLabel += " " + str(wordPos) + ","

                #Write result to label
                self.wordlabel.config(text=wordLabel)
                self.numberlabel.config(text=charLabel)
            else:
                self.numberlabel.config(text="Enter word in search field")

        else:
            self.numberlabel.config(text="No file selected")


root = Tk()
b = PodSearch(root)
root.title("Podcast Searcher")
root.geometry("500x200+150+200")
root.mainloop()
