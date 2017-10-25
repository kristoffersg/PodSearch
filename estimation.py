#!/Users/ksg/miniconda2/bin/python2.7
'''Find word number, time i interval and interval'''

def estimate(words, keyword):
    '''Find word number in interval'''
    counter = 1
    wordlabel = "Word number"
    timestamplabel = ""
    shift = 0
    for i, _ in enumerate(words):
        if _ == "--":
            counter = counter + 1
            shift = i
        if keyword.lower() in _.lower():
            totalwordpos = i + 1
            wpsplit = totalwordpos - shift
            wordlabel += " " + str(wpsplit) + ","
            timestamplabel += maptoaudio(counter)
    return wordlabel, timestamplabel

def maptoaudio(counter):
    '''Where in audio is result'''
    seconds1 = (counter - 1) * 14  # Calc interval start
    minutes, seconds = divmod(seconds1, 60)  # Format to hh:mm:ss
    hours, minutes = divmod(minutes, 60)
    time1 = "%d:%02d:%02d" % (hours, minutes, seconds)

    n = 14 if counter == 1 else 12
    seconds2 = (counter - 1) * 14 + n  # Calc interval end
    minutes, seconds = divmod(seconds2, 60)  # Format to hh:mm:ss
    hours, minutes = divmod(minutes, 60)
    time2 = "%d:%02d:%02d" % (hours, minutes, seconds)

    timestamp = time1 + " - " + time2 + ", "
    return timestamp
