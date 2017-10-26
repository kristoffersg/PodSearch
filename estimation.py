#!/Users/ksg/miniconda2/bin/python2.7
'''Find word number, time in interval and interval'''
from decimal import Decimal

def estimate(words, keyword):
    '''Find word number in interval'''
    counter = 1
    wordlabel = "Word number"
    timestamplabel = ""
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
            timestamplabel += maptoaudio(counter)
            end = 0
            for i, _ in enumerate(words[totalwordpos:]):
                if _ == "--":
                    end = totalwordpos + i
                    hej = end - shift
                    break
            john = Decimal(wpsplit)/Decimal(hej) * 12
            time += str(format(firsttimestamp(counter) + john, '.2f')) + ", "
    if wordlabel.endswith(','):
        wordlabel = wordlabel[:-1]
        wordlabel += ' in interval'
        timestamplabel = timestamplabel[:-2]
        time = time[:-2]
    return (wordlabel, time, timestamplabel)

def maptoaudio(counter):
    '''Where in audio is result'''
    seconds1 = (counter - 1) * 14  # Calc interval start
    time1 = formattime(seconds1)  # Format to hh:mm:ss

    n = 14 if counter == 1 else 12
    seconds2 = (counter - 1) * 14 + n  # Calc interval end
    time2 = formattime(seconds2)  # Format to hh:mm:ss

    timestamp = time1 + " - " + time2 + ", "
    return timestamp

def firsttimestamp(counter):
    seconds = (counter - 1) * 14
    return seconds

def formattime(seconds):
    '''format seconds to hh:mm:ss'''
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time = "%d:%02d:%02d" % (hours, minutes, seconds)
    return time
