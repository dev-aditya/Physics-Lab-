


from sympy import *

import numpy as np
x = symbols('x')

"""Root approximation using Newton-Raphson Method"""

def newton(function,initial_guess,max_iter):
    
    xn = initial_guess
    
    for n in range(0,max_iter):
        
        fxn = function.subs(x,xn)
        
        if abs(fxn) < 10**-4:  #find the |f(x)| upto appropriate decimal digits
            
            print('Found solution after',n,'iterations.')
            try:
                return xn.evalf(4)
            except AttributeError:
                return xn
        
        Dfxn = diff(function,x).subs(x,xn)
        
        if Dfxn == 0:
            
            print('Zero derivative. No solution found.')
            
            return None
        
        xn = xn - fxn/Dfxn
        
    print('Exceeded maximum iterations. No solution found.')
    
    return None


"""Root approximation using bisection methoud"""


def bisection(f,a,b,max_iter):
    
    if f.subs(x,a)*f.subs(x,b) >= 0:
        print("Bisection method fails.")
        return None
    
    a_n = a
    b_n = b
    
    for n in range(1,max_iter+1):
        m_n = (a_n + b_n)/2
        f_m_n = f.subs(x,m_n)
        
        if f.subs(x,a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
            
        elif f.subs(x,b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
            
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        
        else:
            print("Bisection method fails.")
            
            return None
    print("Found approximate solution after",max_iter,"iteration")
    return ((a_n + b_n)/2)




"""Rienmann Sum"""
def lowersum(f,a,b,n):
    x = symbols('x')
    area = 0
    h = (b-a)/n
    t = a
    for i in range(n):
        l = min(f.subs(x,t),f.subs(x,t+h))
        area += l*h
        t = t+h
    return area

            

def uppersum(f,a,b,n):
    x = symbols('x')
    area = 0
    h = (b-a)/n
    t = a
    for i in range(n):
        l = max(f.subs(x,t),f.subs(x,t+h))
        area += l*h
        t = t+h
    return area

            
def Rienmannsum(f,a,b):
    e = 1
    n = int(input("Initial number of divisions you want: "))
    while e>10**-4:
        L = lowersum(f,a,b,n)
        U = uppersum(f,a,b,n)
        e = U-L
        n *= 10
    return (U+L)/2



"""N X N Matrix equation solving"""

import numpy as N
import numpy.linalg as la

var_count = int(input("No. of variables you want to solve for: "))

coef = N.zeros((var_count,var_count))

R_val = N.zeros(var_count)

for row in range(1,var_count+1):
    for col in range(1,var_count+1):
        coef[row-1,col-1] = float(input("Coefficient ofx{}: ".format(col)))
        print(coef)
        
    R_val[row-1]=float(input("Value on the RHS of the equation: "))
    print(R_val)

var_mat = coef.copy()
var_mat = N.transpose(var_mat)

det = []

for row in range(var_count):
    for col in range(var_count):
        var_mat[row,col]= R_val[col]
    det.append(la.det(var_mat))
    var_mat = coef.copy()
    var_mat = N.transpose(var_mat)
det_array = N.array(det)
if la.det(coef)==0:
    if len(set(det))==1 and list(set(det))[0]==0:
        print("Infinite solutions exist!")
    elif len(set(det)) != 0:
        print("No Solution Exist!")
else:
    for i in range(var_count):
        print("Value of  x{} is {}".format(i+1,det_array[i]/la.det(coef)))




