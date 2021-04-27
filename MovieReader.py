'''
@author: Phillip Kang
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    lst = []
    d = {}
    file = open('data/movies.txt', 'r')
    for line in file:
        x = line.strip().split(',')
        lst.append(x)
    movies = [x[1] for x in lst]
    movies = sorted(set(movies))
    for line in lst:
        lst1 = [0 for x in range(len(movies))]
        (name, movie, rating) = (line[0], line[1], line[2])
        if name not in d:
            d[name] = lst1
        d[name][movies.index(movie)] = float(rating)
    return (movies, d)
if __name__ == '__main__':
    print(getdata())