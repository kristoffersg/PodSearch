import time
from os.path import basename
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
from os import path

def stemmer_func(filename):
    start_time = time.time()

    #rawInput = basename(filename)
    input = filename.replace(".txt", "")

    # Preprocessing of the transcribed text-file________________________________________________________________________
    string = open(input + '.txt').read()
    new_str = re.sub('[^a-zA-Z0-9\n\" "]', '', string)                  #Remove all non-alphanumeric characters (./#%,;:)
    rawInput = basename(input)                                          #Cut away folder path
    open("transcribed/stemstop_" + rawInput + '.txt', 'w').close()          #Generate/reset txt file for stemmed words

    # Stopwords import__________________________________________________________________________________________________
    d = path.dirname(__file__)
    stopwords = open(path.join(d, "wordcloudTools/stopwords.txt")).read()   #Loading stopwords file
    stopwords = stopwords.split()                                           #Splitting stopwords file into correct format
    stopwords = set(stopwords)                                              #Making the stopwords file a set

    # Stemming and Stopword removal process_____________________________________________________________________________
    ps = PorterStemmer()
    words = word_tokenize(new_str)
    for w in words:
        if w not in stopwords:
            stemmed = ps.stem(w)
            print(stemmed)
            open("transcribed/stemstop_" + rawInput + '.txt', 'a').write(stemmed + " ")

    elapsed_time = time.time() - start_time
    print("Stemming took " + str(elapsed_time) + " seconds")

    new_src = "transcribed/stemstop_" + rawInput + '.txt'
    return new_src