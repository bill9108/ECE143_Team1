from matplotlib import pyplot as plt
import numpy as np

def create_bar_plots(counts, xaxes, start, end, title, xlabel, ylabel):
    
    '''
    This function help plots the bar plot
    :param:counts
    :type: list
    :param:xaxes
    :type:list or numpy array
    :param:start
    :type:int
    :param:end
    :type:int
    :param:title
    :type:str
    :param:xlabel
    :type:str
    :param:ylabel
    :type:str
    '''
    
    assert isinstance(counts,list)
    assert isinstance(xaxes, list)
    assert isinstance(start,int)
    assert isinstance(end, int)
    assert isinstance(title,str)
    assert isinstance(xlabel,str)
    assert isinstance(ylabel,str)
    
    bins = np.linspace(start,end, len(xaxes)+1)
    arr = plt.hist(counts,bins)
    plt.close()
    my_list = []
    for i in range(len(xaxes)):
        my_list.append(arr[0][i])
    
    plt.figure(num=None, figsize=(12,10),dpi=160)
    barlist = plt.bar(xaxes,my_list,color='#0346d8')
    for i, v in enumerate(my_list):
        plt.text(i,v+2000, str(int(v)), ha='center',fontsize=11)
    plt.title(title,fontsize=18)
    plt.xlabel(xlabel,fontsize=12)
    plt.ylabel(ylabel, fontsize=12)  