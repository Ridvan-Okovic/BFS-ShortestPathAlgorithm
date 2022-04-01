
# Package pandas should be installed using the terminal with the command 'pip install pandas'
from pandas import *
import numpy as np

# If the .csv files are not in the same directory as the commented_code_script.py file
# Provide these 2 variables with the file path of the corresponding files
dataset_from_to = read_csv('FromTo.csv')
dataset_city_info = read_csv('cityName.csv')

# These 3 variables use the pandas built in function to separate the files by columns and store them as list
from_id = dataset_from_to['From_ID'].to_list()
to_id = dataset_from_to['To_ID'].to_list()
city_name = dataset_city_info['Name'].to_list()

nr_of_nodes = 1174
nr_of_edges = 1417


# Function which creates an adjacency matrix
def adjacency_matrix():
    # Used numpy function which creates a matrix of n*n size and initiates all values to 0
    adj = np.zeros((nr_of_nodes, nr_of_nodes), dtype=int)
    # For loop to fill up the adjacency matrix with 1's where there is an edge between them
    for i in range(nr_of_edges):
        # Set nodes to minus one of its value to match the id's to the indices
        from_node = from_id[i] - 1
        to_node = to_id[i] - 1
        # Populate the matrix where there are edges between the vertices
        adj[from_node][to_node] = 1
        adj[to_node][from_node] = 1
    return adj


# Function to perform BFS on the adjacency matrix
def breadth_first_search(start, end):
    # Declare a variable called previous which will store the parent vertex to the current vertex
    # Which we will later use to print the shortest path between 2 cities
    previous = [-1] * nr_of_nodes

    # Set the new_start and new_end to the index at which the city is in the list 'city_name'
    # The id of the city would then be 1 less then its original value but that's okay because
    # Indexing in the matrix and list goes from 0 and we set all id's to 1 minus its original value
    new_start = city_name.index(start)
    new_end = city_name.index(end)

    # Create the adjacency matrix using the function declared previously
    adj = adjacency_matrix()

    # Visited list is used to keep track of which vertices have already been visited
    # Initially we will set all of the values of the visited list to FALSE because none of the vertices are visited
    visited = [False] * nr_of_nodes

    # Create a queue which will initially only contain the start vertex
    queue = [new_start]

    # Set the starting vertex as visited
    visited[new_start] = True

    # This while loop will run until we have entries in the queue or until we hit the break statement
    while queue:
        # vis variable keeps track of the current vertex in the queue
        vis = queue[0]

        # After we got all of the adjacent vertices to the current vertex we pop the current vertex from the queue
        queue.pop(0)

        # Condition which checks whether we have reached the end city in our function
        # If True we break from the while loop
        if vis == new_end:
            break

        # For every adjacent vertex to the current vertex
        for i in range(nr_of_nodes):
            if adj[vis][i] == 1 and (not visited[i]):
                # Push the adjacent vertex in the queue
                queue.append(i)

                # Set the current vertex as visited
                visited[vis] = True

                # Temp is used to keep track of the parent of the ith vertex
                temp = i
                previous[temp] = vis

    # If we don't reach our end vertex we will print to the console 'No path found'
    # noinspection PyUnboundLocalVariable
    if vis != new_end:
        return print('No path found')

    # Empty list to keep track of the path
    path = []

    # Going from the back to front we add cities to the path until the new_end == new_start
    while new_end != new_start:

        # We get the parent to the current last vertex and add it to the list
        new_end = previous[new_end]

        # Fetch and append the corresponding city name to the path
        path.append(city_name[new_end])

    # Use the built in function the reverse the list and append the real end to the end of the list
    path.reverse()
    path.append(end)
    print(path, '-The number of edges between the cities:', len(path)-1)


breadth_first_search('Le Havre', 'Aalborg')
