//James Garrett
//LAB07 3/22/2018

#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

bool isEven(int num) {
    if (num % 2 == 0) {
        return true;
    }
    else {
        return false;
    }
}

bool isOdd(int num) {
    if (isEven(num)) {
        return false;
    }
    else {
        return true;
    }
}

bool isPrime(int num) {
    
    bool prime = true;
    
    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
            prime = false;
            return prime;
        }
    }
    return true;
}

int min(vector<int> vec) {
    
    int minVal;
    
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] < minVal) {
            minVal = vec[i];
        }
    }
    return minVal;
}

int max(vector<int> vec) {
    
    int maxVal = 0;
    
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] > maxVal) {
            maxVal = vec[i];
        }
    }
    return maxVal;
}

int sum(vector<int> vec) {
    
    int sumVal = 0;
    
    for (int i = 0; i < vec.size(); i++) {
        sumVal += vec[i];
        }
    return sumVal;
}

double mean(double sum, double count) {
    double meanVal = sum/count;
    return meanVal;
}

float stddev(double meanVal, const vector<int> vec) {

    double mean = 0;
    vector<int> vec2;
  
  if (vec.size() > 0) {
    mean = meanVal;
  }
  else {
    return 0;
  }
  
  for (int i = 0; i < vec.size(); i++) {
    vec2.push_back(pow((vec[i] - mean),2));
  }
  
  double sumVal = 0;
    
    for (int i = 0; i < vec2.size(); i++) {
        sumVal += vec2[i];
        }
        
  double k = sum(vec2)/vec2.size();
  return sqrt(k);
}

int main() {
    
    //Initializing variables----------------------------------------------------
    vector<int> vec;
    ifstream inFile;
    inFile.open("input.txt");
    
    //Checking to see if input.txt was opened-----------------------------------
    if (!inFile.is_open()) {
      cout << "Could not open file input.txt." << endl;
      
      return 1;
   }
   
   //Reading the numbers from input.txt into a vector---------------------------
   int x;
   int count = 0;
   while (inFile >> x) {
       count += 1;
       vec.push_back(x);
    }
    
    cout << "Count: " << count << endl;
    cout << "Vector Size: " << vec.size() << endl;
    
    //Can close input.txt now---------------------------------------------------
    inFile.close();
    
    //isEven loop---------------------------------------------------------------
    bool even;
    int numEven = 0;
    ofstream outFile;
    outFile.open("evens.txt");
    
    for (int i = 0; i < vec.size(); i++) {
        even = isEven(vec.at(i));
        if (even) {
            ++numEven;
            outFile << vec.at(i);
            outFile << endl;
        }
    }
    
    cout << "Even Numbers: " << numEven << endl;
    
    //Can close evens.txt now---------------------------------------------------
    outFile.close();
    
    //isOdd loop----------------------------------------------------------------
    bool odd;
    int numOdd = 0;
    outFile.open("odds.txt");
    
    for (int i = 0; i < vec.size(); i++) {
        odd = isOdd(vec.at(i));
        if (odd) {
            ++numOdd;
            outFile << vec.at(i);
            outFile << endl;
        }
    }
    
    cout << "Odd Numbers: " << numOdd << endl;
    
    //Can close odds.txt now----------------------------------------------------
    outFile.close();
    
    //isPrime loop
    bool prime;
    int numPrime = 0;
    outFile.open("primes.txt");
    
    for (int i = 0; i < vec.size(); i++) {
        prime = isPrime(vec.at(i));
        if (prime) {
            ++numPrime;
            outFile << vec.at(i);
            outFile << endl;
        }
    }
    
    cout << "Prime Numbers: " << numPrime << endl;
    
    //Can close primes.txt now--------------------------------------------------
    outFile.close();
    
    //Finding Max, Min, Sum, Mean, and StdDev-----------------------------------
    int minVal;
    minVal = min(vec);
    
    cout << "Min number: " << minVal << endl;
    
    int maxVal;
    maxVal = max(vec);
    
    cout << "Max number: " << maxVal << endl;
    
    int sumVal;
    sumVal = sum(vec);
    
    cout << "Sum: " << sumVal << endl;
    
    double meanVal;
    meanVal = mean(sumVal, count);
    
    cout << "Mean: " << meanVal << endl;
    
    double stdDev;
    stdDev = stddev(meanVal, vec);
    
    cout << "Standard Deviation: " << stdDev << endl;
    
    
  return 0;
}
