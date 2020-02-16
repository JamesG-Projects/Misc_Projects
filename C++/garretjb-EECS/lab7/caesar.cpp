//James Garrett
//LAB07 3/22/2018

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

string encrypt(string phrase, string key) {
    
    int count = 0;
    int ASCII_SUM = 0;
    for (int i = 0; i < key.length(); i++) {
        ASCII_SUM += key.at(i);
    }
    count = (ASCII_SUM % 23) + 3;
    
    //cout << "ASCII_SUM Value: " << ASCII_SUM << endl << "Count Value: " << count << endl;
    
    for (int i = 0; i < phrase.length(); i++) {
        if (isupper(phrase[i])) {
            phrase[i] = tolower(phrase[i]);
        }
    }
    
    int temp1 = 0;
    for (int i = 0; i < phrase.length(); i++) {
        if (phrase[i] >= 'a' && (phrase[i] + count) > 'z') {
            temp1 = 24 - count;
            phrase[i] = phrase[i] - temp1;
        }
        else if (phrase[i] >= 'a' && (phrase[i] + count) <= 'z') {
            phrase[i] = phrase[i] + count;
        }
        else {
            phrase[i] = phrase[i];
        }
    }
    
    return phrase;
}

string decrypt(string phrase, string key) {
    
    int count = 0;
    int ASCII_SUM = 0;
    for (int i = 0; i < key.length(); i++) {
        ASCII_SUM += key.at(i);
    }
    count = (ASCII_SUM % 23) + 3;
    
    //cout << "ASCII_SUM Value: " << ASCII_SUM << endl << "Count Value: " << count << endl;
    
    for (int i = 0; i < phrase.length(); i++) {
        if (isupper(phrase[i])) {
            phrase[i] = tolower(phrase[i]);
        }
    }
    
    int temp1 = 0;
    for (int i = 0; i < phrase.length(); i++) {
        if (phrase[i] <= 'z' && (phrase[i] - count) >= 'a') {
            phrase[i] = phrase[i] - count;
        }
        else if (phrase[i] <= 'z' && (phrase[i] + count) >= 'a') {
            temp1 = 24 - count;
            phrase[i] = phrase[i] + temp1;
        }
        
        else {
            phrase[i] = phrase[i];
        }
    }
    
    return phrase;
}

string getReadFileName() {
    string fileName = "";
    cout << "Enter a file to read: " << endl;
    cin >> fileName;
    return fileName;
}

string getWriteFileName() {
    string fileName = "";
    cout << "Enter a file to write to: " << endl;
    cin >> fileName;
    return fileName;
}
int main() {
    
    //Initialize Variables------------------------------------------------------
    ifstream inFS;
    string fileName = "";
    string phrase = "";
    string key = "";

    //Get Key String------------------------------------------------------------
    cout << "Enter the Key for Encryption and Decryption: " << endl;
    cin >> key;
    
    //Get fileName--------------------------------------------------------------
    fileName = getReadFileName();
    
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
    cout << "Original Phrase: " << phrase << endl;
    
    phrase = encrypt(phrase, key);
    cout << "Encrypted Phrase: " << phrase << endl;
    
    phrase = decrypt(phrase, key);
    cout << "Decrypted Phrase: " << phrase << endl;
    
    //Write to another file-----------------------------------------------------
    ofstream outFS;

    //Get second fileName-------------------------------------------------------
    fileName = getWriteFileName();
    
    //Open the specified file---------------------------------------------------
    outFS.open(fileName);
    
    //Check to see if the file opened properly----------------------------------
    if (!outFS.is_open()) {
      cout << "Could not open file " << fileName << endl;
      return 1;
    }
    
    //Actually write to it------------------------------------------------------
    outFS << encrypt(phrase, key);
    
    //Close the File------------------------------------------------------------
    outFS.close();
    
  return 0;
}

