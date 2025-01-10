class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
           vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<bool> visited(n, false);
    stack<int> s;
    s.push(source);

    while (!s.empty()) {
        int current = s.top();
        s.pop();

        if (current == destination) {
            return true;
        }

        if (!visited[current]) {
            visited[current] = true;
            for (int neighbor : graph[current]) {
                if (!visited[neighbor]) {
                    s.push(neighbor);
                }
            }
        }
    }

    return false;
    }
};