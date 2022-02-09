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
