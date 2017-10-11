# # Imports ____________________________________________________________________________________________________________
# Wordcloud
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS
from os.path import basename


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


def wordcloud_create(filename):
    d = path.dirname(__file__)

    # Set source to the audio file in question
    rawInput = basename(filename)
    input_ = rawInput.replace(".wav", ".txt")

    # # Read the mask image
    # taken from
    # https://commons.wikimedia.org/wiki/File:Cloud_font_awesome.svg
    mask = np.array(Image.open(path.join(d, "wordcloudTools\cloud.png")))

    # # Load transcribed txt file:
    text = open(path.join(d, "transcribed/" + input_)).read()

    # # Preprocessing of stopwords:
    stopwords = open(path.join(d, "wordcloudTools/stopwords.txt")).read()   #Loading stopwords file
    stopwords = stopwords.split()                                           #Splitting stopwords file into correct format
    stopwords = set(stopwords)                                              #Making the stopwords file a set

    # # Wordcloud generation:
    wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10, random_state=1).generate(text)

    # # # For black/white wordcloud:
    # plt.title("Wordcloud")
    # plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
    # # wc.recolor(color_func=grey_color_func, random_state=3)    # Necessary to recolor wc to greyscale, when not plotting
    # wc.to_file("wordcloudTools/Wordcloud_result.png")
    # plt.axis("off")
    # plt.show()