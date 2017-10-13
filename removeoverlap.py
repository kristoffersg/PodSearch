#!/Users/ksg/miniconda2/bin/python2.7
'''This module removes overlap in transcription'''
from difflib import SequenceMatcher as sq

def removerlap(words):
    '''Removal of overlap'''
    counter = 1
    cnt = 1
    start = counter
    transcription = ""
    for _ in words[1:len(words)-1]:
        counter = counter + 1
        if _ == "--":
            wordsplus = ""
            wordsminus = ""
            cnt = cnt + 1
            for _ in words[counter:counter + 8]:
                wordsplus += " " + _
            for _ in words[counter - 2:counter - 10 : -1]:
                wordsminus += " " + _        
            # Merge overlap
            if wordsminus != "":
                splitwords = wordsminus.split()
                correctwordsminus = " ".join(splitwords[::-1])
                match = sq(None, correctwordsminus, wordsplus).find_longest_match(0, len(correctwordsminus), 0, len(wordsplus))
                overlap = correctwordsminus + "" + wordsplus[match.b+match.size:]
            # Before overlap
            tempminus = ""
            remwords = words[start: counter - 9] if cnt == 2 else words[start + 8: counter - 9]
            tempminus += ' '.join(remwords) + ' ' + overlap + ' -- '
            start = counter            
            transcription += tempminus
    return transcription    
