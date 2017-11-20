# # Imports ____________________________________________________________________________________________________________
# Wordcloud
from os import path
import random
from os.path import basename
import numpy as np
from PIL import Image
from wordcloud import WordCloud


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    '''Set color for cloud'''
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


def wordcloud_create(filename):
    '''Takes: Filename
    Returns: path to wordcloud'''
    d = path.dirname(__file__)

    # # Read the mask image
    # taken from
    # https://commons.wikimedia.org/wiki/File:Cloud_font_awesome.svg
    mask = np.array(Image.open(path.join(d, "wordcloudTools/cloud.png")))

    # Set source to the audio file and load transcrption
    input_ = basename(filename).replace(".wav", ".txt")
    text = open(path.join(d, "transcribed/" + input_)).read()

    # # Preprocessing of stopwords:
    stopwords = open(path.join(d, "wordcloudTools/stopwords.txt")).read()   #Loading stopwords file
    stopwords = set(stopwords.split()) #Splitting stopwords file into correct format

    # # Wordcloud generation:
    wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10, random_state=1).generate(text)

    # # For black/white wordcloud:
    wc.recolor(color_func=grey_color_func, random_state=3)    # Necessary to recolor wc to greyscale, when not plotting
    wordcloud_path = "wordcloudTools/Wordcloud_result.png"
    wc.to_file(wordcloud_path)

    return wordcloud_path
