'''This module stems and removes stopwords'''
from os.path import basename
from os import path
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def stemmer_func(filename):
    '''Takes: Filename
    Returns: Path to stemmed transcription'''
    # Preprocessing of the transcribed text-file___________________________________________________
    input_ = filename.replace(".txt", "")
    rawinput = basename(input_)                                              #Cut away folder path
    string = open(input_ + '.txt').read()
    new_str = re.sub('[^a-zA-Z0-9\n\" "-]', '', string)      #Remove all non-alphanumeric characters
    open("transcribed/stem_" + rawinput + '.txt', 'w').close() #Generate/reset txt file for stemmed words

    # Stopwords import_____________________________________________________________________________
    d = path.dirname(__file__)
    stopwords = open(path.join(d, "wordcloudTools/stopwords.txt")).read()   #Loading stopwords file
    stopwords = set(stopwords.split())                  #Splitting stopwords file into a set

    # Stemming and Stopword removal process________________________________________________________
    ps = PorterStemmer()
    words = word_tokenize(new_str)
    for w in words:
        if w not in stopwords:
            stemmed = ps.stem(w)
            print stemmed
            open("transcribed/stem_" + rawinput + '.txt', 'a').write(stemmed + " ")

    new_src = "transcribed/stem_" + rawinput + '.txt'
    return new_src
