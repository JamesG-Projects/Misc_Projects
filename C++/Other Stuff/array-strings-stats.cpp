/*
Name: James Garrett
Date: 2/22/2018
Assignment: Lab 05
Description: Array, Vectors, and String Stats
*/


#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


bool find(int array[], int length, int value){
  bool ans = 0;
  
  for (int i = 0; i < length; i++) {
    if (array[i] == value) 
    {
    ans = 1;
    }
  }
return ans;
}

bool isSorted(int array[], int length){
  bool ans = 0;
  int length2 = 0;
  vector<int> array2;
  
  for (int i = 0; i < length - 1; i++) {
    if (array[i+1] >= array[i])
    {
      ans = 1;
      array2.push_back(ans);
    }
    else {
      ans = 0;
      break;
    }
  }
  
  /*int size = sizeof(array);
  if (array2.size() < size) {
     return 0;
  }
   else {
   return ans;
   }
   */
   
   return ans;
}

void reverse(vector <int> &reverse_me) { 
  
  int initial;

  for (int i = 0; i < (reverse_me.size() / 2); i++) {
    initial = reverse_me[i];
    reverse_me[i] = reverse_me[reverse_me.size() - 1 - i];
    reverse_me[reverse_me.size() - 1 - i] = initial;
  }
}

float mean(const vector <float> values) {
  float nums = 0;
  float count = 0;
  float meanNums = 0;
  
  if (values.size() == 0) {
    return 0;
  }
  else {
  for (int i = 0; i < values.size(); i++) {
    nums += values[i];
    count += 1;
  }
  meanNums = nums / count;
  
  return meanNums;
}
}

float stddev(const vector <float> values) { 
  float Mean;
  vector<float> values2;
  if (values.size() > 0) {
    Mean = mean(values);
  }
  else {
    return 0;
  }
  
  for (int i = 0; i < values.size(); i++) {
    values2.push_back(pow((values.at(i) - Mean),2));
  }
  float k = mean(values2);
  return sqrt(k);
}

bool find(vector<int> array, int value) {
  bool ans = 0;
  vector<int> array2;
  
  for (int i = 0; i < array.size(); i++) {
    if (array.at(i) == value) {
      ans = 1;
      array2.push_back(ans);
    }
  }
  return ans;
}

vector<int> removeDups(vector<int> array) {
  vector<int> array2;
  int size = array.size();
  
  for (int i = 0; i < array.size(); i++) {
    if (!find(array2, array.at(i))) {
        array2.push_back(array.at(i));
      }
    }
  return array2;
}

// Strings 
unsigned int countUpperCaseChars(const string &countme){
  int capCount(0);
  
  for (char c: countme) {
    if (isupper(c)) {
      ++capCount;
    }
  }
  return capCount;
}

unsigned int numWords(const string &countme) {
  if(countme.size() == 0){
    return 0.0;
  }
  else {
    int words = 0;
    for (int i = 0; i < countme.size() - 1; ++i) {
      if (isalpha(countme.at(i))) {
        for (i; isalpha(countme.at(i)) && i < countme.size() - 1; ++i) {
        }
        words++;
      }
    }
    return words;
  }
}

string convertToUpper(string &to_be_converted){
  if  (to_be_converted.length() > 0) {
  for (int i = 0; i < to_be_converted.size(); i++) {
    to_be_converted[i] = toupper(to_be_converted[i]);
  }
  return to_be_converted;
  }
  else {
  return to_be_converted;
  }
}

string removeSpaces(const string &remove_from_me){
  string removedSpaces;
  int count = 0;
  int size = remove_from_me.size();
  
  if (remove_from_me == "") {
     return remove_from_me;
  }
  else {
  for (int i = 0; i < (size); i++) {
     removedSpaces.resize(size - count);
     removedSpaces[i - count] = remove_from_me[i];
     
     if (isspace(remove_from_me[i])) {
        removedSpaces.pop_back();
        count++;
     }
  }
  return removedSpaces;
  }
}

vector <int> characterCounts(const string &countme){
  string string2 = removeSpaces(countme);
  vector<int> characters(26,0);
  
  for (int i = 0; i < countme.length(); ++i) {
    if (isalpha(countme[i])) {
      string2[i] = tolower(countme[i]);
      characters.at(static_cast<char> (string2[i] - 'a')) ++;
    }
  }
  return characters;
}

template<typename T>
string print(vector<T> vec);

template<typename T>
string print(T array[], int length);


