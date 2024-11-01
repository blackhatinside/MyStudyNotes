#include<bits/stdc++.h>
using namespace std;

// struct Car {
// 	string model;
// 	int price;
// } bmw;


/*
	Car* Chevrolet = new Car;
	(*Chevrolet).model = "spark";
	(*Chevrolet).price = 800000;
	cout << Chevrolet->model << endl;
	cout << Chevrolet->price << endl;
*/

class Car {
public:					// by default class vars funcs are pvt.
	string model;
	int price;
} bmw;

/*
	Car* Chevrolet = new Car;
	(*(Chevrolet)).model = "spark";
	(*(Chevrolet)).price = 800000;
	cout << Chevrolet->model << endl;
	cout << Chevrolet->price << endl;
*/

// C++ Templates
template <class T1, class T2>
class Calculator {
public:
	T1 x, y;
	Calculator(T1 a, T2 b) {
		x = a;
		y = b;
	}
	T1 add() {
		return x + y;
	}
	T2 mul(T1 a, T2 b) {
		return a * b;
	}
};

/*
	Calculator <int, int> calc(2, 4);
	cout << calc.add() << endl;
	cout << calc.mul(3, 5) << endl;
*/

// Base Class
class Animal {
public:
	int age;

	// constructor
	Animal() {
		age = 0;
		cout << "Animal Object created..." << endl;
	}

	void eat() {
		cout << "Eating..." << endl;
	}

	virtual void speak() {
		cout << "Speaking..." << endl;
	}	// virtual keyword enables overriding for the method

	// setter functions
	void setAge(int animalAge) {
		age = animalAge;
	}	// const keyword promises that the method wont modify object state

	// getter functions
	int getAge() const {
		cout << "Called Animal::getAge()" << endl;
		return age;
	}

	// destructor
	virtual ~Animal() {
		cout << "ANIMAL killed!" << endl;
	}
};

class Human : public Animal {
// private:
	string name;

public:
	// Overriding
	void speak() override {
		cout << "Talking..." << endl;
	}	// override keyword optional

	// Polymorphism
	void speak(string greeting) {
		cout << "Talking... " + greeting << endl;
	}

	// setter function
	void setName(string humanName) {
		name = humanName;
	}

	// getter function
	string getName() {
		return name;
	}
};

class Cat: protected Animal {
public:
	// Overriding
	void speak() override {
		cout << "Meowing..." << endl;
	}

	// setter function
	void set_catAge(int catAge) {
		setAge(catAge);
	}

	// getter function
	int get_catAge() {
		cout << "Called Cat::getAge()" << endl;
		return getAge();
	}

	~Cat() {
		cout << "CAT killed!" << endl;
	}
};

// private inheritance by default
class Dog : Animal {
public:
	Dog() {
		age = 5;
	}

	// Overriding
	void speak() override {
		cout << "Barking..." << endl;
	}

	// Overriding getter function
	int getAge() {
		cout << "Called Dog::getAge()" << endl;
		return age;
	}
};

class Dummy2 {
public:
	int dummyint = 5;
	~Dummy2() {
		cout << "DUMMY2 killed!" << endl;
	}
};

class Puppy : public Dog {
public:
	int get_puppyAge() {
		cout << "Called Puppy::getAge()" << endl;
		return getAge();
	}
};

class Dummy {
public:
	int dummyint = 5;
	~Dummy() {
		cout << "DUMMY killed!" << endl;
	}
};

int main() {

	Dummy d1;
	Human h;
	Dummy2 d2;
	h.setName("Adithya");
	h.setAge(24);
	cout << h.getName() << endl;
	cout << h.getAge() << endl;
	h.eat();
	h.speak();
	h.speak("Hello");
	// cout << h.name << endl;

	cout << endl;

	Cat c;
	// c.age = 5;	// cant access protected members
	// c.eat();		// cant access protected members
	// cout << c.getAge() << endl;		// cant access protected members
	c.speak();
	c.set_catAge(2);
	cout << c.get_catAge() << endl;

	cout << endl;

	Dog d;
	// d.age = 5;		// cant access private members
	// cout << d.setAge(5) << endl;	// cant access private members
	d.speak();
	cout << d.getAge() << endl;

	cout << endl;

	Puppy p;
	// p.age = 1;		// cant access private members
	cout << p.get_puppyAge() << endl;
}

/*

Classes and Objects: Instances, Data + Methods
Encapsulation: access specifiers
Abstraction: abstract classes
Polymorphism: multiple functions with same name but different parameters

Public:
	accessible from anywhere
Protected:
	accessible within class and derived class
	used to provide access to derived classes, but hidden from external code
Private:
	accessible within class only

Public Inheritance:
	Public members -> Public members
	Protected members -> Protected members
	Private members NOT ACCESSIBLE

Protected Inheritance:
	Public members -> Protected members
	Protected members -> Protected members
	Private members NOT ACCESSIBLE

Private Inheritance:
	Public members -> Private members
	Protected members -> Private members
	Private members NOT ACCESSIBLE

*/