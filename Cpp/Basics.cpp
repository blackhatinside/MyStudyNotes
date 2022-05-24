// # declare an array of size n with all values as 0
vector<int> (n, 0);

// # length of the array
let sz = arr.size()

// string slicing - substring
String str1 = "HelloWorld";
str1.length();  // 10
str1.substr(3); // str1[3:]
str1.substr(0, 3);  // str1[0:3]

// sum of an array
int summ = 0;
int a[] = { 5, 10, 15 };
accumulate(a, a + 3, summ); // summ = 30

// product of an array
int myfunc(int x, int y) {
    return x * y;
}
int prod = 1;
int a[] = { 5, 10, 15 };
accumulate(a, a + 3, prod, myfunc); // prod = 750
