from graph import *

def business_trip(graph:Graph ,city_lst):
    cost=0
    state=False

    for country in range(len(city_lst)-1):
        neighbors=graph.get_neighbors(city_lst[country])
        for i in neighbors:
           if city_lst[country+1]==i.node:
               cost+=i.weight
               state=True

    if state==False:
        return False, cost


    return True, cost




