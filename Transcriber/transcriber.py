'''This module is transcribing audio'''
import shutil
import os
from os.path import basename
from os import path
from wav_splitter import readwave, writewave, split
import speech_recognition as sr


def transcribe(filename):
    '''This function transcribes the audio'''
    # Pre-coding_________________________________________________________________________________
    # Clear directory "res"
    if os.path.isdir('res'):
        shutil.rmtree('res')

    # Set source to the audio file
    rawinput = basename(filename)
    input_ = rawinput.replace(".wav", "")
    dest = 'res/output-'                                # Set destination path

    # Pre-set variables__________________________________________________________________________
    # Podcast splitting interval in seconds
    interval_ = 14
    overlap_ = 2                                        # Overlap in seconds

    # Splitting audio file_______________________________________________________________________
    # extract data from wav file
    data = readwave(filename)
    # # split(data, seconds_pr_split=None, overlap=None):
    # If just split(data) is written, it splits the audio into 1 second clips with a
    # 1 second overlap. (1+1 = 2 seconds)
    # split file into equal 1-second intervals
    [splitted, iterations] = split(data, interval_ - overlap_, overlap_)

    # save 1-second interval to output as individual files
    ex1 = writewave(dest + '1-', splitted)
    print ex1  # ['res/file-ex1-0.wav', 'res/file-ex1-1.wav', ...]

    # Transcription Google_________________________________________________________________________
    text_file = open("transcribed/" + input_ +
                     ".txt", "w")     # Open .txt file
    text_file.close()

    # Transcribe for every 20-seconds audio file created
    for i in range(0, iterations):
        # Obtain path to audio files
        audio_file = path.join(path.dirname(path.realpath(__file__)),
                               "res/output-1-" + str(i) + ".wav")

        # use the audio file as the audio source
        rec = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = rec.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # print "Google is trying"
            googletranscription = rec.recognize_google(audio).encode(
                'utf-8')  # encode is for euro signs and other unicode
            # print "Google Speech Recognition:         " + googletranscription

            text_file = open("transcribed/" + input_ + ".txt", "a")
            text_file.write("-- " + googletranscription + " \n")
            text_file.close()
        except sr.UnknownValueError:
            print "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            print "Could not request results from Google Speech Recognition service; {0}".format(e)

    # # Write timestamp to txt_____________________________________________________________________
    text_file = open("transcribed/" + input_ + ".txt", "a")
    text_file.close()
