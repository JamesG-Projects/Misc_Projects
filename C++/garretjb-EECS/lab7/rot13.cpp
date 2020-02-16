//James Garrett
//LAB07 3/22/2018

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

string encrypt(string phrase) {
    
    for (int i = 0; i < phrase.length(); i++) {
        if (isupper(phrase[i])) {
            phrase[i] = tolower(phrase[i]);
        }
    }
    int temp;
    for (int i = 0; i < phrase.length(); i++) {
        if (phrase[i] >= 'a' && phrase[i] <= 'm') {
            phrase[i] = phrase[i] + 13;
        }
        else if (phrase[i] >= 'n' && phrase[i] <= 'z') {
            phrase[i] = phrase[i] - 13;
        }
        else {
            phrase[i] = phrase[i];
        }
    }
    return phrase;
}
string decrypt(string phrase) {
    
    for (int i = 0; i < phrase.length(); i++) {
        if (isupper(phrase[i])) {
            phrase[i] = tolower(phrase[i]);
        }
    }
    int temp;
    for (int i = 0; i < phrase.length(); i++) {
        if (phrase[i] >= 'a' && phrase[i] <= 'm') {
            phrase[i] = phrase[i] + 13;
        }
        else if (phrase[i] >= 'n' && phrase[i] <= 'z') {
            phrase[i] = phrase[i] - 13;
        }
        else {
            phrase[i] = phrase[i];
        }
    }
    return phrase;
}

int main() {
    
    //Initialize Variables------------------------------------------------------
    ifstream inFS;
    string fileName = "";
    string phrase = "";
    
    //Get fileName--------------------------------------------------------------
    cout << "Enter a file name: " << endl;
    cin >> fileName;
    
    //Open the specified file---------------------------------------------------
    inFS.open(fileName);
    
    //Check to see if the file opened properly----------------------------------
    if (!inFS.is_open()) {
      cout << "Could not open file " << fileName << endl;
      return 1;
    }
    
    //Put file string into phrase string----------------------------------------
    while(!inFS.eof()) {
        if(inFS.good()) {
            getline(inFS, phrase);
        }
    }
    
    //Close the file------------------------------------------------------------
    inFS.close();
    
    //Test to make sure it worked properly--------------------------------------
    cout << phrase << endl;
    
    phrase = encrypt(phrase);
    cout << "Encrypted Phrase: " << phrase << endl;
    
    phrase = decrypt(phrase);
    cout << "Decrypted Phrase: " << phrase << endl;
    
    
    //Write to another file-----------------------------------------------------
    ofstream outFS;
    fileName = "";
    
    //Get second fileName-------------------------------------------------------
    cout << "Enter a file name: " << endl;
    cin >> fileName;
    
    //Open the specified file---------------------------------------------------
    outFS.open(fileName);
    
    //Check to see if the file opened properly----------------------------------
    if (!outFS.is_open()) {
      cout << "Could not open file " << fileName << endl;
      return 1;
    }
    
    //Actually write to it------------------------------------------------------
    outFS << encrypt(phrase);
    
    //Close the File------------------------------------------------------------
    outFS.close();
  return 0;
}

