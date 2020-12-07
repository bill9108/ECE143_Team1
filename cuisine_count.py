import json as js
import pandas as pd
import numpy as np

def count_cuisine_num_business (cuisine_dict, cuisines, with_none_cuisine):
    '''
    Count the number of businesses for each cuisine.
    Parameters: cuisine_dict is the dictionary of cuisine generated from get_cuisine().
    cuisines is a list of strings represending cuisines. with_none_cuisine is a boolean
    indicating whether fast food, bars, coffee & tea and breakfast and brunch should be
    included in the count.
    '''
    assert(isinstance(cuisine_dict, dict))
    assert(isinstance(cuisines, list))
    assert(isinstance(with_none_cuisine, bool))
    
    cuiCount = dict()
    for c in cuisines: 
        if c == 'Pizza':
            cuiCount['(Non-Italian) Pizza'] = len(cuisine_dict[c])
        else:
            cuiCount[c] = len(cuisine_dict[c])

    if (with_none_cuisine):
        sortCount = sorted(cuiCount.items(), key=lambda x: x[1], reverse=True)
        countName = list()
        counts = list()
        for i in sortCount:
            countName.append(i[0])
            counts.append(i[1])
    else:
        del (cuiCount['Fast Food'])
        del (cuiCount['Bars'])
        del (cuiCount['Coffee & Tea'])
        del (cuiCount['Breakfast & Brunch'])

        sortCount = sorted(cuiCount.items(), key=lambda x: x[1], reverse=True)
        countName = list()
        counts = list()
        for i in sortCount:
            countName.append(i[0])
            counts.append(i[1])

    return (countName, counts)  


def count_cuisine_num_review (cuisine_dict, checkin, cuisines):
    '''
    Count the number of reviews for each cuisine. Notice that the number of checkin
    and the number of reviews for a business are the same, so this function actually
    counts the number of checkin instead to reduce computation time.
    Parameters: cuisine_dict is the dictionary of cuisine generated from get_cuisine().
    cuisines is a list of strings represending cuisines. checkin is a Pandas dataframe
    containing checkin information. 
    '''
    assert(isinstance(cuisine_dict, dict))
    assert(isinstance(cuisines, list))
    assert(isinstance(checkin, pd.DataFrame))
    assert('business_id' in checkin.columns and 'date' in checkin.columns)

    cuiCount = dict()
    for c in cuisines: 
        if c == 'Pizza':
            cuiCount['(Non-Italian) Pizza'] = len(cuisine_dict[c])
        else:
            cuiCount[c] = len(cuisine_dict[c])

    for i in range(len(checkin)):
        row = checkin.iloc[i]
        business = row.business_id
        count = len(row.date.split(', '))
        for c in cuisines:
            if c == 'Pizza':
                if business in cuisine_dict[c]:
                    cuiCount['(Non-Italian) Pizza'] = cuiCount['(Non-Italian) Pizza'] + count
            else:
                if business in cuisine_dict[c]:
                    cuiCount[c] = cuiCount[c] + count

    del (cuiCount['Fast Food'])
    del (cuiCount['Bars'])
    del (cuiCount['Coffee & Tea'])
    del (cuiCount['Breakfast & Brunch'])

    sortciCount = sorted(cuiCount.items(), key=lambda x: x[1], reverse=True)
    countName = list()
    counts = list()
    for i in sortciCount:
        countName.append(i[0])
        counts.append(i[1])

    return (countName, counts)


def count_cuisine_yearly_num_review(cuisine_dict, review, cuisines, year):
    '''
    Count the number of reviews for each cuisine in the given year.
    Parameters: cuisine_dict is the dictionary of cuisine generated from get_cuisine().
    cuisines is a list of strings represending cuisines. review is a Pandas dataframe
    containing the business ID and date information of reviews. year is the desired year 
    which the reviews should be filtered for.
    '''

    assert(isinstance(cuisine_dict, dict))
    assert(isinstance(cuisines, list))
    assert(isinstance(review, pd.DataFrame))
    assert(isinstance(year, int))
    assert(year > 2000)
    assert('business_id' in review.columns and 'date' in review.columns)
    
    count = dict()

    for c in cuisines:
        if c == 'Pizza':
            count['(Non-Italian) Pizza'] = 0
        else:
            count[c] = 0
        
    for i in range(len(review)):
        row = review.iloc[i]
        business = row.business_id
        if (row.date.year != year):
            continue
        for c in cuisines:
            if c == 'Pizza':
                if business in cuisine_dict[c]:
                    count['(Non-Italian) Pizza'] = count['(Non-Italian) Pizza'] + 1
            else:
                if business in cuisine_dict[c]:
                    count[c] = count[c] + 1

    del (count['Fast Food'])
    del (count['Bars'])
    del (count['Coffee & Tea'])
    del (count['Breakfast & Brunch'])

    sortedCount = sorted(count.items(), key=lambda x: x[1], reverse=True)
    countName = list()
    counts = list()
    for i in sortedCount:
        countName.append(i[0])
        counts.append(i[1])

    return (countName, counts)