import pandas as pd
import matplotlib.pyplot as plt
import functools
import numpy as np
import math
import json

def attribut(business_dir):
    #a = pd.read_json('/home/notebook/data/group/liziwen/ECE143/Yelp_dataset_checkin_clean.json')
    #b = pd.read_json('/home/notebook/data/group/liziwen/ECE143/Yelp_dataset_review_clean.json')
    c = pd.read_json(business_dir)
    #d = pd.read_json('/home/notebook/data/group/liziwen/ECE143/yelp_academic_dataset_user.json')
    attribute = c['attributes']
    star = c['stars']
    num = 0
    good = 0
    bad = 0
    goodstar = 0
    badstar = 0
    for i, v in attribute.items():
        if 'GoodForKids' in v:
            if v['GoodForKids'] == 'True':
                good += 1
                goodstar += star[i]
            else:
                bad += 1
                badstar += star[i]
    good_tv = 0
    bad_tv = 0
    goodstar_tv = 0
    badstar_tv = 0
    for i, v in attribute.items():
        if 'HasTV' in v:
            if v['HasTV'] == 'True':
                good_tv += 1
                goodstar_tv += star[i]
            else:
                bad_tv += 1
                badstar_tv += star[i]
    noise = {}
    for i, v in attribute.items():
        if 'NoiseLevel' in v:
            if v['NoiseLevel'].startswith('u'):
                if v['NoiseLevel'][2:-1] in noise:
                    noise[v['NoiseLevel'][2:-1]] += star[i]
                    noise[v['NoiseLevel'][2:-1] + '_count'] += 1
                else:
                    noise[v['NoiseLevel'][2:-1]] = star[i]
                    noise[v['NoiseLevel'][2:-1] + '_count'] = 1
            else:
                if v['NoiseLevel'][1:-1] in noise:
                    noise[v['NoiseLevel'][1:-1]] += star[i]
                    noise[v['NoiseLevel'][1:-1] + '_count'] += 1
                else:
                    noise[v['NoiseLevel'][1:-1]] = star[i]
                    noise[v['NoiseLevel'][1:-1] + '_count'] = 1
    num = 0
    good_g = 0
    bad_g = 0
    goodstar_g = 0
    badstar_g = 0
    for i, v in attribute.items():
        if 'RestaurantsGoodForGroups' in v:
            if v['RestaurantsGoodForGroups'] == 'True':
                good_g += 1
                goodstar_g += star[i]
            else:
                bad_g += 1
                badstar_g += star[i]

    data_noise = [noise['quiet'] / noise['quiet_count'], noise['average'] / noise['average_count'],
                  noise['loud'] / noise['loud_count'], noise['very_loud'] / noise['very_loud_count']]

    data = [goodstar / good, badstar / bad, goodstar_g / good_g, badstar_g / bad_g, goodstar_tv / good_tv,
            badstar_tv / bad_tv, data_noise[0], data_noise[1], data_noise[2], data_noise[3]]
    labels = ['goodkid', 'badkid', 'goodgroup', 'badgroup', 'withTV', 'withoutTV', 'quiet', 'average', 'loud',
              'veryloud']
    plt.figure(figsize=(14, 12))
    plt.bar([0.3, 1, 2, 2.7, 3.7, 4.4, 6, 7, 8, 9], data, width=0.6, tick_label=labels)
    plt.ylabel('star')
    plt.title('Star from users in terms of some attributes')

def review_time(review_dir):
    b = pd.read_json(review_dir)
    time = b['date']
    month_yr = {}
    for index, value in time.items():
        temp = value.strftime('%Y/%m')
        if temp in month_yr:
            month_yr[temp] += 1
        else:
            month_yr[temp] = 1
    ttt = []
    for i in month_yr:
        ttt.append(i)
    def func(x, y):
        xx = int(x[:4])
        yy = int(y[:4])
        xxx = int(x[5:])
        yyy = int(y[5:])
        if xx < yy:
            return -1

        elif xx == yy:

            if xxx < yyy:
                return -1
            if xxx == yyy:
                return 0
            else:
                return 1
        else:

            return 1
    tttt = sorted(ttt, key=functools.cmp_to_key(func))
    time_count = []
    for i in tttt:
        time_count.append(month_yr[i])
    tick = []
    a = 2004
    b = 12
    for i in range(30):
        if i % 2 == 0:
            b = 12
            tick.append(str(a) + '/' + str(b))
        else:
            b = 6
            a += 1
            tick.append(str(a) + '/' + str(b))

    lll = np.linspace(0, 175, 30)
    plt.figure(figsize=(24, 12))
    plt.plot(time_count[:-4])
    plt.xticks(lll, tick)
    plt.title('Number of reviews vs time')
    plt.ylabel('Reviews')
    plt.xlabel('time(year/month)')

def reviwer_weight(user_dir,save_dir):
    d = pd.read_json(user_dir, lines=True)
    use_time = d['yelping_since']
    review_count = d['review_count']
    useful = d['useful']
    funny = d['funny']
    cool = d['cool']
    fans = d['fans']
    elite = d['elite']
    points = [0 for i in use_time]
    for i, v in use_time.items():
        points[i] += 2020 - int(v[:4])
    for i, v in review_count.items():
        if v != 0:
            points[i] += math.log(v)
    for i, v in useful.items():
        if v != 0:
            points[i] += math.log(v) / 4
    for i, v in funny.items():
        if v != 0:
            points[i] += math.log(v) / 2
    for i, v in cool.items():
        if v != 0:
            points[i] += math.log(v) / 2
    for i, v in fans.items():
        if v != 0:
            points[i] += math.log(v)
    for i, v in elite.items():
        string = list(v.split(','))
        points[i] += len(string)
    res = []
    length = list(range(len(points)))
    points_dic = zip(length, points)
    res.append(dict(points_dic))
    min = 10000
    max = 0
    for i in points:
        if min >i:
            min=i
        if max < i:
            max = i
    points = [(i - min) / (max - min) for i in points]
    points[0]
    points_dic = zip(length, points)
    a = dict(points_dic)
    with open(save_dir, "w", encoding="utf-8") as f:
        json.dump(a, f)
    sort = sorted(points)
    sort = np.array(sort)
    plt.hist(sort, bins=40)
    plt.title('Histogram of users\'weight')
    plt.xlabel('weight')
    plt.ylabel('number')
