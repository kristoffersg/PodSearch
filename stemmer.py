'''This module stems and removes stopwords'''
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def stemmer_func(string):
    '''Takes: Filename
    Returns: Path to stemmed transcription'''
    # Preprocessing of the transcribed text-file___________________________________________________
    new_str = re.sub('[^a-zA-Z0-9\n\" "-]', '', string) #Remove all non-alphanumeric characters

    # Stemming_____________________________________________________________________________________
    ps = PorterStemmer()
    words = word_tokenize(new_str)
    stemmed = ""
    for _ in words:
        stemmed += ps.stem(_) + ' '
    return stemmed
