'''
@author: Phillip Kang
'''
import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    recommend = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    recommend = recommend[:top]
    lst = []
    lst1 = []
    for i in RecommenderEngine.recommendations(name, items, ratings, numUsers):
        if ratings[name][items.index(i[0])] == 0:
            lst.append(i)
        if ratings[name][items.index(i[0])] != 0:
            lst1.append(i)
    return lst1[:top], lst[:top]

if __name__ == '__main__':
    name = 'student1367'
    items = ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind',
             'A Nightmare on Elm Street', 'Alice in Wonderland',
             'Anchorman: The Legend of Ron Burgundy',
             'Austin Powers in Goldmember', 'Avatar', 'Black Swan']
    ratings = {'student1367': [0, 3, -5, 0, 0, 1, 5, 1, 3, 0],
               'student1046': [0, 0, 0, 3, 0, 0, 0, 0, 3, 5],
               'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0],
               'student1103': [-3, 3, -3, 5, 0, 0, 5, 3, 5, 5]}
    numUsers = 2
    top = 3
    print(makerecs(name, items, ratings, numUsers, top))
             



