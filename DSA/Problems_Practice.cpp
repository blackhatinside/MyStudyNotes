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

//* -- solve function begins -- //
auto solve()
{
    string w; cin >> w;
    stack<char> arr;
    for (char x : w)
    {
        if (arr.size() == 0 or !(arr.top() == 'S' and x == 'T'))
        {
            arr.push(x);
        }
        else
        {
            arr.pop();
        }
    }
    cout << arr.size();
    return "\n";
}
// -- solve function ends -- */

int main()
{
    FAST_IO;
    cout << solve();
    return 0;
}
