#!/Users/ksg/miniconda2/bin/python2.7
'''This module is the GUI and some functions'''
from Tkinter import Tk, Button, Frame, Label, LEFT, RIGHT, BOTTOM, TOP, BOTH, YES, Entry
from os.path import basename
from tkFileDialog import askopenfilename
import ttk
from transcriber import transcribe
from worder import wordcloud_create
from stemmer import stemmer_func
from PIL import ImageTk, Image
from removeoverlap import removerlap
from estimation import findword
from audioduration import *


class PodSearch(object):
    '''This is the GUI class'''

    # Initialization of variables
    filename = ""

    # Initialization of GUI
    def __init__(self, master):
        '''Init of the GUI'''
        # Frame for progress bar
        self.bottomframe = Frame(master, highlightbackground="green", highlightcolor="green",
                                 highlightthickness=1, width=500, height=200)
        self.bottomframe.pack(side=BOTTOM)

        # Frame for buttons and entry
        self.leftframe = Frame(master, highlightbackground="blue", highlightcolor="blue",
                               highlightthickness=1, width=400, height=400)
        self.leftframe.pack(side=LEFT)

        # Sub frame  for buttons
        self.leftsubframe_top = Frame(self.leftframe, highlightbackground="yellow",
                                      highlightcolor="yellow", highlightthickness=1)
        self.leftsubframe_top.pack(side=TOP)

        # Sub frame for entry
        self.leftsubframe_bot = Frame(self.leftframe, highlightbackground="purple",
                                      highlightcolor="purple", highlightthickness=1)
        self.leftsubframe_bot.pack(side=BOTTOM)

        # Frame for wordcloud
        rightframe = Frame(master, highlightbackground="red", highlightcolor="red",
                           highlightthickness=1, width=250, height=250)
        rightframe.pack(side=RIGHT)


        # Browse button
        self.browsebtn = Button(self.leftsubframe_top, text="Browse", command=self.browse)
        self.browsebtn.pack(side=LEFT)

        # Quit button
        self.quitbtn = Button(self.leftsubframe_top, text="Quit", command=self.leftframe.quit)
        self.quitbtn.pack(side=LEFT)

        # Filepath label
        self.pathlabel = Label(self.leftsubframe_bot, text="filename")
        self.pathlabel.pack()

        # Textbox
        self.searchentry = Entry(self.leftsubframe_bot)
        self.searchentry.pack()
        self.searchentry.bind('<Return>', lambda _: self.search())

        # Search button
        self.searchbtn = Button(self.leftsubframe_bot, text="Search", command=self.search)
        self.searchbtn.pack()

        # Word label
        self.wordlabel = Label(self.bottomframe)
        self.wordlabel.pack()

        # Timestamp label
        self.timestamplabel = Label(self.bottomframe)
        self.timestamplabel.pack()

        # estimate label
        self.estimatelabel = Label(self.bottomframe)
        self.estimatelabel.pack()

        # Working Label
        self.workinglabel = Label(self.bottomframe)
        self.workinglabel.pack()

        # Progress Bar
        self.pbar_det = ttk.Progressbar(self.bottomframe, orient="horizontal", length=400,
                                        mode="indeterminate")

        # Wordcloud preparation
        self.imagefile = "wordcloudTools/black_background.png"
        self.imagefile = Image.open(self.imagefile)
        self.image1 = self.imagefile.resize((400, 400), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.image1)

        self.panel1 = Label(rightframe, image=self.image1)
        self.display = self.image1
        self.panel1.pack(side=TOP, fill=BOTH, expand=YES)

        self.duration = 0



    # Browse function
    def browse(self):
        '''browse for file'''
        if self.wordlabel != "":  # clear the labels if necessary
            self.wordlabel.config(text="")
            self.pathlabel.config(text="")
            self.timestamplabel.config(text="")
            self.estimatelabel.config(text="")
        self.filename = askopenfilename()  # openfile dialog and put file in filename
        if not self.filename:  # leave method if cancel is clicked
            return
        self.pathlabel.config(text=basename(self.filename))  # show filename as label
        if self.filename.endswith('.txt'):
            return
        self.duration = findduration(self.filename)
        self.workinglabel.config(text="WORKING", font=(
            "Helvetica", 20))  # Show WORKING when transcribing
        self.pbar_det.pack()  # show the progress bar
        self.pbar_det.start()  # Start the progress bar
        root.update()
        new_path = transcribe(self.filename)  # Call transcribe
        self.workinglabel.config(text="")  # remove working label

        wordcloud_path = wordcloud_create(self.filename)
        self.new_image(wordcloud_path)
        stemmer_func(new_path)

        self.pbar_det.stop()  # Stop progress bar
        self.pbar_det.pack_forget()  # Remove progress bar


    # Search function
    def search(self):
        '''Search in transcription'''
        # Open transcription
        trans = basename(self.filename).replace(".wav", ".txt")

        if not trans == '':
            if not self.searchentry.get() == '':
                with open('transcribed/' + trans, 'r') as filen:  # Open transcribed file
                    transcription = filen.read().replace('\n', '')

                keyword = self.searchentry.get()  # Get entry from textbox
                nooverlapstring = removerlap(transcription.split(' '))  # Call removerlap function
                words = nooverlapstring.split(' ')  # Splits new transcription into words list

                # Find word number and time interval
                wordlabel, time, timestamplabel = findword(words, keyword, self.duration)

                # Write result to label
                if wordlabel != "Word number":
                    self.wordlabel.config(text=wordlabel)
                    self.estimatelabel.config(text=time)
                    self.timestamplabel.config(text=timestamplabel)
                else:
                    self.wordlabel.config(text="Word not found")
                    self.timestamplabel.config(text="")
            else:
                self.wordlabel.config(text="Enter word in search field")

        else:
            self.timestamplabel.config(text="No file selected")

    def new_image(self, path):
        '''Word Cloud image'''
        self.imagefile2 = Image.open(path)
        self.image2 = self.imagefile2.resize((400, 400), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.image2)
        self.panel1.configure(image=self.image2)
        self.display = self.image2

root = Tk()
b = PodSearch(root)
root.title("Podcast Searcher")
root.geometry("650x500+0+200")
root.mainloop()
