#!/Users/ksg/miniconda2/bin/python2.7
'''This module detects the duration of the imported audio file'''
import wave
import contextlib


def findduration(filepath):
    '''Takes: filepath
    Returns: Duration of .wav file in seconds'''
    with contextlib.closing(wave.open(filepath,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration
