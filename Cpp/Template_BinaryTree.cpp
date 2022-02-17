// -- by cyberkid05 -- //

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
#define forr(i, xx, yy) for (ll i = xx; i < yy; i++)

//* STRUCT & CLASS DEFINITIONS BEG //
struct Node
{
    int val;
    vector<Node *> children;
};

Node *newNode(int key)
{
    Node *temp = new Node;
    temp->val = key;
    return temp;
}

class Solution
{
// Input: root = [1,null,3,2,4,null,5,6]
// Output: [[1],[3,2,4],[5,6]]
public:
    vector<int> nodes;  // to store the answer

    auto traversalUtil(Node* root)
    {
        if (!root)
            return;

        // if (nodes.size() == depth)   // depth is used for level order traversal
        //     nodes.push_back(vector<int>());

        for (auto child : root -> children)
            traversalUtil(child);

        nodes.push_back(root -> val);

        // if (root -> left)
        // traversalUtil(root -> left);

        // if (root -> right)
        // traversalUtil(root -> right);
    }

    vector<int> postorder(Node* root)
    {
        nodes.clear();
        traversalUtil(root);
        return nodes;
    }
};
// STRUCT & CLASS DEFINITIONS END */

template <typename T>
void inpA (T arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
}

template <typename T>
void inpV (vector<T> &vec, int n)
{
    vec.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin >> vec[i] ;
    }
}

template <typename T, size_t SIZE>
void outA (const T (&array)[SIZE])
{
    for (size_t i = 0; i < SIZE; i++)
    {
        std::cout << array[i] << " ";
    }
    // cout << "\n";
}

template <typename T>
void outV (const vector<T> &vec)
{
    for (int i = 0; i < vec.size(); i++)
    {
        cout << vec[i] << " " ;
    }
    // cout << "\n";
}

template <typename T>
void outAptr(const T array[], size_t SIZE)
{
    /*  SIZE = sizeof(array_name) / sizeof(int)  */
    /*  SIZE = sizeof(array) / sizeof(array[0])  */
    for (size_t i = 0; i < SIZE; i++)
    {
        cout << array[i] << " ";
    }
}

//* -- solve function begins -- //
auto solve()
{
    /*   Let us create below tree
    *              10
    *        /   /    \   \
    *        2  34    56   100
    *       / \         |   /  | \
    *      77  88       1   7  8  9
    */
    Node *root = newNode(10);
    (root->children).push_back(newNode(2));
    (root->children).push_back(newNode(34));
    (root->children).push_back(newNode(56));
    (root->children).push_back(newNode(100));
    (root->children[0]->children).push_back(newNode(77));
    (root->children[0]->children).push_back(newNode(88));
    (root->children[2]->children).push_back(newNode(1));
    (root->children[3]->children).push_back(newNode(7));
    (root->children[3]->children).push_back(newNode(8));
    (root->children[3]->children).push_back(newNode(9));
    Solution *obj = new Solution;
    outV(obj->postorder(root));
    return "";
}
// -- solve function ends -- */

int main()
{
    FAST_IO;
    // cin.ignore();   // to ignore the current line in input
    // cout.precision(9);  // precision of decimal values in cout

    // ll tcs = one; cin >> tcs;
    // for (ll tc = 1; tc <= tcs; tc += 1)
    // while (tcs -- > zer)
    {
        // YOUR CODE HERE
        // cout << "Hello World\n";
        // cout << solve(); cout << endl;
        // cout << solve();
        cout << solve() << endl;
    }
    return 0;
}

// -- by cyberkid05 -- //
