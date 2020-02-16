/*
    James Garrett
    M12349664
    Lab09
*/

#include <iostream>
#include <vector>

#include "LList.h"

using namespace std;

int main(){
    LList a;
    
    /*
    for(int i = 0; i < 5; i++){
        a.push_front(45);
    }
    */
    
    //Check if list is empty or not
    if (a.empty() == 1) {
    cout << "Empty Status: Empty" << endl;
    }
    else {
        cout << "Empty Status: Not Empty" << endl;
    }
    
    //Display size of the list
    cout << "Size of list: " << a.size() << endl;
    
    //Get a number to push back
    /*
    int val;
    cout << "Enter a value to push back: " << endl;
    cin >> val;
    */
    for (int i = 1; i <= 3; i++) {
    a.push_back(i);
    }
    cout << a << endl;
    
    //Reverse the list
    cout << "Reversed List: " << endl;
    a = a.reverse();
    cout << a << endl;
    
    //Pop Back the last value
    a.pop_back();
    cout << "New size of list: " << a.size() << endl;
    cout << a << endl;
    
    
    
    return 0;
}

