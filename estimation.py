#!/Users/ksg/miniconda2/bin/python2.7
'''Find word number, time in interval and interval'''
from decimal import Decimal

def findword(words, keyword):
    '''Find word number, interval and estimation'''
    counter = 1
    wordlabel = "Word number"
    timeintervallabel = ""
    shift = 0
    time = "Estimated at "
    for i, _ in enumerate(words):
        if _ == "--":
            counter = counter + 1
            shift = i
        if keyword.lower() in _.lower():
            totalwordpos = i + 1
            wpsplit = totalwordpos - shift
            wordlabel += " " + str(wpsplit) + ","
            timeintervallabel += calcinterval(counter)
            for k, _ in enumerate(words[totalwordpos:]):
                if _ == "--":
                    wordinterval = totalwordpos + k - shift
                    break
            if counter == 1:
                decimal = Decimal(wpsplit)/Decimal(wordinterval) * 14
            else:
                decimal = Decimal(wpsplit)/Decimal(wordinterval) * 12
            totalseconds = str(round(firsttimestamp(counter) + decimal, 2))
            head, tail = totalseconds.split('.')
            time += str(formattime(int(head)) + "." + tail) + ", "
    if wordlabel.endswith(','):
        wordlabel = wordlabel[:-1]
        wordlabel += ' in interval'
        timeintervallabel = timeintervallabel[:-2]
        time = time[:-2]
    return (wordlabel, time, timeintervallabel)

def calcinterval(counter):
    '''Where in audio is result'''
    seconds1 = (counter - 1) * 14  # Calc interval start
    time1 = formattime(seconds1)  # Format to hh:mm:ss

    number = 14 if counter == 1 else 12
    seconds2 = (counter - 1) * 14 + number  # Calc interval end
    time2 = formattime(seconds2)  # Format to hh:mm:ss

    timestamp = time1 + " - " + time2 + ", "
    return timestamp

def firsttimestamp(counter):
    '''returns seconds on beginning of interval'''
    seconds = (counter - 1) * 14
    return seconds

def formattime(seconds):
    '''format seconds to hh:mm:ss'''
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time = "%d:%02d:%02d" % (hours, minutes, seconds)
    return time
