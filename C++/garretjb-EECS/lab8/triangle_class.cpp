
// 
// Name: Braydon Garrett
// UCID: M12349664


#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

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
    
//Triangle Class================================================================
class Triangle {
  friend class Point;
    public: 
    
    //Two Constructors----------------------------------------------------------
    Triangle() {
    }
    
    Triangle(Point p1, Point p2, Point p3) {
      P1 = p1;
      P2 = p2;
      P3 = p3;
    }
    
    //Set and Get Functions-----------------------------------------------------
    void SetPoints(Point p1, Point p2, Point p3);
    Point getPointP1() const;
    Point getPointP2() const;
    Point getPointP3() const;
    
    double length(Point temp1, Point temp2) const;
    bool triangleTest(Point P1, Point P2, Point P3) const;
    double perimeter(Point P1, Point P2, Point P3) const;
    bool equilateral(Point P1, Point P2, Point P3) const;
    double slope(Point temp1, Point temp2) const;
    bool right(Point P1, Point P2, Point P3) const;
    double area(Point P1, Point P2, Point P3) const;
    
    //Input/Output Operators----------------------------------------------------
    friend istream& operator>>(istream &input, Triangle &T ) {
      input >> T.P1 >> T.P2 >> T.P3;
    	return input;
    }

    friend ostream& operator<<(ostream &output, const Triangle &T ) {
	    output << T.P1 << T.P2 << T.P3;
	    return output;
    }
    
    private:
    Point P1;
    Point P2;
    Point P3;
};

  void Triangle::SetPoints(Point p1, Point p2, Point p3) {
      P1 = p1;
      P2 = p2;
      P3 = p3;
    }
  
    Point Triangle::getPointP1() const {
      return P1;
    }
    
    Point Triangle::getPointP2() const {
      return P2;
    }
    
    Point Triangle::getPointP3() const {
      return P3;
    }
    
  double Triangle::length(Point temp1, Point temp2) const {
    double length = sqrt(pow((temp2.getCoordX() - temp1.getCoordX()),2) + pow((temp2.getCoordY() - temp1.getCoordY()),2));
    return length;
  }
  
  bool Triangle::triangleTest(Point P1, Point P2, Point P3) const {
    double length1 = length(P1,P2);
    double length2 = length(P2,P3);
    double length3 = length(P3,P1);
    
    if (((length1 + length2) >= length3) && ((length2 + length3) >= length1) && ((length3 + length1) >= length2)) {
      return true;
    }
    else {
      return false;
    }
  }
  
  double Triangle::perimeter(Point P1, Point P2, Point P3) const {
    double perimeter;
    double length1 = length(P1,P2);
    double length2 = length(P2,P3);
    double length3 = length(P3,P1);
    
    /* Testing to make sure length values come out correctly--------------------
    cout << "Length1 = " << length1 << endl;
    cout << "Length2 = " << length2 << endl;
    cout << "Length3 = " << length3 << endl;
    */
    
    perimeter = length1 + length2 + length3;
    return perimeter;
  }
  
  double Triangle::slope(Point temp1, Point temp2) const {
      if (temp2.getCoordX() == temp1.getCoordX()) {
        return 0;
      }
      else {
      double slope = (temp2.getCoordY() - temp1.getCoordY()) / (temp2.getCoordX() - temp1.getCoordX());
      return slope;
      }
    }
  
  bool Triangle::equilateral(Point P1, Point P2, Point P3) const {
    double length1 = length(P1,P2);
    double length2 = length(P2,P3);
    double length3 = length(P3,P1);
    
    if ((length1 == length2) && (length2 == length3)) {
      return true;
    }
    else {
      return false;
    }
  }
  
  bool Triangle::right(Point P1, Point P2, Point P3) const {
    double slope1 = slope(P1,P2);
    double slope2 = slope(P2,P3);
    double slope3 = slope(P3,P1);
    
    /* Checking to make sure slopes go through correctly------------------------
    cout << "Slope1 = " << slope1 << endl;
    cout << "Slope2 = " << slope2 << endl;
    cout << "Slope3 = " << slope3 << endl;
    */
    
    if ((slope1 == 0 && slope2 == 0) || (slope2 == 0 && slope3 == 0) || (slope3 == 0 && slope1 == 0)) {
      return true;
    }
    else if ((slope1 == (-1/slope2)) || (slope2 == (-1/slope3)) || (slope3 == (-1/slope1))) {
      return true;
    }
    else {
      return false;
    }
  }
  
  double Triangle::area(Point P1, Point P2, Point P3) const {
    double area = 0;
    double S;
    double length1 = length(P1,P2);
    double length2 = length(P2,P3);
    double length3 = length(P3,P1);
    
    S = (length1 + length2 + length3)/2;
    area = sqrt((S) * (S - length1) * (S - length2) * (S - length3));
    return area;
  }
int main() {
  Point P1;
  Point P2;
  Point P3;
  Triangle T1;
  
  cout << "Enter Point 1: ";
  cin >> P1;
  cout << "Enter Point 2: ";
  cin >> P2;
  cout << "Enter Point 3: ";
  cin >> P3;
  
  cout << "P1: " << P1 << endl << "P2: " << P2 << endl << "P3: " << P3 << endl;
  cout << "P1 to P2 Length: " << T1.length(P1,P2) << endl << "P2 to P3 Length: " << T1.length(P2,P3) << endl << "P3 to P1 Length: " << T1.length(P3,P1) << endl;
  cout << "Triangle Status: " << T1.triangleTest(P1,P2,P3) << endl;
  cout << "Area: " << T1.area(P1,P2,P3) << endl;
  cout << "Perimeter: " << T1.perimeter(P1,P2,P3) << endl;
  cout << "Right Triangle Status: " << T1.right(P1,P2,P3) << endl;
  cout << "Equilateral Triangle Status: " << T1.equilateral(P1,P2,P3) << endl;
  
  return 0;
}
