#!/Users/ksg/miniconda2/bin/python2.7
'''this module estimates the time in an interval'''

from PodSearch import maptoaudio

def estimate(words, keyword):
    '''Estimates time'''
    counter = 1
    wordlabel = "Word number"
    timestamp = ""
    shift = 0
    for i, _ in enumerate(words):
        if _ == "--":
            counter = counter + 1
            shift = i
        if keyword.lower() in _.lower():
            totalwordpos = i + 1
            wpsplit = totalwordpos - shift
            wordlabel += " " + str(wpsplit) + ","

            timestamp += maptoaudio(counter)

    return timestamp, wordlabel
