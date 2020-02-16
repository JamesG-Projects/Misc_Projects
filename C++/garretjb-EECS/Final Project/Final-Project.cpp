//James Garrett
//M12349664
//Final Project 
//4/20/2018


#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <iterator>
#include <algorithm>
#include <stdio.h>
#include <string.h>

using namespace std;

const int HEIGHT = 5; 
const int WIDTH = 30;
string moves = "Empty";
enum xDirection {Right, Left};
enum yDirection {Up, Down};
int i = 0;



//==============================================================================
//Functions for use with getting/reading the chosen Maze file
string getReadFileName() {
    string fileName = "Maze";
    cout << "Select a Maze to solve" << endl;
    cout << "Options are: " << endl << "Maze (Easy)" << endl << "Maze2 (Slightly Harder)";
    cout << endl << "Maze3 (Difficult)" << endl << "Maze4 (Hard)" << endl;
    cin >> fileName;
    return fileName;
}

vector<string> mazeSelection() {
    
    //Initialize Variables------------------------------------------------------
    ifstream inFS;
    string fileName = "";
    vector <string> maze;
    string line = "";
    
    //Get fileName of the Maze--------------------------------------------------
    fileName = getReadFileName();
    
    //Open the specified file---------------------------------------------------
    inFS.open(fileName);
    
    //Check to see if the file opened properly----------------------------------
    if (!inFS.is_open()) {
      cout << "Could not open file " << fileName << endl;
      return maze;
    }
    
    //Put file string into phrase string----------------------------------------
    /*while(!inFS.eof()) {
        if(inFS.good()) {
            while (getline(inFS, line)) {
                maze += line;
                maze.push_back('\n');
            }
        }
    }*/
    copy(istream_iterator<string>(inFS),
         istream_iterator<string>(),
         back_inserter(maze));
    for (int i = 0; i <= maze.size(); i++) {
    cout << maze.at(i);
    }
    //Close the file------------------------------------------------------------
    inFS.close();
    
    return maze;
}
//==============================================================================


class MazeData {
    public:
    
    //--------------------------------------------------------------------------
    //Default Constructors
    MazeData() {
    
    }
    
    //Set Maze
    MazeData(vector<string> MAZE) {
    for (int i = 0; i <= MAZE.size(); i++) {
            Maze[i] = MAZE[i];
        }
    }
    //--------------------------------------------------------------------------
    //String list of prior moves
    //Robot should mainly stick to the 'right' walls
    vector<string> moves;
    
    //--------------------------------------------------------------------------
    //Fill the maze
    //Set and Get Functions-----------------------------------------------------
    void setMaze(vector<string> MAZE);
    vector<string> getMaze() const;
    string at(int x, int y) const;
    //--------------------------------------------------------------------------
    //Input/Output Operators
    /*
    friend istream& operator>>(istream &input, MazeData &mazeData ) {
      input >> mazeData.Maze;
    	return input;
    }

    friend ostream& operator<<(ostream &output, const MazeData &mazeData ) {
	    output << mazeData.Maze;
	    return output;
    }
    */
    
    //bool operator=(const MazeData &sstring);
    
    private:
    vector <string> Maze;
    
};

    void MazeData::setMaze(vector<string> MAZE) {
        for (int i = 0; i <= MAZE.size(); i++) {
            Maze[i] = MAZE[i];
        }
    }
    /*
    bool MazeData::operator=(const MazeData &sstring)  {
        if(sstring == ' ') {
            return true;
        }
         else {
            return false;
         }
    }*/
    
    string MazeData::at(int x, int y) const{
        int count = (y * 30) - (30 - x);
        return Maze[count];
    }
    
    vector<string> MazeData::getMaze() const{
        return Maze;
    }
    

struct Robot{
    int x = 2;
    int y = 5;
    xDirection prevDrX;
    yDirection prevDrY;
};


