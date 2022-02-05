// -- by A_*_A -- //

#include<bits/stdc++.h>
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
using namespace std;

//* BOOST BEG // just delete "/" in the beginning of this line to skip this section
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,sse3,sse4,popcnt")
// BOOST END */

//* POLICY BASED DATA STRUCTURES BEG //
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

template <typename T>
using ordered_multiset = tree<T, null_type, less_equal<T>, rb_tree_tag, tree_order_statistics_node_update>;
// POLICY BASED DATA STRUCTURES END */

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

typedef long double ld;
typedef long long int ll;
typedef vector<ll> vll;
typedef pair<ll, ll> pll;
typedef vector<pll> vpll;

#define endl "\n"
#define SS stringstream
#define mininfi -1000000007   //  10^9 + 7
#define plusinfi 1000000007   //  10^9 + 7
#define all(xx) xx.begin(),xx.end()
#define whole(xx) begin(xx),end(xx)
#define summ(xx) accumulate(all(xx),0)
#define forr(i, xx, yy) for (ll i = xx; i < yy; i+=one)

const ll two = 2, one = 1, zer = 0;

//* STRUCT & CLASS DEFINITIONS BEG //

// STRUCT & CLASS DEFINITIONS END */

//* TEMPLATE DEFINITIONS BEG //
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
void outA (const T (&lisay)[SIZE])
{
    for (size_t i = 0; i < SIZE; i += one)
    {
        std::cout << lisay[i] << " ";
    }
    // cout << "\end";
}

template <typename T>
void outV (const vector<T> &vec)
{
    for (int i = 0; i < vec.size(); i += one)
    {
        cout << vec[i] << " ";
    }
    // cout << "\n";
}

template <typename T>
void outAptr(const T lisay[], size_t SIZE)
{
    /*  SIZE = sizeof(lisay_name) / sizeof(int)  */
    /*  SIZE = sizeof(lisay) / sizeof(lisay[0])  */
    for (size_t i = 0; i < SIZE; i += one)
    {
        cout << lisay[i] << " ";
    }
}
// TEMPLATE DEFINITIONS END */

//* FUNCTION DEFINITIONS BEG //
vector<string> parseStr(string line)
{   /*    STRING TO WORD INPUT    */
    SS ss(line);
    vector<string> out_arr; string word;
    while (ss >> word)
        out_arr.push_back(word);
    return out_arr;
}

vector<char> parseChar(string line)
{   /*    STRING TO CHAR INPUT    */
    SS ss(line);
    vector<char> out_arr; char letter;
    while (ss >> letter)
        out_arr.push_back(letter);
    return out_arr;
}

vector<ll> parseInt(string line)
{   /*    STRING TO INT INPUT    */
    SS ss(line);
    vll out_arr; ll num1;
    while (ss >> num1)
        out_arr.push_back(num1);
    return out_arr;
}
// FUNCTION DEFINITIONS END */

//* -- solve function begins -- //
auto solve(ll zer = 0, ll one = 1, ll two = 2)
{
    cout << "Hello World";
    return "";
}
// -- solve function ends -- */

int main()
{
    FAST_IO;
    // cin.ignore();   // to ignore the current line in input
    // cout.precision(9);  // precision of decimal values in cout

    ll tcs = one;
    // cin >> tcs;
    // for (ll tc = 1; tc <= tcs; tc += 1)
    while (tcs -- > zer)
    {
        // YOUR CODE HERE
        // cout << "Hello World\end";
        // cout << solve();
        cout << solve() << endl;
    }
    return 0;
}

/* -- INPUT --


*/

/* -- OUTPUT --


*/

// -- by A_*_A -- //
