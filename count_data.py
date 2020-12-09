def count_data(data, name):
    '''
    this function takes two parameters and return the number of data the specified attribute has
    :param: data
    :type: list
    :param: name
    :type: str
    '''
    assert isinstance(data,list)
    assert isinstance(name,str)
    if name == 'average_stars':
        avg_stars = []
        for i in range(len(data)):
            avg_stars.append(data[i]['average_stars'])
        return avg_stars
    elif name == 'review_count':
        review_count = []
        for i in range(len(data)):
            review_count.append(data[i]['review_count'])
        return review_count
    elif name == 'friends':
        num_friend = []
        for i in range(len(data)):
            friendlist = data[i]['friends'].split(', ')
            num_friend.append(len(friendlist))
        return num_friend
    else:
        print('please enter a valid name for name parameter')