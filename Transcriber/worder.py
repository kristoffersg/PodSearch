# # Imports ____________________________________________________________________________________________________________
# Wordcloud
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS
from os.path import basename

# Stemming
from stemmer import stemmer_func

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

    # # Load transcripted txt file:
    text = open(path.join(d, "transcribed/" + input_)).read()

    # # Preprocessing of stopwords:
    stemmed_stopwords = stemmer_func("wordcloudTools/stopwords")    #Stemming of the stopwords file
    temp = open(path.join(d, stemmed_stopwords)).read()             #Loading new stemmed stopwords file
    temp = temp.split()                                             #Splitting stopwords file into correct format
    stemmed_stopwords_set = set(temp)                               #Making the stopwords file a set
    # print stemmed_stopwords_set

    # # Stemming the transcribed txt file
    stemmed_txt = stemmer_func("transcribed/" + input_)
    text = open(path.join(d, stemmed_txt)).read()

    # # Wordcloud generation:
    wc = WordCloud(max_words=1000, mask=mask, stopwords=stemmed_stopwords_set, margin=10,
                   random_state=1).generate(text)

    # # Store default colored image:
    default_colors = wc.to_array()

    # # For black/white wordcloud:
    plt.title("Wordcloud")
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
    wc.to_file("wordcloudTools/Wordcloud_result.png")
    plt.axis("off")
    plt.show()

    # # For default colored words:
    # plt.figure()
    # plt.title("Default colors")
    # plt.imshow(default_colors, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

# wordcloud_create()

# start_time = time.time()
#
# string = open('Full_GG_28_Nature_Podcast_18_August_2016.txt').read()
# new_str = re.sub('[^a-zA-Z0-9\n\" "]', '', string)
# open('b.txt', 'w').close()
#
# ps = PorterStemmer()
# words = word_tokenize(new_str)
# for w in words:
#     stemmed = ps.stem(w)
#     print(stemmed)
#     open('b.txt', 'a').write(stemmed + " ")
#
# elapsed_time = time.time() - start_time
# print("Stemming took " + str(elapsed_time) + " seconds")