bool RobotMove(Robot &robot, MazeData Maze, string &moves, bool &move) {
    
    if (move) {
        //Check up/down/left/right for possible moves
        bool goUp = false;
        bool goDown = false;
        bool goRight = false;
        bool goLeft = false;
        string sstring = " ";
        
        //Check if directions are possible
        string Maze1 = Maze.at(robot.x, robot.y);
        cout << "Maze1: " << Maze1 << endl; //Check this char
        
        if (strncmp(Maze1,sstring)) { //GO RIGHT
        goRight = true;
        }
        else if (Maze.at(robot.x-1) == ' ' && Maze.at(robot.y) == ' ') { //GO LEFT
        goLeft = true;
        }
        else if (Maze.at(robot.x) == ' ' && Maze.at(robot.y+1) == ' ') { //GO DOWN (y+1 is read as down -- [NOT UP])
        goDown = true;
        }
        else if (Maze.at(robot.x && robot.y) == ' ' && Maze.at(robot.y-1) == ' ') { //GO UP
        goUp = true;
        }
        
        //Movement Logging------------------------------------------------------
        enum Moves {right, left, up, down, none};
        Moves M = none;
        
        if (moves == "Right") {
            M = right;
        }
        else if (moves == "Left") {
            M = left;
        }
        else if (moves == "Up") {
            M = up;
        }
        else if (moves == "Down") {
            M = down;
        }
        else {
            M = none;
        }
        
        
        //======================================================================
        //Check for possible movements now
        //======================================================================
        
        
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        //Was prevDrX Right?
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if (robot.prevDrX == Right && !goRight) {
            if (robot.prevDrY == Up) { //Was prevDrY Up?
                if (goUp) { //If going Up is possible, go Up
                    M = up;
                }
                else if (goDown && M != up) { //Or if going down is possible, go down
                    M = down;
                }
                else if (goLeft) { //or if going left is possible, go left
                M = left;
                }
                else { //If no other choice, dont move
                    M = none;
                }
                
            }
            else { //Was prevDrY Down?
                if (goDown) { //If going Down is possible, go Down
                    M = down;
                }
                else if (goUp && M != down) { //Or if going Up is possible, go Up
                    M = up;
                }
                else if (goLeft) { //or if going left is possible, go left
                M = left;
                }
                else { //If no other choice, dont move
                    M = none;
                }
            }
        }
        //----------------------------------------------------------------------
        //If we can move right, we always want to go right
        else if (robot.prevDrX == Right && goRight) { 
            M = right;
        }
        //----------------------------------------------------------------------
        
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        //Was prevDrX Left?
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        else if (robot.prevDrX == Left && !goLeft) {
            if (robot.prevDrY == Up) { //Was prevDrY Up?
                if (goUp) { //If going Up is possible, go Up
                    M = up;
                }
                else if (goDown && M != up) { //Or if going down is possible, go down
                    M = down;
                }
                else if (goRight) { //or if going right is possible, go right
                M = right;
                }
                else { //If no other choice, dont move
                    M = none;
                }
            }
            else { //Was prevDrY Down?
                if (goDown) { //If going Down is possible, go Down
                    M = down;
                }
                else if (goUp && M != down) { //Or if going Up is possible, go Up
                    M = up;
                }
                else if (goRight) { //or if going left is possible, go left
                M = right;
                }
                else { //If no other choice, dont move
                    M = none;
                }
            }
        }
        //----------------------------------------------------------------------
        //If we can move left (but not right), move left
        else if (robot.prevDrX == Left) {
            M = left;
        }
        //----------------------------------------------------------------------
        
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        //Was prevDrY Up?
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        else if (robot.prevDrY == Up && !goUp) {
            if (robot.prevDrX == Right) { //Was prevDrX Right?
                if (goRight) {
                    M = right;
                }
                else if (goLeft && M != right) {
                    M = left;
                }
                else if (goDown) {
                M = down;
                }
                else {
                    M = none;
                }
            }
            else { //Was prevDrX Left?
                if (goLeft) {
                    M = left;
                }
                else if (goRight && M != left) {
                    M = right;
                }
                else if (goDown) {
                M = down;
                }
                else {
                    M = none;
                }
            }
        }
        //----------------------------------------------------------------------
        //If we can move up (but not right or left), move up
        else if (robot.prevDrY == Up) {
            M = up;
        }
        //----------------------------------------------------------------------
        
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        //Was prevDrY Down?
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        else if (robot.prevDrY == Down && !goDown) {
            if (robot.prevDrX == Right) { //Was prevDrX Right?
                if (goRight) {
                    M = right;
                }
                else if (goLeft && M != right) {
                    M = left;
                }
                else if (goUp) {
                M = up;
                }
                else {
                    M = none;
                }
            }
            else { //Was prevDrX Left?
                if (goLeft) {
                    M = left;
                }
                else if (goRight && M != left) {
                    M = right;
                }
                else if (goUp) {
                M = up;
                }
                else {
                    M = none;
                }
            }
        }
        //----------------------------------------------------------------------
        //If we can move down (but not right, left or up), move down
        else if (robot.prevDrY == Down) {
            M = down;
        }
        //----------------------------------------------------------------------
        
        //======================================================================
        //Decide what to do with each movement
        //======================================================================
        
        switch(M) {
            case right:
            robot.prevDrX = Right;
            moves = "Right";
            robot.x++;
            break;
            
            case left:
            robot.prevDrX = Left;
            moves = "Left";
            robot.x--;
            break;
            
            case up:
            robot.prevDrY = Up;
            moves = "Up";
            robot.y--;
            break;
            
            case down:
            robot.prevDrY = Down;
            moves = "Down";
            robot.y++;
            break;
            
            case none:
            moves = "None";
            break;
        }
    }
    
    while (robot.x != WIDTH) {
    move = true;
    }
    cout << "Moves: " << moves << endl;
    cout << "Robot End Coords: " << "(" << robot.x << ", " << robot.y << ")" << endl;
    return move;
}

int main() {
    
    //General Initialization of Variables
    Robot robot;
    MazeData Maze;
    Maze.setMaze(mazeSelection());
    
    bool move = true;
    cout << "Robot Initial Coords: " << "(" << robot.x << ", " << robot.y << ")" << endl;
    
    //Start Simulation Call
    RobotMove(robot, Maze, moves, move);
    
    return 0;
}