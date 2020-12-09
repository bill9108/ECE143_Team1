from matplotlib import pyplot as plt
import numpy as np

def create_pie_chart(counts, labels, start, end, title):
    
    '''
    This function takes four parameters and return a pie chart
    :param:counts
    :type:list
    :param:labels
    :type:list
    :param:start
    :type:int
    :param:end
    :type:int
    :param:title
    :type:str
    '''
    
    assert isinstance(counts,list)
    assert isinstance(labels, list)
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert isinstance(title,str)
    
    
    bins = np.linspace(start,end, len(labels)+1)
    arr = plt.hist(counts,bins)
    plt.close()
    my_list = []
    for i in range(len(labels)):
        my_list.append(arr[0][i])
    fig1, ax1 = plt.subplots(figsize=(10,10))

    patches, texts, autotexts = ax1.pie(my_list,labels = labels, autopct = '%1.2f%%',shadow=True, startangle = 90)
    ax1.axis('equal')
    for t in texts:
        t.set_fontsize(14)
    for at in autotexts:
        at.set_fontsize(14)
        at.set_color('white')
        at.set_fontweight('bold')
    plt.title(title,fontsize=20)
    plt.show()