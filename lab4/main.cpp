#include <algorithm>
#include <ctime>
#include <iostream>
#include <random>
#include <vector>
#include <ostream>
#include <fstream>

// The rest of the code


#define NUM_VERTEX 100
#define NUM_EDGES 100
#define NUM_COLORS 3


std::vector<std::vector<int>> generate_random_graph(int num_vertices=NUM_VERTEX, int num_edges=NUM_EDGES) {
    std::vector<std::pair<int, int>> all_possible_edges;

    for (int i = 0; i < num_vertices; ++i) {
        for (int j = i + 1; j < num_vertices; ++j) {
            all_possible_edges.emplace_back(i, j);
        }
    }

    if (num_edges > all_possible_edges.size()) {
        std::cerr << "Error: Too many edges for the given number of vertices." << std::endl;
        return std::vector<std::vector<int>>();
    }

    // Shuffle the edges using Fisher-Yates algorithm
    std::mt19937 rng(static_cast<unsigned int>(std::time(nullptr)));
    for (int i = all_possible_edges.size() - 1; i > 0; --i) {
        std::uniform_int_distribution<int> distribution(0, i);
        int j = distribution(rng);
        std::swap(all_possible_edges[i], all_possible_edges[j]);
    }

    std::vector<std::vector<int>> graph(num_vertices, std::vector<int>(num_vertices, 0));
    for (int i = 0; i < num_edges; ++i) {
        int u = all_possible_edges[i].first;
        int v = all_possible_edges[i].second;
        graph[u][v] = 1;
        graph[v][u] = 1;
    }

    return graph;
}
bool is_safe(int vertex, int color, const std::vector<std::vector<int>>& graph, const std::vector<int>& color_assignment) {
    for (int neighbor = 0; neighbor < graph.size(); ++neighbor) {
        if (graph[vertex][neighbor] == 1 && color_assignment[neighbor] == color) {
            return false;
        }
    }
    return true;
}

bool graph_color_util(const std::vector<std::vector<int>>& graph, int num_colors, std::vector<int>& color_assignment, int vertex) {
    if (vertex == graph.size()) {
        return true;
    }

    for (int color = 1; color <= num_colors; ++color) {
        if (is_safe(vertex, color, graph, color_assignment)) {
            color_assignment[vertex] = color;

            if (graph_color_util(graph, num_colors, color_assignment, vertex + 1)) {
                return true;
            }

            color_assignment[vertex] = 0;
        }
    }

    return false;
}

std::vector<int> graph_coloring(const std::vector<std::vector<int>>& graph, int num_colors) {
    std::vector<int> color_assignment(graph.size(), 0);

    if (!graph_color_util(graph, num_colors, color_assignment, 0)) {
        return std::vector<int>{};
    }

    return color_assignment;
}

int main() {
    std::vector<std::vector<int>> graph = generate_random_graph();

    int num_colors = NUM_COLORS;
    std::vector<int> color_assignment = graph_coloring(graph, num_colors);

    // Save the graph and color assignment to a log file
    std::ofstream log_file("graph_coloring_output.log");
    if (!color_assignment.empty()) {
        log_file << "Graph:\n";
        for (const auto& row : graph) {
            for (int cell : row) {
                log_file << cell << " ";
            }
            log_file << "\n";
        }
        log_file << "\nColor assignment:\n";
        for (int color : color_assignment) {
            log_file << color << " ";
        }
        log_file << std::endl;
    } else {
        log_file << "No solution exists." << std::endl;
    }
    log_file.close();

    return 0;
}
