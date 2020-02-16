
// 
// Name:
// UCID: M12349664


#include <iostream>

using namespace std;

// We have setup class framework for you.
// Please add cin/cout overload first and at the same time add the coordinates
//
// See github example as specified in the assignment handout for exaamples
//

class Point {
    public:
    
    //Two Constructors----------------------------------------------------------
    Point() {
      x = 0;
      y = 0;
    }
    Point(int x1, int y1) {
      x = x1;
      y = y1;
    }
    
    //Set and Get Functions-----------------------------------------------------
    void SetCoords(int x_coord, int y_coord);
    int getCoordX() const;
    int getCoordY() const;
    
    //Input/Output Operators----------------------------------------------------
    friend istream& operator>>(istream &input, Point &p ) {
      input >> p.x >> p.y;
    	return input;
    }

    friend ostream& operator<<(ostream &output, const Point &p ) {
	    output << "(" << p.x << "," << p.y << ")";
	    return output;
    }
    
    private:
    int x;
    int y;

  };

    void Point::SetCoords(int x_coord, int y_coord) {
    x = x_coord;
    y = y_coord;
    return;
    }
  
    int Point::getCoordX() const {
      return x;
    }
    
    int Point::getCoordY() const {
      return y;
    }
    
int main() {
  Point P1;
  
  cout << "Enter P1: ";
  cin >> P1;

  cout << "P1: " << P1 << endl;
  
  Point P2;
  P2.SetCoords();
  cout << P2;
  return 0;
}
