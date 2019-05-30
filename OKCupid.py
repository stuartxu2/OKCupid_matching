import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk, re, pprint
from nltk import word_tokenize
import seaborn as sns
from pygeocoder import Geocoder
import gmaps
import gmaps.datasets
gmaps.configure(api_key="AIzaSyCr7VthVl0P5-f-tGEv2zxRfxa3lI2z3Uk")

import matplotlib.pyplot as plt
%matplotlib inline
sns.set(style="ticks", color_codes=True)

def clean_text(text):
    '''
    clean the text data: split the text, remove the redundant signs and words.
    '''
    text = text.replace('<br />', ' ')
    text = text.replace('\n', ' ')
    words = nltk.word_tokenize(text)   #split the text into words
    words = [word for word in words if word.isalpha()]    #remove the non-alphabetic signs
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in set(stop_words)]   #remove the stop words
    return words

def clean_text_column(df, col_name):
    '''
    input a dataframe and one of its column, the function clean the text within
    the column.
    '''
    df_ = df[df[col_name].notnull()]
    df[col_name] = df_.apply(lambda row: clean_text(row[col_name]), axis = 1)


def get_coordinates(address):
    '''
    transform the physical address into longitude and latitude.
    '''
    result = Geocoder('AIzaSyCr7VthVl0P5-f-tGEv2zxRfxa3lI2z3Uk').geocode(str(address))
    return result.coordinates


def get_coordinates(address):
    '''
    get the longitude and latitude of the address
    '''
    result = Geocoder('AIzaSyCr7VthVl0P5-f-tGEv2zxRfxa3lI2z3Uk').geocode(str(address))
    return result.coordinates


def generate_wordcloud(words, mask):
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