int main(){
  srand(time(0));   

  cout << "find:" << endl;
  int x1[10] = {1,2,3,5,5,6,7,8,9,0};
 
  cout << "false/0 = " << find(x1, 10, 4) << endl;
  cout << "false/0 = " << find(x1, 10, 99) << endl;
  cout << "true/1 = " << find(x1, 10, 5) << endl;
  cout << "true/1 = " << find(x1, 10, 0) << endl;
  cout << "true/1 = " << find(x1, 10, 1) << endl;
  cout << "true/1 = " << find(x1, 10, 6) << endl;
  cout << endl;
  cout << endl;
  
  cout << "reverse:" << endl;
  vector <int> v1 = {1,2,3,4,5};
  reverse(v1);
  cout << "[5,4,3,2,1] = " << print(v1) << endl;
  reverse(v1);
  cout << "[1,2,3,4,5] = " << print(v1) << endl;
  vector <int> v2 = {5};
  cout << "[5] = " << print(v2) << endl;
  vector <int> v3 = {1,2,4,5};
  reverse(v3);
  cout << "[5,4,2,1] = " << print(v3) << endl;
  vector <int> v4(100);
  v4[0]  = 4;
  v4[1]  = 2;
  reverse(v4);
  cout << "0 = " << v4[0] << endl;
  cout << "2 = " << v4[98] << endl;
  cout << "4 = " << v4[99] << endl;
  
  cout << endl << "mean:" << endl;
  vector <float> f1 = {1.2, 2.4, 3.4};
  vector <float> f2 = {5.6, 5.6, 5.6, 5.6, 5.6, 5.6};
  cout << "2.33 = " << mean(f1) << endl;
  cout << "5.6 = " << mean(f2) << endl;
  
  cout << endl << "stddev:" << endl;
  cout << "0.899 = " << stddev(f1) << endl;
  cout << "0 = " << stddev(f2) << endl;
  
  cout << endl << "removedups:" << endl;
  vector<int> v5;
  v5.push_back(1);
  v5.push_back(2);
  v5.push_back(3);
  v5.push_back(3);
  v5.push_back(4);
  v5.push_back(5);
  v5.push_back(1);
  vector<int> v12 = removeDups(v5);
  cout << "[1,2,3,4,5] = " << print(v12) << endl;
  cout << "5 = " << v12.size() << endl;
  vector<int> v6;
  for(int i = 0; i < 100; i++){
    v6.push_back(i%17 + i %7);
  }
  vector<int> v22 = removeDups(v6);
  cout << "22 = " << v22.size() << endl;

  cout << "\nString Functions: " << endl;
  string upper_test = "aaABCdeFG"; 
  cout << "countUpperCase" << endl;
  cout << "5 = " << countUpperCaseChars(upper_test) << endl;
  cout << "5 = " << countUpperCaseChars("AAAAA") << endl;
  cout << "0 = " << countUpperCaseChars("aaaaa") << endl;
  string no_upper_case = "aaaa";
  cout << "0 = " << countUpperCaseChars(no_upper_case) << endl;

  cout << "RemoveSpaces:" << endl;
  string test1 = "aa AB Cd e FG"; 
  string test2 = "aaAB Cd e FG "; 
  string test3 = " rrAB Cd e FG"; 
  string test4 = " rrAB Cd e FG "; 
 
  cout << "aaABCdeFG = " << removeSpaces(test1) << endl;
  cout << "aaABCdeFG = " << removeSpaces(test2) << endl;
  cout << "rrABCdeFG = " << removeSpaces(test3) << endl;
  cout << "rrABCdeFG = " << removeSpaces(test4) << endl;

  return 0;
}

// A sneaky way to allow 1 function to print any typed array, as long as
// the passed array element can be sent to <<.
// The stringstream allows us to 'print' information to a fake output
// stream, and then get the result as a string.  It's a simple way of
// getting a non-string/character into a string.
// Contense of this function will not be tested in this course!

template<typename T>
string print(vector<T> vect) {
  stringstream out;
  out << '[';
  for(int i = 0; i < vect.size(); i++){
    out << vect[i];
    if(i != vect.size()-1)out << ',';
  }
  out << ']';
  return out.str();
}


template<typename T>
string print(T array[], int length){
  stringstream out;
  out << '[';
  for(int i = 0; i < length; i++){
    out << array[i];
    if(i != length-1)out << ',';
  }
  out << ']';
  return out.str();
}

