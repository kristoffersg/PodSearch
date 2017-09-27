from wav_splitter import readwave, writewave, split
import time
import shutil
import os

start_time = time.time()

# # Pre-coding__________________________________________________________________________________________________________
# Clear directory "res"
if(os.path.isdir('res')):
    shutil.rmtree('res')
# Set source to the audio file in question
input_ = "Little Happier 1"
src = 'pods/' + input_ + '.wav'
# Set destination path
dest = 'res/output-'

# # Pre-set variables___________________________________________________________________________________________________
# Podcast splitting interval in seconds
interval_ = 20
# Overlap in seconds
overlap_ = 2

# # Splitting audio file________________________________________________________________________________________________
# extract data from wav file
data = readwave(src)
# # split(data, seconds_pr_split=None, overlap=None):
# If just split(data) is written, it splits the audio into 1 second clips with a 1 second overlap. (1+1 = 2 seconds)
# split file into equal 1-second intervals
[splitted, iterations] = split(data, interval_-overlap_, overlap_)

# save each 1-second interval to output as individual files
ex1 = writewave(dest + '1-', splitted)
print ex1 # ['res/file-ex1-0.wav', 'res/file-ex1-1.wav', ...]

#_________________________________________________________________________________________________________
# Transcription Google

import speech_recognition as sr
# obtain path to "english.wav" in the same folder as this script
from os import path

text_file = open("transcribed/Full_GG_" + input_ + ".txt", "w")
text_file.close()

# Transcribe for every 20-seconds audio file created
for i in range(0, iterations):
    # Obtain path to audio files
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "res/output-1-" + str(i) + ".wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        print("Google is trying")
        GoogleTranscription = r.recognize_google(audio).encode('utf-8')  #encode is for euro signs and other unicode
        print("Google Speech Recognition:         " + GoogleTranscription)

        text_file = open("transcribed/Full_GG_" + input_ + ".txt", "a")
        text_file.write(GoogleTranscription + "\n")
        text_file.close()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


# # Write timestamp to txt______________________________________________________________________________________________
Google_elapsed_time = time.time() - start_time
print("Google took " + str(Google_elapsed_time) + " seconds")

text_file = open("transcribed/Full_GG_" + input_ + ".txt", "a")
text_file.write("\n \n" + "Google took " + str(Google_elapsed_time) + " seconds")
text_file.close()