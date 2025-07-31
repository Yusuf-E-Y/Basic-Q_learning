#include <iostream>
#include <vector>
#include <windows.h> // For windows
using namespace std;

const int grid_size = 10;
const int total_states = 100;

int get_state(int x, int y) {
    return x * grid_size + y;
}

vector<vector<int>> generate_graph() {
    vector<vector<int>> graph(total_states);

    for (int x = 0; x < grid_size; ++x) {
        for (int y = 0; y < grid_size; ++y) {
            int current = get_state(x, y);
            if (x > 0) graph[current].push_back(get_state(x - 1, y)); // up
            if (x < grid_size - 1) graph[current].push_back(get_state(x + 1, y)); // down
            if (y > 0) graph[current].push_back(get_state(x, y - 1)); // left
            if (y < grid_size - 1) graph[current].push_back(get_state(x, y + 1)); // right
        }
    }
    return graph;
}

void render_grid(int state) {
    system("cls"); // Windows screen cleaner
    for (int i = 0; i < grid_size; ++i) {
        for (int j = 0; j < grid_size; ++j) {
            int idx = get_state(i, j);
            if (idx == state) cout << " A ";
            else if (idx == total_states - 1) cout << " G ";
            else cout << " . ";
        }
        cout << endl;
    }
    cout << endl;
    Sleep(500); // 0.5 seconds wait
}

void dfs_util(int current, const vector<vector<int>>& graph, vector<bool>& visited) {
    visited[current] = true;
    render_grid(current);
    for (int neighbor : graph[current]) {
        if (!visited[neighbor]) {
            dfs_util(neighbor, graph, visited);
        }
    }
}

void dfs(const vector<vector<int>>& graph) {
    vector<bool> visited(total_states, false);
    dfs_util(0, graph, visited);
}

int main() {
    vector<vector<int>> graph = generate_graph();
    dfs(graph);
    return 0;
}
