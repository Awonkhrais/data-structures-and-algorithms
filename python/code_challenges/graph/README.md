# Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.
## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:
- add node - add edge - get nodes - get neighbors - size

## Approach & Efficiency
Big O:
Time: O(n^2)
Space: O(n)


## API

add_node(value): adds a new node to the graph, returns the added node
add_edge(start_node, end_node, weight): adds new edge between two nodes, takes in two nodes, has ability to add weight
get_nodes( ) - returns all of the nodes as a collection
get_neighbors(node): returns a collection of nodes (with weights) connected to a node, takes in a node
size( ) - returns number of nodes in Graph; integer
