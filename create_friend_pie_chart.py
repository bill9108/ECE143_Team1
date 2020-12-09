from matplotlib import pyplot as plt
import numpy as np

def create_friends_pie_chart(sizes, labels, title):
    '''
    This fucntion helps to create the pie chart when visualizing the friends data
    :param:sizes
    :type:list
    :param:labels
    :type:list
    :praam:title
    :type:str
    '''
    
    
    fig1, ax1 = plt.subplots(figsize=(10,10))

    patches, texts, autotexts = ax1.pie(sizes,labels = labels, autopct = '%1.2f%%',shadow=True, startangle = 45)
    ax1.axis('equal')
    for t in texts:
        t.set_fontsize(14)
    for at in autotexts:
        at.set_fontsize(14)
        at.set_color('white')
        at.set_fontweight('bold')
    plt.title(title,fontsize=20)
    plt.show()