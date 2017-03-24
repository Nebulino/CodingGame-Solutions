'''
Your program must find the point that is exactly between two other points.
You are given the coordinates (x, y) of two points which bind a line segment.
The midpoint of this line segment is the target point. 
Be careful with float numbers and use . as a decimal mark.
INPUT:
Line 1: Two integers separated by whitespace x1 and y1, the coordinates of the first point.
Line 2: Two integers separated by whitespace x2 and y2, the coordinates of the second point.
OUTPUT:
Two integers separated by whitespace, the coordinates of the midpoint.
CONSTRAINTS:
-100 < x,y < 100
EXAMPLE:
Input
1 2
3 5
Output
2 3.5
'''
import sys
import math


x_1, y_1 = [int(i) for i in input().split()]
x_2, y_2 = [int(i) for i in input().split()]

xmedia = float((x_1+x_2)/2)
ymedia = float((y_1+y_2)/2)

print('%g'%(xmedia), '%g'%(ymedia))
