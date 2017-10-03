#!/Users/ksg/miniconda2/bin/python2.7
'''This module is the GUI and some functions'''
from Tkinter import Tk, Button, Frame, Label, LEFT, Entry
from os.path import basename
from tkFileDialog import askopenfilename
from transcriber import transcribe


class PodSearch(object):
    '''This is the GUI class'''
    filename = ""

    # Initialization
    def __init__(self, master):
        '''Init of the GUI'''
        frame = Frame(master)
        frame.pack()

        # Browse button
        self.browsebtn = Button(frame, text="Browse", command=self.browse)
        self.browsebtn.pack(side=LEFT)

        # Quit button
        self.quitbtn = Button(frame, text="Quit", command=frame.quit)
        self.quitbtn.pack(side=LEFT)

        # Filepath label
        self.pathlabel = Label(master)
        self.pathlabel.pack()

        # Textbox
        self.searchentry = Entry(master)
        self.searchentry.pack()
        self.searchentry.bind('<Return>', lambda _: self.search())

        # Search button
        self.searchbtn = Button(master, text="Search", command=self.search)
        self.searchbtn.pack()

        # Word label
        self.wordlabel = Label(master)
        self.wordlabel.pack()

        # Timestamp label
        self.timestamplabel = Label(master)
        self.timestamplabel.pack()

    # Browse function
    def browse(self):
        '''browse for file'''
        self.filename = askopenfilename()  # openfile dialog and put file in filename
        self.pathlabel.config(text=basename(self.filename)
                              )  # show filename as label
        transcribe(self.filename)  # Call transcribe

    # Search function
    def search(self):
        '''Search in transcription'''
        # Open transcription
        wavepath = basename(self.filename)
        trans = wavepath.replace(".wav", ".txt")

        if not trans == '':
            if not self.searchentry.get() == '':
                with open('transcribed/' + trans, 'r') as fn:  # Open transcribed file
                    transcription = fn.read().replace('\n', '')

                keyword = self.searchentry.get()  # Get entry from textbox
                # Split transcription into words
                words = transcription.split(' ')

                # Find number of word
                counter = 0
                wordlabel = "Word number"
                timestamplabel = ""
                for i, _ in enumerate(words):
                    if _ == "--":
                        counter = counter + 1
                    if keyword.lower() in _.lower():
                        wordpos = i + 1
                        wordlabel += " " + str(wordpos) + ","
                        timestamplabel += self.spotter(counter)

                # Write result to label
                if wordlabel != "Word number":
                    self.wordlabel.config(text=wordlabel)

                    self.timestamplabel.config(text=timestamplabel)
                else:
                    self.wordlabel.config(text="Word not found")
            else:
                self.wordlabel.config(text="Enter word in search field")

        else:
            self.wordlabel.config(text="No file selected")

    def spotter(self, counter):
        '''Where in audio is result'''
        seconds1 = (counter - 1) * 12  # Calc interval start
        m, s = divmod(seconds1, 60)  # Format to hh:mm:ss
        h, m = divmod(m, 60)
        time1 = "%d:%02d:%02d" % (h, m, s)

        seconds2 = (counter - 1) * 12 + 14  # Calc interval end
        m, s = divmod(seconds2, 60)  # Format to hh:mm:ss
        h, m = divmod(m, 60)
        time2 = "%d:%02d:%02d" % (h, m, s)

        timestamp = time1 + " - " + time2 + ", "
        return timestamp


root = Tk()
b = PodSearch(root)
root.title("Podcast Searcher")
root.geometry("500x200+150+200")
root.mainloop()
