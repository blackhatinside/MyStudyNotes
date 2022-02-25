// https://atcoder.jp/contests/agc005/tasks/agc005_a
import java.io.*;
import java.lang.*;
import java.util.*;

public class Main { // atcoder - Main; codechef - Main;
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] w = scan.nextLine().toCharArray();
		Stack<Character> stack = new Stack<>();
		for (Character x : w) {
			if ((stack.size() == 0) || !(Character.compare(stack.peek(), 'S') == 0 && Character.compare(x, 'T') == 0)) {
				stack.push(x);
			} else {
				stack.pop();
			}
		}
		int ans = stack.size();
		System.out.println(ans);
	}
}

