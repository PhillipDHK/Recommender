'''
@author: Phillip Kang
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    lst1 = [0 for x in range(len(items))]
    lst2 = [0 for x in range(len(items))]
    for k, v in ratings.items():
        for value in range(len(v)):
            lst1[value] += v[value]
            if v[value] != 0:
                lst2[value] += 1
    lst3 = []
    for i in range(len(lst1)):
        if lst2[i] == 0:
            lst3.append(float(0))
        else:
            lst3.append(lst1[i]/lst2[i])
    ret = []
    for i in range(len(items)):
        ret.append(tuple((items[i], lst3[i])))
    ret = sorted(ret)
    return sorted(ret, key = lambda x: x[1], reverse = True)
def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    lst1 = []
    d = {}
    for k, v in ratings.items():
        if k == name:
            lst1.append(v)
        if k != name:
            d[k] = v
    count = 0
    for k, v in d.items():
        for i in range(len(v)):
            count += v[i] * lst1[0][i]
        d[k] = count
        count = 0
    d_list = d.items()
    ret = list(d_list)
    ret = sorted(ret)
    return sorted(ret, key = lambda x: x[1], reverse = True)

def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    similar = similarities(name, ratings)
    similar = similar[:numUsers]
    d = {}
    for k, v in ratings.items():
        weight = 0
        for i in similar:
            if k == i[0]:
                weight = i[1]
        new_ratings = [weight * x for x in v]
        d[k] = new_ratings
    return averages(items, d)

if __name__ == '__main__':
    items = ["DivinityCafe", "FarmStead", "IlForno",
    "LoopPizzaGrill", "McDonalds", "PandaExpress",
     "Tandoor", "TheCommons", "TheSkillet"]
    ratings = {"Sarah Lee":
                   [3, 3, 3, 3, 0, -3, 5, 0, -3],
               "Melanie":
                   [5, 0, 3, 0, 1, 3, 3, 3, 1],
               "J J":
                   [0, 1, 0, -1, 1, 1, 3, 0, 1],
               "Sly one":
                   [5, 0, 1, 3, 0, 0, 3, 3, 3],
               "Sung-Hoon":
                   [0, -1, -1, 5, 1, 3, -3, 1, -3],
               "Nana Grace":
                   [5, 0, 3, -5, -1, 0, 1, 3, 0],
               "Harry":
                   [5, 3, 0, -1, -3, -5, 0, 5, 1],
               "Wei":
                   [1, 1, 0, 3, -1, 0, 5, 3, 0]}

    # print(averages(items, ratings))
    # print(similarities('Harry', ratings))
    print(recommendations('Harry', items, ratings, 2))