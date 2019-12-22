# AStar
Comparing A* Search with basic graph traversal algorithms 


A* search is an informed search algorithm used to traverse weighted graphs, attempting to find the shortest path between two vertices. We call A* an "informed" search algorithm, because it uses a heuristic function to estimate the cost between points in a graph.

At any given point in a search, A* needs to decide which direction it should explore in the graph, and so using this estimation, along with the known distance from the start vertex to the current vertex, it determines the most optimal path to explore. More specifically, A* attempts to minimize the function f(n) = g(n) + h(n), where g(n) is the current path cost from the start, and h(n) is the estimation of the path cost to the goal.

My assignment was to compare A* search to some basic uninformed search algorithms like breadth first search, depth first and iterative deepening search on a simple array manipulation problem. The problem was as follows: imagine you're given two 2D arrays, and your task is find a sequence of operations (shifting rows or columns) that tranforms the first array into the second array.
