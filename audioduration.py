#!/Users/ksg/miniconda2/bin/python2.7
'''This module detects the duration of the imported audio file'''
import wave

def findduration(filepath):
    '''Takes: filepath
    Returns: Duration of .wav file in seconds'''

    audiofile = wave.open(filepath, 'r')
    frames = audiofile.getnframes()
    framerate = audiofile.getframerate()
    duration = frames / float(framerate)
    return duration
