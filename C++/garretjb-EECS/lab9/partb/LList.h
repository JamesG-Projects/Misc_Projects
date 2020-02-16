#ifndef LLIST_H
#define LLIST_H

/*
    Linked List class that store integers, with [] operator.
    Uses head pointer.
    Paul Talaga
    September 2015
*/
#include <ostream>
#include <stdexcept>

#define int int

using namespace std;

struct node_t {
    int data;
    node_t* next;
};

// This implementation will use a head pointer,
// allowing O(1) insertion on the front,
// and O(n) on the end.
class LList {

public:
    LList(){
        head = NULL;
    }

    ~LList(){
        clear();
    }

    LList(const LList& other){
        // Do the same as the default constructor
        head = NULL;
        // Check if the other LList is empty
        if(other.head == NULL){
            return;
        }
        // Not empty?  Iterate through the other list
        // and push_back on myself.
        node_t* temp = other.head;
        while(temp){
            push_back(temp->data);
            temp = temp->next;
        }
    }

    // Similar to copy constructor, but check for self
    // assignment, if not, clear and copy all data.
    LList& operator= (const LList& other){
        if(this == &other){
            return *this;
        }
        clear();
        if(other.head == NULL){
            return *this;
        }
        node_t* temp = other.head;
        while(temp){
            push_back(temp->data);
            temp = temp->next;
        }
        return *this;
    }

    //Functions start here======================================================
    
    //Empty Check--------------------------------------------------------------+
   bool empty() const {
       return (head == NULL);
    }
    
    //List Size----------------------------------------------------------------+
    unsigned int size() const {
        
        if (empty()) {
           return 0; 
        }
        
        int sizeCount = 0;
        node_t* curNode = head;
        while (curNode != NULL) {
            ++sizeCount;
            curNode = curNode->next;
        }
        return sizeCount;
    }

    //Push Back a value--------------------------------------------------------+
    void push_back(int value){ 
        
        //Create temporary nodes
        if (head == NULL) {
            head = new node_t;
            head->data = value;
            head->next = NULL;
            
        }
        else {
            node_t* curNode = head;
            node_t* last = new node_t;
            last->data = value;
            last->next = NULL;
            
            while (curNode->next != NULL) {
                curNode = curNode->next;
            }
            curNode->next = last;
        }
    }

    //Push Front a value-------------------------------------------------------+
    void push_front(int value){
        // Empty list?
        if(head == NULL){
            head = new node_t;
            head->data = value;
            head->next = NULL;
        }else{ // Not empty
            node_t* temp = new node_t;
            temp->data = value;
            temp->next = head;
            head = temp;
        }
    }

    //Pop Front a value--------------------------------------------------------+
    void pop_front(){
        if(head == NULL) return;
        node_t* temp = head;
        head = head->next;
        delete temp;
    }

    //Pop Back a value---------------------------------------------------------+
    void pop_back(){
        
        node_t* curNode = head;
        for (int i = 0; i < size()-2; i++) {
            curNode = curNode->next;
        }
        curNode->next = NULL;
        cout << "Last value of list has been removed." << endl;
    }
    

    // Overload [] operator
    // Return logic error if index out of bounds
    int& operator[](unsigned pos) const {
        node_t* temp = head;
        while(temp != NULL && pos > 0){
            temp = temp->next;
            pos--;
        }
        // As long as I don't have a null pointer, assign.
        if(pos == 0 && temp != NULL){
            return temp->data;
        }
        throw logic_error("Index invalid");
    }

    //Reverse List-------------------------------------------------------------+
    LList reverse() const {
        
        LList reverse;
        node_t* temp = this->head;
        
        for (int i = 0; i < size(); i++) {
            reverse.push_front(temp->data);
            temp = temp->next;
        }
        return reverse;
    }

    bool operator==(const LList& other) const {
        node_t* temp = this->head;
        for (int i = 0; i < size(); i++) {
            if (other[i] != temp->data) {
                return false;
            }
            temp = temp->next;
        }
        return true;
    }

    bool operator!=(const LList& other) const {
        return !operator==(other);
    }
    
    LList operator+ (const LList& listComp) const {
        LList temp;
        temp = *this;
        for(int i = 0; i < listComp.size(); i++) {
            temp.push_back(listComp[i]);
        }
        return temp;
    }
    void clear(){
        node_t* last = head;
        while(head){
            head = head->next;
            delete last;
            last = head;
        }
        // Normally you never want to change head or you'll orphan part
        // of the list, but in this case we are wiping the list,
        // so it is ok to so and saves us a variable.
        head = NULL;
    }

private:
    node_t* head;

};

// Note this function is O(n^2) because getAt is O(n) and we are
// doing it n times.

ostream& operator<<(ostream& out, const LList &other) {     
    out << "[";     
    for(unsigned int i = 0; i < other.size(); i++) {         
        out << other[i] << ", ";     
    }      
    out << "]";     
    return out; 
    
}

#endif
