import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image


def generate_wordcloud (business, reviews, star, max_words):
    '''
    Description: generate a wordcloud from all the reviews with the
    specific star rating. 
    Parameters: business is a dataframe containing information
    of all the businesses. reviews is a dataframe containing
    the review dataset. star is the rating level of the reviews that this
    wordcloud is generated from. max_words is the maximum number of
    words in the wordcloud.
    '''

    assert(isinstance(business, pd.DataFrame))
    assert(isinstance(reviews, pd.DataFrame))
    assert(isinstance(star, int))
    assert(isinstance(max_words, int))
    assert('stars' in business.columns and 'business_id' in business.columns)
    assert('text' in reviews.columns)

    stopwords = set(STOPWORDS) 
    rest = business[business['stars'] == star]
    a = list(set(rest['business_id']))
    all_reviews = ""
    for i in range(len(a)):
        b = list(reviews[reviews['business_id']==a[i]]['text'])
        bs = ""
        bs = bs.join(b)
        all_reviews += bs
        i = i + 1

    all_reviews = all_reviews.lower()
    punc = '!()-[]{};:"\,<>./?@#%^&*_~'
    for p in punc:
        all_reviews = all_reviews.replace(p,"")

        
    replace=["food","order","location","place","one","time","go","minute","manager",
            "said","pizza","employee","drive thru", 'even', 'back', 'ed', 'told', 
            'will', 'never', 'asked', 'give', 'went', 'drive', 'know', 'alway',
            ' s ', ' ing ', ' i ', ' t ', ' u ', ' od ', 'come', 'came', 'restaurant']

    for s in replace:
        all_reviews = all_reviews.replace(s,"")

    wordcloud = WordCloud(width = 800, height = 800, background_color ='white', 
                      stopwords = stopwords, min_font_size = 10, max_words=max_words).generate(all_reviews) 
    plt.figure(figsize = (10, 10), dpi = 200) 
    plt.imshow(wordcloud) 