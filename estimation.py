#!/Users/ksg/miniconda2/bin/python2.7
'''Find word number, time in interval and interval'''
from decimal import Decimal

def findword(words, keyword, duration):
    '''Takes: List of words, keyword and duration of .wav file in seconds
    Returns: Word number, interval and estimation'''
    # Initialization of variables
    counter = 1
    wordlabel = "Word number"
    timeintervallabel = "Located in: "
    shift = -1
    time = "Estimated at: "
    for i, _ in enumerate(words[:-1]): # For loop throght words but not the ending "--"
        if _ == "--":  # counts the intervals
            counter += 1
            shift = i
            shiftstartseconds = (counter - 1) * 12 + 2
        if keyword.lower() in _.lower():  # Compare keyword to word
            wpsplit = i - shift  # Position of word in interval
            wordlabel += " " + str(wpsplit) + ","  # Make label with position
            timeintervallabel += calcinterval(counter, duration)  # Make label with interval
            for k, _ in enumerate(words[i:]):  # Find position of interval end
                if _ == "--":
                    wordinterval = k + wpsplit - counter
                    break
            if counter == 1:  # If first interval it is 14 seconds
                decimal = Decimal(wpsplit)/Decimal(wordinterval) * 14
                shiftseconds = 14 / Decimal(wordinterval)
            else:  # every other interval is 12
                if (counter - 1) * 12 + 2 > duration:  # makes the ready for last interval
                    lastinterval = duration - shiftstartseconds
                    decimal = Decimal(wpsplit)/Decimal(wordinterval) * int(lastinterval)
                    shiftseconds =  int(lastinterval) / Decimal(wordinterval)
                else:
                    decimal = Decimal(wpsplit)/Decimal(wordinterval) * 12
                    shiftseconds = 12/Decimal(wordinterval)
            # make label of estimation
            n = 0 if counter == 1 else 2
            totalseconds = str(round(((counter - 1) * 12 + n + decimal)-shiftseconds, 2))
            head, tail = totalseconds.split('.')
            time += str(formattime(int(head)) + "." + tail) + ', '

    # Removes ", "" in the end of the labels
    if wordlabel.endswith(','):
        wordlabel = wordlabel[:-1]
        wordlabel += ' in interval'
        timeintervallabel = timeintervallabel[:-2]
        time = time[:-2]
    return (wordlabel, time, timeintervallabel)

def calcinterval(counter, duration):
    '''Takes: Interval counter
    Returns: Which interval result is in'''
    if counter == 1:
        seconds1 = 0
        seconds2 = 14
    else:
        seconds1 = (counter - 1) * 12 + 2  # Calc interval start
        seconds2 = seconds1 + 12
    time1 = formattime(seconds1)  # Format to hh:mm:ss
    if seconds2 > duration:  # make sure interval doesn't exceed durtion of .wav file
        seconds2 = duration
    time2 = formattime(seconds2)  # Format to hh:mm:ss

    timestamp = time1 + " - " + time2 + ", "
    return timestamp

def formattime(seconds):
    '''Takes: Seconds
    Returns: hh.mm.ss'''
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time = "%02d:%02d:%02d" % (hours, minutes, seconds)
    return time
