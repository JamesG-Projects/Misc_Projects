// Programmer:   James Garrett
// Description:  Lab 6 Part A
//


// This is essentially an empty shell

#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct node {
	string name;
	double resistance;
	double voltage;
	double power;
};

int voltage() {
    int volt;
    
    cout << "Enter voltage: ";
    cin >> volt;
    cout << endl;
    
    return volt;
}

int resistance() {
    int resist;
    
    cout << "Enter resistance: ";
    cin >> resist;
    cout << endl;
    
    return resist;
}

int current(int volt, int resist) {
    int curr = volt / resist;
    
    return curr;
}

int power_across(int volt, int curr) {
    int power = volt * curr;
    
    return power;
}

void DisplayNetwork(int volt, int resist, int curr, int power) {
    
    cout << volt << resist << endl;
    
    cout << "Circuit Parameters: " << endl << "Resistance: " << resist << endl << "Voltage: " << volt << endl;
    
    cout << "Current: " << curr << endl << "Power: " << power << endl;
}
int main() {
    int volt;
    int resist;
    int curr;
    int power;
    
    volt = voltage();
    resist = resistance();
    curr = current(volt, resist);
    power = power_across(volt, curr);
    
}