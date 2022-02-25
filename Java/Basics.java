/*

Java is a verbose programming language.
Java is platform independent.
All code in Java is defined in classes.
Java constants can be initialized using public static final variable_name.  
Compilation: Source Code to Byte Code (Creates a executable class file)
{} can be used for creating scopes in the program

*/

##################################################

// System.out.println("Hello World");	// using print() will not throw "\n"
// print("Hello World")

// string1.toCharArray();
// list(string1)

// string1.length();
// len(string1)

// String1.toCharArray().length;
// len(list(string1))

// string1.indexOf("A");
// string1.find("A")

// string1.charAt(index);
// string1[index]

// boolean flag = true
// bool flag = True

// int tcs = Integer.parseInt(br.readLine);
// tcs = int(input())

// Arrays.sort(arr1);
// arr1.sort()

// string1.equals(string2);
// string1 == string2

// string1.contains("abc")
// "abc" in string1

// string1.toLowerCase()
// string1.lower()

// character1.isLowerCase()
// character1.islower()

// Math.abs(4 - 5)
// abs(4 - 5)

// (Character.compare('a', 'b') == 0)
// 'a' == 'b'

// Map<Character, Integer> hp = new HashMap<>();
// hp.containsKey(key1); hp.put(key1, value1); int xx = hp.get(key1);
// hp = collections.defaultdict(lambda: 0)
// hp[key1] = value1; xx = hp[key1];

// StringBuilder sb = new StringBuilder();
// string word = sb.append("Valid\n");

// --------------------------------------------------
// ARRAY LIST
// -	add(index = n, element)
// -	addAll(oldarr)
// -	get(index)
// -	set(index, newvalue)
// -	remove(index)
// -	remove(Integer.valueOf(30))
// -	size()
// -	clear()
// STACK
// -	push(element)
// -	pop()
// -	peek()

// QUEUE
// -	offer(element)
// -	poll()
// -	peek()

// SET
// - 	add(element)
// - 	remove(element)
// - 	contains(element)
// - 	isEmpty()
// --------------------------------------------------

##################################################

Scanner scan = new Scanner(System.in);

// 10 helloworld
int lim = scan.nextInt();
String word = scan.next();
System.out.println(lim);
System.out.println(word);
// 10
// helloworld

// 10
// 9 8 7 6 5 4 3 2 1 0
int lim = scan.nextInt();
int[] arr = new int[lim];
int total = 0;
for (int i = 0; i < lim; i += 1) {
    arr[i] = scan.nextInt();
}
for (int num : arr) {
    total += num;
}
System.out.println(total);
// 45

// 10
// if it were your girl would you still allow that
int lim = scan.nextInt();
String[] arr = new String[lim];
for (int i = 0; i < lim; i += 1) {
    arr[i] = scan.next();
    System.out.print(arr[i]);
}
// ifitwereyourgirlwouldyoustillallowthat

// 10
// if it were your girl would you still allow that
int num = scan.nextInt();
scan.nextLine();
String sentence = scan.nextLine();
String[] arr = sentence.split("\\s");
for (String ele : arr) {
    System.out.println(ele);
}
// if
// it
// were
// your
// girl
// would
// you
// still
// allow
// that

// HelloWorld
String word = scan.nextLine();
char[] letters = word.toCharArray();
for (char letter : letters) {
    System.out.print(letter + " ");
}
// H e l l o W o r l d 
