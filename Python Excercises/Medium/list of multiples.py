"""def quadratic_equation(a,b,c):
     import math as m
     """

"""import math as m
print(m.sqrt(9))"""

"""Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c."""

def quadratic_solution(a,b,c):
    import cmath as m
    squareroot = m.sqrt((b**2)-(4*a*c))
    solution1 = (-b + squareroot)/(2*a)
    solution2 = (-b- squareroot)/(2*a)
    if solution1.imag ==0:
        solution1 = int(solution1.real)
    if solution2.imag ==0:
        solution2 = int(solution2.real)   


    return solution1 , solution2
print (quadratic_solution(1,2,3))
print (quadratic_solution(1,2,1))

