import json

def load_user_data(path,dataset):
    '''
    This function takes two input parameters and return a list of data.
    :param: path
    :type: str
    :param:dataset
    :type: str
    
    :rtype:list
    '''
    assert isinstance(path,str)
    assert isinstance(dataset,str)
    if dataset == 'user':
        data=[]
        with open(path,encoding ="utf8") as f:
            for line in f:
                data.append(json.loads(line))
        return data
    else:
        print("please enter a valid dataset name")