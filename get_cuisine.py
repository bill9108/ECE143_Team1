import json as js
import pandas as pd
import numpy as np

def get_cuisine(business):
    '''
    Returns a dictionary mapping the id of all businesses in the incoming dataframe
    to a cuisine type.
    Parameters: business must be a Pandas dataframe with a column labeled as 
    'business_id'.
    '''

    assert(isinstance(business, pd.DataFrame))
    assert('business_id' in business.columns)

    cuisine = ['Chinese', 'Italian', 'Japanese', 'Korean', 'Mexican', 'American', 'Greek', 'French', 'Spanish', 'Turkish', 'Vietnamese',
          'Russian', 'German',  'Argentine', 'Thai', 'Middle Eastern', 'Brazilian', 'Pakistani', 
          'Indian','Filipino', 'Pizza', 'Caribbean', 'Hawaiian', 'Cuban', 'Mediterranean', 'Coffee & Tea',
          'Breakfast & Brunch', 'Fast Food', 'Bars']

    covered = set()
    for c in cuisine:
        for i in range(len(business)):
            if i not in covered and c in business.iloc[i].categories:
                covered.add(i)

    cuiDic = dict()
    covered.clear()

    for c in cuisine:
        cuiDic[c] = list()
        for i in range(len(business)):
            row = business.iloc[i]
            if i not in covered and c in row.categories:
                cuiDic[c].append(row.business_id)
                covered.add(i)

    return cuiDic
    