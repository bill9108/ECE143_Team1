import json as js
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_bars(countName, counts):
    '''
    Plot a bar plot for the number of different types of restaurants.
    Parameters: countName is a list of the names of the types and counts
    is a list of the corresponding number of restaurants. The two lists
    must be of the same length.
    '''
    assert(isinstance(countName, list))
    assert(isinstance(counts, list))
    assert(len(countName) == len(counts))

    f, ax = plt.subplots(figsize=(18,12), dpi = 200)
    barlist = plt.bar (countName, height=counts, width=0.5,color='#0b37e5')
    for i, v in enumerate(counts):
        ax.text(i, v + 25, str(v), color='blue', fontweight='bold', ha='center')
    plt.title('Number of Different Types of Restaurants on Yelp', fontsize=22)
    barlist[2].set_color('grey')
    barlist[7].set_color('grey')
    barlist[5].set_color('grey')
    barlist[9].set_color('grey')
    plt.xticks(rotation=60, fontsize=12)
    plt.ylabel('# of Restaurants', fontsize=18)


def plot_pie(countName, counts, title, colors = None):
    '''
    Plot a pie chart for the given names and numbers with the given list of colors.
    Parameters: countName is the list of names of the categories and counts is the
    list of numbers. colors is the list of colors for each corresponding 
    category. The length of colors must match the length of countName.
    '''
    assert(isinstance(countName, list)) 
    assert(isinstance(counts, list))
    assert(colors == None or isinstance(colors, list))
    assert(isinstance(title, str))
    assert(len(countName) == len(counts) and (colors == None or len(counts) == len(colors)))

    f, ax = plt.subplots(figsize=(10,10),dpi = 200)

    patches, texts, autotexts = plt.pie (x=counts[0:10], labels=countName[0:10], 
    autopct='%1.2f%%', labeldistance=1.05, colors=colors)
    ax.axis('equal')
    for t in texts:
        t.set_fontsize(14)
    for at in autotexts:
        at.set_fontsize(14)
        at.set_color('white')
        at.set_fontweight('bold')
    plt.title(title, fontsize=20)
    f.show()