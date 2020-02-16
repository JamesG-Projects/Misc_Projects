
// 
// Name: Braydon Garrett
// UCID: M12349664


#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

// We have setup class framework for you. Please copy the point 
// class you created to this file.

//Point Class===================================================================
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
    
//Line Class====================================================================
class Line {
    friend class Point;
    public:
    
    //Two Constructors----------------------------------------------------------
    Line() {
    }
    
    Line(Point p1, Point p2) {
      P1 = p1;
      P2 = p2;
    }
    
    //Set and Get Functions-----------------------------------------------------
    void SetLines(Point p1, Point p2);
    Point getPointP1() const;
    Point getPointP2() const;
    
    double slope() const;
    double length() const;
    double y_int() const;
    bool horizontal() const;
    bool vertical() const;
    bool parallel(double slope1, double slope2) const;
    bool intersects(double slope1, double slope2) const;
    
    //Input/Output Operators----------------------------------------------------
    friend istream& operator>>(istream &input, Line &L ) {
      input >> L.P1 >> L.P2;
    	return input;
    }

    friend ostream& operator<<(ostream &output, const Line &L ) {
	    output << L.P1 << L.P2;
	    return output;
    }
    
    private:
    Point P1;
    Point P2;
};
    
    void Line::SetLines(Point p1, Point p2) {
      P1 = p1;
      P2 = p2;
    }
  
    Point Line::getPointP1() const {
      return P1;
    }
    
    Point Line::getPointP2() const {
      return P2;
    }
    
    double Line::slope() const {
      if (P2.getCoordX() == P1.getCoordX()) {
        return 0;
      }
      else {
      double slope = (P2.getCoordY() - P1.getCoordY()) / (P2.getCoordX() - P1.getCoordX());
      return slope;
      }
    }
    
    double Line::length() const {
      double length = sqrt(pow((P2.getCoordX() - P1.getCoordX()),2) + pow((P2.getCoordY() - P1.getCoordY()),2));
      return length;
    }
    
    double Line::y_int() const {
      double y_int = P1.getCoordY() - (P1.getCoordX() * slope());
      return y_int;
    }
    
    bool Line::horizontal() const {
      if (P2.getCoordY() == P1.getCoordY()) {
        return true;
      }
      else {
        return false;
      }
    }
    
    bool Line::vertical() const {
      if (P2.getCoordX() == P1.getCoordX()) {
        return true;
      }
      else {
        return false;
      }
    }
    
    bool Line::parallel(double slope1, double slope2) const {
      if (slope1 == slope2) {
        return true;
      }
      else {
        return false;
      }
    }
    
    bool Line::intersects(double slope1, double slope2) const {
      if (slope1 != slope2) {
      return true;
      }
      else {
      return false;
      }
    }
    
int main() {
  Line L1;
  Line L2;
  
  cout << "Enter L1: ";
  cin >> L1;
  cout << "Enter L2: ";
  cin >> L2;
  
  cout << "L1: " << L1 << endl << "L2: " << L2 << endl;
  cout << "L1 Slope: " << L1.slope() << endl << "L2 Slope: " << L2.slope() << endl;
  cout << "L1 Length: " << L1.length() << endl << "L2 Length: " << L2.length() << endl;
  cout << "L1 Y-Int: " << L1.y_int() << endl << "L2 Y-Int: " << L2.y_int() << endl;
  cout << "L1 Horizontal?: " << L1.horizontal() << endl << "L2 Horizontal?: " << L2.horizontal() << endl;
  cout << "L1 Vertical?: " << L1.vertical() << endl << "L2 Vertical?: " << L2.vertical() << endl;
  cout << "Lines Parallel?: " << L1.parallel(L1.slope(), L2.slope()) << endl;
  cout << "Lines Intersect?: " << L1.intersects(L1.slope(), L2.slope()) << endl;

  return 0;
}
