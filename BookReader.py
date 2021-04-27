'''
@author: Phillip Kang
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    titles = []
    students = {}
    file = open('data/books.txt', 'r')
    count = 0
    for line in file:
        components = line.strip().split(',')
        student = ''
        count += 1
        for i in range(len(components)):
            if i == 0:
                students[components[i]] = []
                student = components[i]
            elif i%2 == 0:
                students[student].append(float(components[i]))
            elif count == 1:
                titles.append(components[i])
    return titles, students

if __name__ == '__main__':
    print(getdata())