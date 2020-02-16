// Programmer:   James Garrett
// Description:  Lab 06 Part A/B Code

#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct node {
    string name;
    double resistance;
    double voltage_across;
    double power_across;
};

string nodeName() {
    string node_name;
    cout << "Enter Node Name: ";
    cin >> node_name;
   
    return node_name;
}

//Voltage Function
int voltage() {
    // Enter source voltage
    double source_voltage;
    cout << "Enter Source Voltage: ";
    cin >> source_voltage;
    
    return source_voltage;
}

//Resistance Function
int nodeResistance() {
    double resistance;
    // Enter basic Node Information
    //N1.name = nodeName();
    cout << "Resistor Value: ";
    cin >> resistance;
   
   return resistance;
}

//Current Function
double seriesCurrent(double source_voltage, double resistance){
    double total_resistance;
    // Calculate series current for the one-node network
    total_resistance = resistance;
    double series_current = source_voltage / total_resistance;

    return series_current;
}

//Voltage Across the Resistor Function
int voltageAcross(double series_current, double resistance) {
    double voltage_across;
        // Calculate voltage across the restistor 
    voltage_across = series_current * resistance;
    
    return voltage_across;
}

//Calculating the Power
double power(double voltage_across, double series_current) {
    double power_across;
    // Calculate the power across the resistor
    power_across = voltage_across * series_current;
    
    return power_across;
}

//Calculating total Resistance
double totalResistance(vector<node> resistorList) {
    int sum = 0;
    for (int i = 0; i < resistorList.size(); i++) {
        sum = sum + resistorList.at(i).resistance;
    }
    
    return sum;
}

//DisplayNetwork
void network(double source_voltage, double total_resistance, double series_current, double totalPower, vector<node> N1) {
    
    // Display Network Information
    cout << "Series Network: " << endl;
    cout << "Source Voltage: " << source_voltage << "-Volts" << endl;
    cout << "Total Resistance: " << total_resistance << "-Ohms" << endl;
    cout << "Series Current: " << series_current << "-Amperes" << endl;
    cout << "Total Power: " << totalPower << "-Watts" << endl;
    
    // Display Node information
    //cout << "Node Name: " << N1.name << endl;
    for (int i = 0; i < N1.size(); i++) {
    cout << "Node Voltage: " << N1.at(i).voltage_across << "-Volts" << endl;
    cout << "Node Resistance: " << N1.at(i).resistance << "-Ohms" << endl;
    cout << "Node Power: " << N1.at(i).power_across << "-Watts" << endl;
    }
    
}

int main() {
    node N1;
    
    vector<node> resistorList;
    
    double resistance;
    double inputVoltage;
    double current;
    
    inputVoltage = voltage();

    do {
        N1.name = nodeName();
        N1.resistance = nodeResistance();
        resistorList.push_back(N1);
    } while (N1.resistance != 0);
    resistorList.pop_back();
    
    double sum;
    sum = totalResistance(resistorList);
    
    double series_current;
    series_current = seriesCurrent(inputVoltage, sum);
    
    for (int i = 0; i < resistorList.size(); i++) {
    resistorList.at(i).voltage_across = voltageAcross(series_current, resistorList.at(i).resistance);
    resistorList.at(i).power_across = power(resistorList.at(i).voltage_across, series_current);
    } 
    
    double totalPower = power(inputVoltage, series_current);
    
    //Display Final Circuit Values
    network(inputVoltage, sum, series_current, totalPower, resistorList);
    
    return 0;
}
