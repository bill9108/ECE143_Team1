from matplotlib import pyplot as plt
import numpy as np

def plot_stacked_plot(data1,data2, labels):
    '''
    This function create a stacked bar plot 
    :param:data1
    :type:list
    :param: data2
    :type: list
    :param:labels
    :type: list
    '''
    assert isinstance(data1, list)
    assert isinstance(data2,list)
    assert isinstance(labels, list)

    pair = []
    for i in range(len(data1)):
        pair.append((data1[i],data2[i]))
    review_one = [0]*6
    review_more = [0]*6
    for i in pair:
        if i[0] < 10 and i[1]==1:
            review_one[0]+=1
        elif i[0] <10 and i[1]>1:
            review_more[0]+=1
        elif (i[0]>=10 and i[0]<20) and i[1]==1:
            review_one[1]+=1
        elif (i[0]>=10 and i[0]<20) and i[1]>1:
            review_more[1]+=1
        elif (i[0]>=20 and i[0]<30) and i[1]==1:
            review_one[2]+=1
        elif (i[0]>=20 and i[0]<30) and i[1]>1:
            review_more[2]+=1
        elif (i[0]>=30 and i[0]<40) and i[1]==1:
            review_one[3]+=1
        elif (i[0]>=30 and i[0]<40) and i[1]>1:
            review_more[3]+=1
        elif (i[0]>=40 and i[0]<50) and i[1]==1:
            review_one[4]+=1
        elif (i[0]>=40 and i[0]<50) and i[1]>1:
            review_more[4]+=1
        elif i[0]>=50 and i[1]==1:
            review_one[5]+=1
        elif i[0]>=50 and i[1]>1:
            review_more[5]+=1
    
    fig, ax = plt.subplots(figsize=(12,15))
    ax.bar(labels,review_more,color = '#ff820f',label='users with one friend')
    ax.bar(labels,review_one,color = '#0346d8',bottom = review_more,label = 'users with more than one friend')
    plt.legend(prop={'size':15})
    plt.title('Number of Reviews And Number of Friends', fontsize=20)
    plt.ylabel('Number of Users', fontsize=12)
    plt.xlabel('Number of Reviews', fontsize=12)
    plt.show()