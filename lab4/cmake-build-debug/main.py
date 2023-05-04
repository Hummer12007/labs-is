import networkx as nx
import matplotlib.pyplot as plt

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    graph = []
    color_assignment = []

    mode = None
    for line in lines:
        if line.startswith("Graph:"):
            mode = "graph"
            continue
        elif line.startswith("Color assignment:"):
            mode = "colors"
            continue

        if mode == "graph":
            graph.append([int(x) for x in line.strip().split()])
        elif mode == "colors":
            color_assignment = [int(x) for x in line.strip().split()]

    return graph, color_assignment

def draw_graph(graph, color_assignment):
    G = nx.Graph()

    for i, row in enumerate(graph):
        for j, col in enumerate(row):
            if col == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    node_colors = [color_assignment[node] for node in G.nodes()]

    nx.draw(G, pos, node_color=node_colors, with_labels=True, cmap=plt.cm.jet)
    plt.show()

if __name__ == "__main__":
    file_path = "graph_coloring_output.log"
    graph, color_assignment = read_log_file(file_path)

    if graph and color_assignment:
        draw_graph(graph, color_assignment)
    else:
        print("No solution exists.")
