// Student.java
public class Student {
	String name;
	int age;
	int[] marks = new int[3];

	Student (String username, int userage, int usermarks[]) {
		name = username;
		age = userage;
		marks = usermarks.clone();
	}

	static double getaverage (int[] marks) {
		double tot = 0;
		for (int i = 0; i < 3; i++) {
			tot += marks[i];
		}
		return tot / 3;
	}
}

// Application.java
import java.io.*;
import java.lang.*;
import java.util.*;
import java.util.Arrays;
import java.util.HashMap;
public class Application {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<Student> cseA = new ArrayList<>();
		int numberofstudents = scan.nextInt();
		System.out.println("YES");
		scan.nextLine();
		System.out.println(numberofstudents);
		while (numberofstudents-- > 0) {
			String newname = scan.next();
			int newage = scan.nextInt();
			scan.nextLine();
			int[] newmarks = new int[3];
			for (int i = 0; i < 3; i++) {
				newmarks[i] = scan.nextInt();
			}
			Student newcomer = new Student(newname, newage, newmarks);
			cseA.add(newcomer);
		}
		System.out.println(cseA);
		cseA.remove(1);
		System.out.println(cseA);
		System.out.println(cseA.get(1).name);
		int[] arr = new int[] {73, 85, 96};
		System.out.println("Enter roll no:\t");
		int queryindex = scan.nextInt();
		System.out.println(Student.average(csea.get(queryindex).getaverage));
	}
}
