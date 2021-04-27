'''
@author: Phillip Kang
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    """
    Tests if functions from RecommenderEngine works. A statement is printed
    depending whether it works or not.
    """
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)

    
    avg = RecommenderEngine.averages(items,ratings)
    if avg[0:3] == [('DivinityCafe', 4.0), ('TheCommons', 3.0), ('Tandoor', 2.4285714285714284)]:
        print("average",avg)
        print("Averages work")
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        if key == 'Sung-Hoon':
            if slist[0:3] == [('Wei', 1), ('Sly one', -1), ('Melanie', -2)]:
                print("Similarities work")

        print(key,slist)
        r3 = RecommenderEngine.recommendations(key,items,ratings,3)
        if key == 'Sarah Lee':
            if r3[0:3] == [('Tandoor', 149.5), ('TheCommons', 128.0), ('DivinityCafe', 123.33333333333333)]:
                print("top",r3)
                print("Recommendations Work")

if __name__ == '__main__':
    driver()