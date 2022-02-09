Scanner scan = new Scanner(System.in);

// 10
// 9 8 7 6 5 4 3 2 1 0
int lim = scan.nextInt();
int[] arr = new int[lim];
int total = 0;
for (int i = 0; i < lim; i += 1) {
    arr[i] = scan.nextInt();
    total += arr[i];
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
String[] arr = sentence.split(" ");
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
