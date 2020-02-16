
// 
// Name: Braydon Garrett
// UCID: M12349664


#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <string>

const double PI = 3.141592653589793238463;

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
  
//Circle Class==================================================================
class Circle {
    friend class Point;
    public:
    
    //Two Constructors----------------------------------------------------------
    Circle() {
    }
    
    Circle(Point center, Point pnt) {
      P1 = center;
      P2 = pnt;
    }
    
    //Set and Get Functions-----------------------------------------------------
    void SetPoints(Point center, Point pnt);
    Point getPointP1() const;
    Point getPointP2() const;
    
    double radius(Point P1, Point P2) const;
    double diameter(Point P1, Point P2) const;
    double area(Point P1, Point P2) const;
    double circumference(Point P1, Point P2) const;
    bool intersect(Point P1, Point P2, Point P3, Point P4) const;
    bool lieWithin(Point P1, Point P2, Point P3, Point P4) const;
    
    //Input/Output Operators----------------------------------------------------
    friend istream& operator>>(istream &input, Circle &C ) {
      input >> C.P1 >> C.P2;
    	return input;
    }

    friend ostream& operator<<(ostream &output, const Circle &C ) {
	    output << C.P1 << C.P2;
	    return output;
    }
    private:
    Point P1;
    Point P2;
    Point P3;
    Point P4;
};
    void Circle::SetPoints(Point center, Point pnt) {
      P1 = center;
      P2 = pnt;
    }
  
    Point Circle::getPointP1() const {
      return P1;
    }
    
    Point Circle::getPointP2() const {
      return P2;
    }
    
    double Circle::radius(Point P1, Point P2) const {
      double length = sqrt(pow((P2.getCoordX() - P1.getCoordX()),2) + pow((P2.getCoordY() - P1.getCoordY()),2));
      return length;
    }
    
    double Circle::diameter(Point P1, Point P2) const {
      double length = sqrt(pow((P2.getCoordX() - P1.getCoordX()),2) + pow((P2.getCoordY() - P1.getCoordY()),2));
      double diameter = 2 * length;
      return diameter;
    }
    
    double Circle::area(Point P1, Point P2) const {
      double area = PI * pow(radius(P1,P2),2);
      return area;
    }
    
    double Circle::circumference(Point P1, Point P2) const {
      double circumference = 2 * PI * radius(P1,P2);
      return circumference;
    }
    
    bool Circle::intersect(Point P1, Point P2, Point P3, Point P4) const {
      if (radius(P1,P3) <= (radius(P1,P2) + radius(P3,P4))) {
        return true;
      }
      else {
        return false;
      }
    }
    
    bool Circle::lieWithin(Point P1, Point P2, Point P3, Point P4) const {
      if (radius(P1,P3) <= radius(P1,P2)) {
      return true;
      }
      else {
        return false;
      }
    }
    
int main() {
  Circle C1;
  Point P1;
  Point P2;
  
  
  cout << "Enter Center Point: ";
  cin >> P1;
  cout << "Enter Point on Circle: ";
  cin >> P2;
  
  cout << "Center Point: " << P1 << endl << "Point on Circle: " << P2 << endl;
  cout << "Radius: " << C1.radius(P1,P2) << endl;
  cout << "Diameter: " << C1.diameter(P1,P2) << endl;
  cout << "Area: " << C1.area(P1,P2) << endl;
  cout << "Circumference: " << C1.circumference(P1,P2) << endl;
  
  Circle C2;
  Point P3;
  Point P4;
  
  cout << "Enter Center Point of Second Circle: ";
  cin >> P3;
  cout << "Enter Point on Second Circle: ";
  cin >> P4;
  
  cout << "Intersection Test: " << C2.intersect(P1, P2, P3, P4) << endl;
  cout << "Lie Within Test: " << C2.lieWithin(P1,P2,P3,P4) << endl;
  
  return 0;
}
