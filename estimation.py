#!/Users/ksg/miniconda2/bin/python2.7
'''Find word number, time in interval and interval'''
from decimal import Decimal

def findword(words, keyword):
    '''Takes: List of words and keyword
    Returns: Word number, interval and estimation'''
    # Initialization of variables
    counter = 1
    wordlabel = "Word number"
    timeintervallabel = ""
    shift = 0
    time = "Estimated at "
    for i, _ in enumerate(words):
        if _ == "--":  # counts the intervals
            counter = counter + 1
            shift = i
        if keyword.lower() in _.lower():  # Compare keyword to word
            totalwordpos = i + 1  # position of word in transcription
            wpsplit = totalwordpos - shift  # Position of word in interval
            wordlabel += " " + str(wpsplit) + ","  # Make label with position
            timeintervallabel += calcinterval(counter)  # Make label with interval
            for k, _ in enumerate(words[totalwordpos:]):  # Find position of interval end
                if _ == "--":
                    wordinterval = totalwordpos + k - shift
                    break
            if counter == 1:  # If first interval it is 14 seconds
                decimal = Decimal(wpsplit)/Decimal(wordinterval) * 14
            else:  # every other interval is 12
                decimal = Decimal(wpsplit)/Decimal(wordinterval) * 12
            # make label of estimation
            totalseconds = str(round(firsttimestamp(counter) + decimal, 2))
            head, tail = totalseconds.split('.')
            time += str(formattime(int(head)) + "." + tail) + ", "
    # Removes ', ' in the end of the labels
    if wordlabel.endswith(','):
        wordlabel = wordlabel[:-1]
        wordlabel += ' in interval'
        timeintervallabel = timeintervallabel[:-2]
        time = time[:-2]
    return (wordlabel, time, timeintervallabel)

def calcinterval(counter):
    '''Takes: Interval counter
    Returns: Which interval result is in'''
    seconds1 = (counter - 1) * 14  # Calc interval start
    time1 = formattime(seconds1)  # Format to hh:mm:ss

    number = 14 if counter == 1 else 12
    seconds2 = (counter - 1) * 14 + number  # Calc interval end
    time2 = formattime(seconds2)  # Format to hh:mm:ss

    timestamp = time1 + " - " + time2 + ", "
    return timestamp

def firsttimestamp(counter):
    '''Takes: interval counter
    Returns: Beginning second of interval'''
    seconds = (counter - 1) * 14
    return seconds

def formattime(seconds):
    '''Takes: Seconds
    Returns: Seconds in hh:mm:ss'''
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time = "%d:%02d:%02d" % (hours, minutes, seconds)
    return time
