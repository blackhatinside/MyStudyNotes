// https://atcoder.jp/contests/agc005/tasks/agc005_a
#include<bits/stdc++.h>
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
using namespace std;

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

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

int main()
{
    FAST_IO;
    cout << solve();
    return 0;
}
