import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk, re, pprint
from nltk import word_tokenize

import matplotlib.pyplot as plt

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

def generate_wordcloud(words, mask=None, STOPWORDS=['']):
    word_cloud = WordCloud(width = 2000, height = 300, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

def plot_word_frequency(word_count1, word_count2, title='Don\'t forget your title gurl~'):
    """
    For plotting male and female word count use.
    Word_count1 is male word count, word_count2 is female.
    """
    fig, ax = plt.subplots(2, 1, figsize=(20, 15))

    x1 = np.arange(word_count1.shape[0])
    x2 = np.arange(word_count2.shape[0])
    widTh = 0.6

    ax[0].bar(x1, word_count1['count'],
              color='#3462BF', width=widTh, label='Male')
    ax[0].set_xticks(x1)
    ax[0].set_xticklabels(word_count1['word'], rotation=45,
                          fontsize=18, weight='bold', ha='right')
    ax[0].set_ylabel("Count", fontsize=18, weight='bold')
    ax[0].legend()

    ax[1].bar(x2, word_count2['count'], color='#F23D6D',
              width=widTh, label='Female')
    ax[1].set_xticks(x2)
    ax[1].set_xticklabels(word_count2['word'], rotation=45,
                          fontsize=18, weight='bold', ha='right')
    ax[1].set_xlabel("Frequent Words", fontsize=18, weight='bold')
    ax[1].set_ylabel("Count", fontsize=18, weight='bold')

    ax[1].legend()

    _ = ax[0].set_title(title, fontsize = 25, weight='bold')
    plt.tight_layout()
