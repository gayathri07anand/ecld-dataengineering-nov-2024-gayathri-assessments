def perimeter_of_triangle(coordinates_given):
    x1,y1 = coordinates_given[0]
    x2,y2 = coordinates_given[1]
    x3,y3 =coordinates_given[2]
    
    import math as m
    side1= m.sqrt((x2-x1)**2 + (y2-y1)**2)
    side2 = m.sqrt((x3-x2)**2 + (y3-y2)**2)
    side3 = m.sqrt((x3-x1)**2 + (y3-y1)**2)
    perimeter = round(side1 + side2 + side3,2)
    return perimeter
print (perimeter_of_triangle([[-10, -10], [10, 10 ], [-10, 10]]))

