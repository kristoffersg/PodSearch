from stemming.porter2 import stem
import time
from os.path import basename
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re

def stemmer_func(filename):
    start_time = time.time()

    #rawInput = basename(filename)
    input = filename.replace(".txt", "")

    string = open(input + '.txt').read()
    new_str = re.sub('[^a-zA-Z0-9\n\" "]', '', string)                  #Remove all non-alphanumeric characters (./#%,;:)
    rawInput = basename(input)                                          #Cut away folder path
    open("transcribed/stem_" + rawInput + '.txt', 'w').close()          #Generate/reset txt file for stemmed words

    ps = PorterStemmer()
    words = word_tokenize(new_str)
    for w in words:
        stemmed = ps.stem(w)
        print(stemmed)
        open("transcribed/stem_" + rawInput + '.txt', 'a').write(stemmed + " ")

    elapsed_time = time.time() - start_time
    print("Stemming took " + str(elapsed_time) + " seconds")

    new_src = "transcribed/stem_" + rawInput + '.txt'
    return new_src