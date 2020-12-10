import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
import progressbar
import plotly.graph_objs as go
import numpy as np
import plotly as py
import cufflinks as cf
from plotly.offline import init_notebook_mode,iplot
import re
import plotly.express as px
cf.go_offline()
cf.set_config_file(offline=True,world_readable=True)
from IPython.display import Image


def polarity(business, review, star):
    assert isinstance(business,pd.DataFrame)
    assert isinstance(review,pd.DataFrame)
    assert isinstance(star,list)

    restaurant=business[business['categories'].str.contains('Restaurants')]
 
    fig2=go.Figure()
    avg_polarity=[]
    for i in range(len(star)):    
        rest_5=restaurant[restaurant['stars']==star[i]]
        a=list(set(rest_5['business_id']))
        hh=[]
        for j in range(len(a)):
            b=list(review[review['business_id']==a[j]]['text'])
            polarity=[]
            for sentence in b:
                blob = TextBlob(sentence)
                polarity.append(blob.sentiment.polarity)
            if len(polarity)!=0:
                hh.append(sum(polarity)/len(polarity))
        avg_polarity.append(sum(hh)/len(hh))
        trace=go.Scatter(x=np.linspace(0,len(hh),num=len(hh)),y=hh,line_shape='spline',name='{} star'.format(str(star[i])))
        fig2.add_trace(trace)
        fig2.update_layout(title="Polarity of Reviews with Different Ratings",title_x=0.5,title_font_size=25,xaxis_title='i\'th restaurant',yaxis_title='Polarity')
    fig2.show()


def subjectivity(business,review,star):
    assert isinstance(business,pd.DataFrame)
    assert isinstance(review,pd.DataFrame)
    assert isinstance(star,list)

    restaurant=business[business['categories'].str.contains('Restaurants')]

    fig1=go.Figure()
    avg_subjectivity=[]
    for i in range(len(star)):    
        rest_5=restaurant[restaurant['stars']==star[i]]
        a=list(set(rest_5['business_id']))
        hhh=[]
        for j in range(len(a)):
            b=list(review[review['business_id']==a[j]]['text'])
            subjectivity=[]
            for sentence in b:
                blob = TextBlob(sentence)
                subjectivity.append(blob.sentiment.subjectivity)
            if len(subjectivity)!=0:
                hhh.append(sum(subjectivity)/len(subjectivity))
        avg_subjectivity.append(sum(hhh)/len(hhh))
        trace=go.Scatter(x=np.linspace(0,len(hhh),num=len(hhh)),y=hhh,line_shape='spline',name='{} star'.format(str(star[i])))
        fig1.add_trace(trace)
        fig1.update_layout(title="subjectivity of different star rate",title_x=0.5,xaxis_title='i\'th of restaurants',yaxis_title='subjectivity')
    fig1.show()




