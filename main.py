import networkx as nx
import matplotlib.pyplot as plt

# 1
print("Problem 1")

G1 = nx.Graph()
main_edges = [
    ('A', 'B'), ('A', 'E'), ('B', 'C'), ('B', 'F'), ('C', 'D'), ('C', 'G'), 
    ('D', 'H'), ('E', 'F'), ('E', 'I'), ('F', 'G'), ('F', 'J'), ('G', 'H'), 
    ('I', 'J'), ('I', 'M'), ('J', 'N'), ('M', 'N')
]

unconnected_edges = [
    ('K', 'L'), ('L', 'O'), ('O', 'P')
]

# add all edges to the graph
G1.add_edges_from(main_edges)
G1.add_edges_from(unconnected_edges)

# part a 
def find_all_connected_components(graph):
    return list(nx.connected_components(graph))

connected_components = find_all_connected_components(G1)
print('\nPart A')
print('Connected Components:', connected_components)

# part b 
def check_path(graph, start, end):
    bfs_path_exists = nx.has_path(graph, start, end)
    # check path using DFS manually
    dfs_path_exists = False
    for path in nx.dfs_edges(graph, start):
        if end in path:
            dfs_path_exists = True
            break
    
    return bfs_path_exists, dfs_path_exists

# example check between 'A' and 'M'
bfs_path, dfs_path = check_path(G1, 'A', 'M')
print('\nPart B')
print(f"Path exists between 'A' and 'M': BFS: {bfs_path}, DFS: {dfs_path}")


#part c 
def compare_paths(graph, start, end):
    # find path using BFS
    bfs_path = nx.shortest_path(graph, start, end)
    # find path using DFS
    dfs_paths = list(nx.all_simple_paths(graph, start, end))
    # grab the first path 
    dfs_path = dfs_paths[0] if dfs_paths else None
    
    return bfs_path, dfs_path

# compare the paths 
bfs_path, dfs_path = compare_paths(G1, 'A', 'M')
print('\nPart C')
print(f"BFS path between 'A' and 'M': {bfs_path}")
print(f"DFS path (one of the possible paths) between 'A' and 'M': {dfs_path}")
print('\n')





#2
print("Problem 2 \n")
edges = [(1, 3), (3, 2), (4, 1), (2, 1), (4, 2), 
         (3, 5), (5, 6), (5, 8), (6, 8), (6, 7),
         (6, 10), (8, 10), (10, 9), (10, 11), (8, 9),
         (9, 5), (7, 10), (9, 11), (11, 12), (4, 12)]

G = nx.DiGraph()
G.add_edges_from(edges)

#Part A
#Find strongly connected components of the digraph
scc = list(nx.strongly_connected_components(G))

print("Part A \nStrongly Connected Components:")
for i in scc:
    print(i)

#Part B
#Draw the meta graph
meta_graph = nx.condensation(G)
pos = nx.spring_layout(meta_graph)
nx.draw(meta_graph, pos, with_labels = True, node_size = 1000, node_color = 'skyblue')
plt.title("Meta Graph of Strongly Connected Components")
plt.show()

#Part C
#Linearize it in topological order
topological = list(nx.topological_sort(meta_graph))

print("Topological Order:")
print(topological)
nx.draw_kamada_kawai(G, with_labels = True)
plt.show()


#3
#Dijkstra's Algorithm
def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph[min_node]:
      weight = current_weight + graph[min_node][edge]['weight']
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

#Part 3 Graph
G3 = nx.Graph()

G3edges = [('A', 'B', 22), ('A', 'C', 9), ('A', 'D', 12), 
           ('B', 'C', 35), ('C', 'D', 4), ('C', 'E', 65),
           ('D', 'E', 33), ('B', 'F', 36), ('C', 'F', 42),
           ('E', 'F', 18), ('F', 'G', 39), ('E', 'G', 23),
           ('B', 'H', 34), ('F', 'H', 24), ('G', 'H', 25),
           ('D', 'I', 30), ('G', 'I', 21), ('H', 'I', 19)]

pos = {'A':(0,2), 'B':(1,5), 'C':(1,2), 'D':(1,-1),
       'E':(2,1), 'F':(3,3), 'G':(4,1), 'H':(5,5),
       'I':(5,-1)}


G3.add_weighted_edges_from(G3edges)

G3.distance = {('A', 'B'): 22, ('A', 'C'): 9, ('A', 'D'): 12,}

edge_labels = nx.get_edge_attributes(G3, "weight")

nx.draw(G3, pos, with_labels = True, node_size = 700)
nx.draw_networkx_edge_labels(G3, pos, edge_labels)
plt.show()


#a)
print("\nDijkstra's Shortest Path")
v, path = dijkstra(G3, 'A')
print('Visited: ', v)
print('Path :', path)

#b) Minimum spanning tree for a connected weighted graph
MST = nx.minimum_spanning_tree(G3)

edge_labels = nx.get_edge_attributes(MST, "weight")

nx.draw(MST, pos, with_labels = True, node_size = 700)
nx.draw_networkx_edge_labels(MST, pos, edge_labels)
plt.show()

#d) If the graph has an edge with a negative weight, can you apply 
#   Dijkstra’s algorithm to find a shortest path tree?
G3Test = nx.Graph()

G3TestEdges = [('A', 'B', -22), ('A', 'C', 9), ('A', 'D', 12), 
           ('B', 'C', 35), ('C', 'D', 4), ('C', 'E', 65),
           ('D', 'E', 33), ('B', 'F', -36), ('C', 'F', 42),
           ('E', 'F', 18), ('F', 'G', 39), ('E', 'G', 23),
           ('B', 'H', 34), ('F', 'H', 24), ('G', 'H', 25),
           ('D', 'I', 30), ('G', 'I', 21), ('H', 'I', 19)]

G3Test.add_weighted_edges_from(G3TestEdges)

print("\nDijkstra's Algorithm on graph with a negative weight")
v, path = dijkstra(G3, 'A')
print('Visited: ', v)
print('Path :', path)

