import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk, re, pprint
from nltk import word_tokenize

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

def count_words(text):
    '''
    count the frequency of the words in a string, and return a DataFrame.
    The input should be a string with english words.
    The output is a dataframe with words and the counts.
    '''
    lst = text.split(' ')
    set_ = set(lst)

    count = []
    for x in set_:
        n = lst.count(x)
        count.append(n)

    df = pd.DataFrame(data = list(zip(lst, count)), columns = ['word', 'count'])
    df = df.sort_values(by='count', ascending=False)
    return df

def generate_wordcloud(words, mask, STOPWORDS):
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
