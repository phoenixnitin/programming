"""
Minimum distance problem
"""
import sys
import heapq as heap

city_map = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
 'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
 'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
 'Drobeta': {'Mehadia': 75, 'Craiova': 120},
 'Eforie': {'Hirsova': 86},
 'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
 'Hirsova': {'Urziceni': 98, 'Eforie': 86},
 'Iasi': {'Vaslui': 92, 'Neamt': 87},
 'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
 'Oradea': {'Zerind': 71, 'Sibiu': 151},
 'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
 'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
 'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
 'Zerind': {'Arad': 75, 'Oradea': 71},
 'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80},
 'Timisoara': {'Arad': 118, 'Lugoj': 111},
 'Giurgiu': {'Bucharest': 90},
 'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
 'Vaslui': {'Iasi': 92, 'Urziceni': 142},
 'Neamt': {'Iasi': 87}}


def init_visited():
    '''
    Initialize visited object
    '''
    visited = {}
    for city in city_map:
        visited[city] = 0
    return visited

def get_city_with_minimum_distance(yet_to_explore):
    '''Get city with minimum distance in yet_to_explore'''
    minimum = sys.maxsize
    city = ''
    for cityname in yet_to_explore:
        if yet_to_explore[cityname] < minimum:
            minimum = yet_to_explore[cityname]
            city = cityname
    return city

def minimum_distance(source, destination):
    '''
    Find minimum distance between source and destination.
    '''
    visited = init_visited()
    distance = {}
    # yet_to_explore = {}
    yet_to_explore = []
    heap.heapify(yet_to_explore)
    # try:
    visited[source] = 1
    distance[source] = 0

    # yet_to_explore[source] = 0
    heap.heappush(yet_to_explore, (0, source))

    while yet_to_explore:
        # current_city = get_city_with_minimum_distance(yet_to_explore)
        _, current_city = heap.heappop(yet_to_explore)
        for connected_city in city_map[current_city]:
            if visited[connected_city]:
                calculated_distance = distance[current_city] + \
                    city_map[current_city][connected_city]
                if calculated_distance < distance[connected_city]:
                    distance[connected_city] = calculated_distance
                    # yet_to_explore[connected_city] = distance[connected_city]
                    heap.heappush(yet_to_explore, (distance[connected_city], connected_city))
            else:
                calculated_distance = distance[current_city] + \
                    city_map[current_city][connected_city]
                if destination not in distance or calculated_distance < distance[destination]:
                    visited[connected_city] = 1
                    distance[connected_city] = calculated_distance
                    # yet_to_explore[connected_city] = distance[connected_city]
                    heap.heappush(yet_to_explore, (distance[connected_city], connected_city))
        # del yet_to_explore[current_city]
    return distance[destination]
    # except Exception :
    #     pass

# print (minimum_distance('Oradea', 'Lugoj'))
# print (minimum_distance('Oradea', 'Sibiu'))
# print (minimum_distance('Iasi', 'Bucharest'))
print (minimum_distance('Oradea', 'Neamt'))
print (minimum_distance('Oradea', 'Giurgiu'))
