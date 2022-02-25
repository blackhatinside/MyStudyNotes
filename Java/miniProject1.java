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

// ##################################################

// Vehicle.java
enum VehicleOutline {
	username,
	vehicleID,
	wheeler;
}

public class Vehicle {
	String username;
	int vehicleID;
	int wheeler;

	Vehicle (String uname, int vID, int vWheeler) {
		this.username = uname;	// 'this' keyword is not mandatory
		this.vehicleID = vID;
		this.wheeler = vWheeler;
	}
	@Override
	public String toString() {
		return username + " " + wheeler + "-wheeler " + vehicleID;
	}
}

// Applicationjava
import java.io.*;
import java.lang.*;
import java.util.*;
public class Application {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Vehicle> lane1 = new Stack<>();
		int choice = -1;
		while (choice != 0) {
			System.out.println("\nParking System\n1. Add a Vehicle\n2. Remove a Vehicle\n3. Number of Vehicles\n4. Peek into last Vehicle\n5. Exit\nEnter your choice: ");
			choice = scan.nextInt(); scan.nextLine();
			switch (choice) {
			case 1: {
				String givenName = scan.next();
				int givenID = scan.nextInt();
				int givenwheels = scan.nextInt();
				scan.nextLine();
				lane1.push(new Vehicle(givenName, givenID, givenwheels));
				System.out.println("Vehicle added to lane!");
				break;
			}
			case 2: {
				System.out.println("Vehicle removed from lane!");
				lane1.pop();
				break;
			}
			case 3: {
				System.out.println("Displaying lane details.");
				System.out.println("\n" + lane1.size() + " vehicles found!\n");
				System.out.println(lane1);
				break;
			}
			case 4: {
				System.out.println("Peeking into the last vehicle.");
				System.out.println(lane1.peek());
			}
			case 5: {
				System.out.println("Exiting from program.");
				choice = 0;
				break;
			}
			default: {
				System.out.println("Invalid Input!");
			}
			}
		}
	}
}
