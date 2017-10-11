#!/Users/ksg/miniconda2/bin/python2.7
'''This module is the GUI and some functions'''
from Tkinter import Tk, Button, Frame, Label, LEFT, Entry
from os.path import basename
from tkFileDialog import askopenfilename
import ttk
from transcriber import transcribe
from worder import wordcloud_create
from stemmer import stemmer_func
from removeoverlap import removerlap

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

        # Working Label
        self.workinglabel = Label(master)
        self.workinglabel.pack()

        # Progress Bar
        self.pbar_det = ttk.Progressbar(
            orient="horizontal", length=400, mode="indeterminate")

    # Browse function
    def browse(self):
        '''browse for file'''
        if self.wordlabel != "":  # clear the labels if necessary
            self.wordlabel.config(text="")
            self.pathlabel.config(text="")
            self.timestamplabel.config(text="")
        self.filename = askopenfilename()  # openfile dialog and put file in filename
        if not self.filename:  # leave method if cancel is clicked
            return
        self.pathlabel.config(text=basename(self.filename))  # show filename as label
        if self.filename.endswith('.txt'):
            return
        self.workinglabel.config(text="WORKING", font=(
            "Helvetica", 20))  # Show WORKING when transcribing
        self.pbar_det.pack()  # show the progress bar
        self.pbar_det.start()  # Start the progress bar
        root.update()
        new_path = transcribe(self.filename)  # Call transcribe
        self.workinglabel.config(text="")  # remove working label

        wordcloud_create(self.filename)
        stemmer_func(new_path)

        self.pbar_det.stop()  # Stop progress bar
        self.pbar_det.pack_forget()  # Remove progress bar


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

                removerlap(words)

                # Find number of word
                counter = 0
                wordlabel = "Word number"
                timestamplabel = ""
                shift = 0
                for i, _ in enumerate(words):
                    if _ == "--":
                        counter = counter + 1
                        shift = i
                    if keyword.lower() in _.lower():
                        totalwordpos = i + 1
                        wpsplit = totalwordpos - shift
                        wordlabel += " " + str(wpsplit) + ","

                        timestamplabel += self.maptoaudio(counter)

                # Write result to label
                if wordlabel != "Word number":
                    self.wordlabel.config(text=wordlabel)

                    self.timestamplabel.config(text=timestamplabel)
                else:
                    self.wordlabel.config(text="Word not found")
                    self.timestamplabel.config(text="")
            else:
                self.wordlabel.config(text="Enter word in search field")

        else:
            self.wordlabel.config(text="No file selected")

    def maptoaudio(self, counter):
        '''Where in audio is result'''
        seconds1 = (counter - 1) * 12  # Calc interval start
        minutes, seconds = divmod(seconds1, 60)  # Format to hh:mm:ss
        hours, minutes = divmod(minutes, 60)
        time1 = "%d:%02d:%02d" % (hours, minutes, seconds)

        seconds2 = (counter - 1) * 12 + 14  # Calc interval end
        minutes, seconds = divmod(seconds2, 60)  # Format to hh:mm:ss
        hours, minutes = divmod(minutes, 60)
        time2 = "%d:%02d:%02d" % (hours, minutes, seconds)

        timestamp = time1 + " - " + time2 + ", "
        return timestamp


root = Tk()
b = PodSearch(root)
root.title("Podcast Searcher")
root.geometry("500x200+150+200")
root.mainloop()
