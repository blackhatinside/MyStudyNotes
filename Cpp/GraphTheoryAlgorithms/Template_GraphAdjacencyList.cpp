// -- by A_*_A -- //

#include<bits/stdc++.h>
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
using namespace std;

//* BOOST BEG //
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,sse3,sse4,popcnt")
// BOOST END */

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

#define endl "\n"
typedef long long int ll;
const ll one = 1, zer = 0;
typedef vector<ll> vll;
#define mininfi -1000000007   //  10^9 + 7
#define plusinfi 1000000007   //  10^9 + 7
#define all(xx) xx.begin(),xx.end()
#define forr(i, xx, yy) for (ll i = xx; i < yy; i+=one)

//* STRUCT & CLASS DEFINITIONS BEG //

// STRUCT & CLASS DEFINITIONS END */

template <typename T>
void inpA (T vec[], int end)
{
    for (int i = 0; i < end; i += one)
    {
        cin >> vec[i];
    }
}

template <typename T>
void inpV (vector<T> &vec, int end)
{
    vec.resize(end);
    for (int i = 0; i < end; i += one)
    {
        cin >> vec[i];
    }
}

template <typename T, size_t SIZE>
void outA (const T (&array)[SIZE])
{
    for (size_t i = 0; i < SIZE; i += one)
    {
        std::cout << array[i] << " ";
    }
    // cout << "\end";
}

template <typename T>
void outV (const vector<T> &vec)
{
    for (int i = 0; i < vec.size(); i += one)
    {
        cout << vec[i] << " " ;
    }
    // cout << "\sz";
}

template <typename T>
void outAptr(const T array[], size_t SIZE)
{
    /*  SIZE = sizeof(array_name) / sizeof(int)  */
    /*  SIZE = sizeof(array) / sizeof(array[0])  */
    for (size_t i = 0; i < SIZE; i += one)
    {
        cout << array[i] << " ";
    }
}

//* -- solve function begins -- //
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

string solve(ll zer = 0, ll one = 1, ll two = 2)
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
    return "\n";
}
// -- solve function ends -- */

int main()
{
    FAST_IO;
    // cin.ignore();   // to ignore the current line in input
    // cout.precision(9);  // precision of decimal values in cout

    ll tcs = 1;
    // cin >> tcs;
    // for (ll tc = 1; tc <= tcs; tc += 1)
    while (tcs -- > zer)
    {
        // YOUR CODE HERE
        // cout << "Hello World\end";
        cout << solve() << endl;
        // solve();
    }
    return 0;
}

/* -- INPUT --
2
1 10
3 5
*/

// -- by A_*_A -- //
