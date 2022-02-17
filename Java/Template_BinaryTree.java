import java.io.*;
import java.lang.*;
import java.util.*;
import java.util.Arrays;
import java.util.HashMap;

class Node {
	int val;
	Node left = null;
	Node right = null;
	Node (int value) {
		val = value;
	}
}

class BinaryTree {
	Node root = null;
	public void inorderTraversal(Node root) {
		if (root == null) return;
		inorderTraversal(root.left);
		System.out.println(root.val);
		inorderTraversal(root.right);
	}
}

public class Application {
	public static String solve(int a, int b) {
		Triangle myTriangle = new Triangle(a, b);
		System.out.println(Triangle.numofsides);
		System.out.println(myTriangle.findArea());
		return "\n";
	}
	public static void main(String[] args) {
		try {
			System.setIn(new FileInputStream("inputf.txt"));
			System.setOut(new PrintStream(new FileOutputStream("outputf.txt")));
		} catch (Exception e) {
			System.err.println("Error");
		}

		Scanner scan = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int z = 0, tcs = 1;
		// tcs = scan.nextInt();
		while (tcs-- > 0) {
			BinaryTree tree = new BinaryTree();
			tree.root = new Node(1);
			tree.root.left = new Node(2);
			tree.root.right = new Node(3);
			tree.root.left.left = new Node(4);
			tree.root.left.right = new Node(5);
			tree.inorderTraversal(tree.root);
		}
	}
}
