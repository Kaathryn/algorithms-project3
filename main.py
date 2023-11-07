import networkx as nximport matplotlib.pyplot as pltdef dijkstra(graph, initial):  visited = {initial: 0}  path = {}  nodes = set(graph.nodes)  while nodes:     min_node = None    for node in nodes:      if node in visited:        if min_node is None:          min_node = node        elif visited[node] < visited[min_node]:          min_node = node    if min_node is None:      break    nodes.remove(min_node)    current_weight = visited[min_node]    for edge in graph[min_node]:      weight = current_weight + graph[min_node][edge]['weight']      if edge not in visited or weight < visited[edge]:        visited[edge] = weight        path[edge] = min_node  return visited, path#1#2edges = [(1, 3), (3, 2), (4, 1), (2, 1), (4, 2),          (3, 5), (5, 6), (5, 8), (6, 8), (6, 7),         (6, 10), (8, 10), (10, 9), (10, 11), (8, 9),         (9, 5), (7, 10), (9, 11), (11, 12), (4, 12)]print(len(edges))G = nx.DiGraph()G.add_edges_from(edges)scc = list(nx.strongly_connected_components(G))print("Strongly Connected Components:")for i in scc:    print(i)meta_graph = nx.condensation(G)pos = nx.spring_layout(meta_graph)nx.draw(meta_graph, pos, with_labels = True, node_size = 1000, node_color = 'skyblue')plt.title("Meta Graph of Strongly Connected Components")plt.show()topological = list(nx.topological_sort(meta_graph))print("Topological Order:")print(topological)nx.draw_kamada_kawai(G, with_labels = True)plt.show()#3G3 = nx.Graph()G3edges = [('A', 'B', 22), ('A', 'C', 9), ('A', 'D', 12),            ('B', 'C', 35), ('C', 'D', 4), ('C', 'E', 65),           ('D', 'E', 33), ('B', 'F', 36), ('C', 'F', 42),           ('E', 'F', 18), ('F', 'G', 39), ('E', 'G', 23),           ('B', 'H', 34), ('F', 'H', 24), ('G', 'H', 25),           ('D', 'I', 30), ('G', 'I', 21), ('H', 'I', 19)]pos = {'A':(0,2), 'B':(1,5), 'C':(1,2), 'D':(1,-1),       'E':(2,1), 'F':(3,3), 'G':(4,1), 'H':(5,5),       'I':(5,-1)}G3.add_weighted_edges_from(G3edges)G3.distance = {('A', 'B'): 22, ('A', 'C'): 9, ('A', 'D'): 12,}edge_labels = nx.get_edge_attributes(G3, "weight")nx.draw(G3, pos, with_labels = True, node_size = 700)nx.draw_networkx_edge_labels(G3, pos, edge_labels)plt.show()#a)print("Dijkstra's Shortest Path")v, path = dijkstra(G3, 'A')print('Visited: ', v)print('Path :', path)#b) Minimum spanning tree for a connected weighted graph#c) Are a shortest path tree and a minimum spanning tree usually #   the same? #d) If the graph has an edge with a negative weight, can you apply #   Dijkstra’s algorithm to find a shortest path tree?