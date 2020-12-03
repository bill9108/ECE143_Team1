import pandas as pd
import numpy as np

def clean_dataset (path, outPath, dataset, cleaned_business = None):
    '''
    Clean the review or business dataset. 
    if dataset is "business", drops all businesses with na value, not open, not in the U.S., and not a 
    restaurant.
    If dataset is "review", drop all review that is not for the businesses in the cleaned_business dataset.
    Parameters: path is a string for input file path. outPath is a string for the output
    file path. dataset is a string specifying which dataset is to be cleaned. cleaned_business
    is the file path to the cleaned businesses dataset when dataset is "review".
    '''

    assert(isinstance(path, str) and len(path) > 0)
    assert(isinstance(outPath, str) and len(outPath) > 0)
    assert(isinstance(dataset, str) and dataset == 'business' or dataset == 'review')
    assert(dataset != 'review' or (dataset == 'review' and isinstance(cleaned_business, str) and len(clean_dataset) > 0))

    if dataset == 'business':
        df = pd.read_json(path, lines=True)
        df = df.dropna()

        discard = list()
        states = ['IL', 'AZ', 'OH', 'PA', 'NV', 'NC', 'SC', 'WI',
        'TX', 'CO', 'NY', 'FL', 'VT', 'HI', 'OR', 'WA', 'CA',
        'VA', 'NE']
        for i in df.index:
            if 'Restaurants' not in df.loc[i].categories or df.loc[i].is_open == 0 or df.loc[i].state not in states:
                discard.append(i)
            
        df.drop(discard, inplace=True)
        df.drop('is_open', axis=1, inplace=True)

        f = open (outPath, 'w')
        df.to_json(path_or_buf=f)
        f.close()
        return
    
    elif dataset == 'review':
        bus = pd.read_json(cleaned_business, encoding='utf8')
        busId = np.array(bus['business_id'])
        reviewReader = pd.read_json(path, lines=True, encoding='utf8', chunksize=100000)
        reviewDfList = list()
        for chunk in reviewReader:
            reviewDfList.append(chunk[chunk.business_id.isin(busId)])

        review = pd.concat(reviewDfList)

        f = open (outPath, 'w')
        review.to_json(path_or_buf=f)
        f.close()