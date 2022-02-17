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
        cin >> vec[i] ;
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
    // cout << "\end";
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

vector<long long int> sievePrime(int end)   //  return array of prime numbers <= n
{   /*    SIEVE OF ERATOSTHENES    */
    vector<long long int> primes(end + 1, 1);
    // primes.reserve(end);
    primes[0] = primes[1] = 0;
    for (int i = 4; i <= end + 1; i += 2)
    {
        primes[i] = 0;
    }
    for (int i = 3; i * i <= end + 1; i += 2)
    {
        if (primes[i] == 1)
        {
            for (int x = i * i; x <= end + 1; x += i)
                primes[x] = 0;
        }
    }
    return primes;
}

auto segmentedSieve(int beg, int end)   // printing all primes in range [beg....end]
{
    const int S = 100000000;
    vector<int> primes;
    int nsqrt = sqrt(end);
    vector<char> is_prime(nsqrt + 2, true);
    for (int i = 2; i <= nsqrt; i++)
    {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * i; j <= nsqrt; j += i)
                is_prime[j] = false;
        }
    }

    // int result = 0;
    vector<char> block(S);
    for (int k = 0; k * S <= end; k++)
    {
        fill(block.begin(), block.end(), true);
        int start = k * S;
        for (int p : primes)
        {
            int start_idx = (start + p - 1) / p;
            int j = max(start_idx, p) * p - start;
            for (; j < S; j += p)
                block[j] = false;
        }
        if (k == 0)
            block[0] = block[1] = false;
        for (int i = beg; i < S && start + i <= end; i++) {
            if (block[i])
                // result++;
                cout << i << endl;
        }
    }
    // return result;
}

auto solve()
{
    ll end, beg; cin >> beg >> end;
    segmentedSieve(beg, end);
    return "\n";
}
// -- solve function ends -- */

int main()
{
    FAST_IO;
    // cin.ignore();   // to ignore the current line in input
    // cout.precision(9);  // precision of decimal values in cout

    ll tcs = one; cin >> tcs;
    // for (ll tc = 1; tc <= tcs; tc += 1)
    while (tcs -- > zer)
    {
        // YOUR CODE HERE
        // cout << "Hello World\end";
        // cout << solve() << endl;
        cout << solve();
    }
    return 0;
}

/* -- INPUT --
2
1 10
3 5
*/

// -- by A_*_A -- //
