// -- by A_*_A -- //

#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
typedef long long int ll;

//* STRUCT & CLASS DEFINITIONS BEG //
class Graph {
    int V;
    list<int> *adj;
public:
    Graph(int v) {
        V = v;
        adj = new list<int>[v];
    }
    void addEdge(int i, int j, bool undir = true) {
        adj[i].push_back(j);
        if (undir) {
            adj[j].push_back(i);
        }
    }
    void printAdjList() {
        for (int i = 0; i < V; i++) {
            cout << i << ": ";
            for (auto node : adj[i]) {
                cout << node << ", ";
            }
            cout << endl;
        }
    }
};
// STRUCT & CLASS DEFINITIONS END */

//* -- solve function begins -- //
void solve()
{
    Graph g(6);
    g.addEdge(0, 1);
    g.addEdge(0, 4);
    g.addEdge(2, 1);
    g.addEdge(3, 4);
    g.addEdge(4, 5);
    g.addEdge(2, 3);
    g.addEdge(3, 5);
    g.printAdjList();
}
// -- solve function ends -- */

int main()
{
    solve();
    return 0;
}

/* -- INPUT --

*/

/* -- OUTPUT --
0: 1, 4,
1: 0, 2,
2: 1, 3,
3: 4, 2, 5,
4: 0, 3, 5,
5: 4, 3,
*/

// -- by A_*_A -- //
