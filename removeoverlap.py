#!/Users/ksg/miniconda2/bin/python2.7
'''This module removes overlap in transcription'''
from difflib import SequenceMatcher as sq

def removerlap(words):
    '''Removal of overlap'''
    counter = 1
    for _ in words[1:len(words)-1]:
        counter = counter + 1
        if _ == "--":
            wordsplus = ""
            wordsminus = ""
            for _ in words[counter:counter + 8]:
                wordsplus += " " + _
            for _ in words[counter - 2:counter - 10 : -1]:
                wordsminus += " " + _
            if wordsminus != "":
                splitwords = wordsminus.split()
                correctwordsminus = " ".join(splitwords[::-1])
                match = sq(None, correctwordsminus, wordsplus).find_longest_match(0, len(correctwordsminus), 0, len(wordsplus))
                overlap = correctwordsminus + "" + wordsplus[match.b+match.size:]
    return overlap