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
    rawinput = basename(filename)                                              #Cut away folder path
    string = open(filename).read()
    new_str = re.sub('[^a-zA-Z0-9\n\" "-]', '', string)      #Remove all non-alphanumeric characters
    open("transcribed/stem_" + rawinput, 'w').close() #Generate txt file for stemmed words

    # Stemming_____________________________________________________________________________________
    ps = PorterStemmer()
    words = word_tokenize(new_str)
    for _ in words:
        stemmed = ps.stem(_)
        print stemmed
        open("transcribed/stem_" + rawinput, 'a').write(stemmed + " ")

    new_src = "transcribed/stem_" + rawinput
    return new_src
