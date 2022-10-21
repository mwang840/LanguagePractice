#include <iostream>
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> graph;
vector<bool> visited;
vector<int>result;

void dfs(int n){
    visited[n] = true;
    result.push_back(n);
    for(int i = 0; i < graph[n].size(); ++i){
        if(!visited[graph[n][i]]){
            dfs(graph[n][i]);
        }
    }
}
int main(){
    int m, n;
    std::cin>>m;
    std::cin>>n;
    visited = vector<bool>(n);
    graph.resize(m);
    for(int i = 0; i < n; ++i){
        int a, b;
        std::cin >> a >> b;
        a--;
        b--;
        graph[a].push_back(b);
    }

    for(int j = 0; j < n; ++j){
        if(!visited[j]){
            dfs(j);
        }

    }
    for(int i = 0; i < result.size(); ++i){
        cout<< result[i]<< " ";
    }

}