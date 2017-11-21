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
            for _ in words[counter:counter + 6]:
                wordsplus += " " + _
            if wordsplus.startswith(' '):
                wordsplus = wordsplus[1:]
            for _ in words[counter - 7:counter - 1]:
                wordsminus += _ + " "

            # Merge overlap
            if wordsminus != "":
                match = sq(None, wordsminus, wordsplus).find_longest_match(0, len(wordsminus), 0, len(wordsplus))
                overlap = wordsminus + wordsplus[match.b+match.size:]

            # Before overlap
            remwords = words[start: counter - 10] if cnt == 2 else words[start + 6: counter - 7]
            transcription += ' '.join(remwords) + ' ' + overlap + ' -- '
            start = counter
            rest = ""
            for _ in words[counter + 6:]:
                rest += _ + " "
            if rest.endswith(' '):
                rest = rest[:-1]

    transcription += rest + "--"

    # Only for debugging
    text_file = open("overlapremoved/Output.txt", "w")
    text_file.write(transcription)
    text_file.close()

    return transcription
