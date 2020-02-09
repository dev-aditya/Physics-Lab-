#!/usr/bin/env python
# coding: utf-8

# In[1]:

'''Try not to alter the code and run the program as it is.'''

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
init_printing()


def voltage(file):
    
    f = open(file,'r')
    lines = f.readlines()[18:]
    f.close()
    tval = []
    for i in lines:
        tval.append(float(i.split(',')[4]))
    return np.array(tval)

def tval(file):
    
    f = open(file,'r')
    lines = f.readlines()[18:]
    f.close()
    vol_val = []
    for i in lines:
        vol_val.append(float(i.split(',')[3]))
    return np.array(vol_val)


x = tval('freefall.csv')
y = voltage('freefall.csv')


# In[2]:


# Mean and Standard deviation from an array
def mean(x):
    return sum(x)/len(x)

def str_dev(x):
    m = mean(x)
    
    sq_sum = 0
    
    for i in x:
        sq_sum += (i-m)**2
        
    return sqrt(sq_sum/(len(x)-1))

def gauss(m):
    
    x = symbols('x')
    mu = mean(m)
    sig = str_dev(m)
    
    return (1/(sig*sqrt(2*pi)))*exp(-(x-mu)**2/(2*(sig)**2)) #gives out the gaussian distribution function
    
 '''This fucction takes the expression in a string format and then ask user for the number of variables and their symbols and respective mean
     and standard deviation and returns the error in the dependent variable'''    
def error(exp):
    
    ex = sympify(exp)
    
    var_count = int(input('No. of variables in the eq: '))
    var = []
    m= 0
    while m<var_count:
        m+=1
        a = input("variable in the expression: ")
        var.append(a)
        locals()[a]= symbols(a)  # converts the string into a variable name
    
    var = np.array(var)
    val = {}
    error_val = {}
    
    for i in var:
        m,n = float(input('Error in variable {}  '.format(i))),float(input('Mean Value of variable {}  '.format(i)))
         
        val[i]=n
        error_val[i]=m
    diff_sq = []
    
    for i in var:
        
        diff_sq.append((diff(ex,i).evalf(subs=val)*error_val[i])**2)
        
    return sqrt(sum(diff_sq))
        
        
    
 


# In[3]:


p1_n = []
p1_s = []
p2_n = []
p2_s = []
p3_n = []
p3_s = []
p4_n = []
p4_s = []
count = 0
for i in y:
    count += 1
    if (i== -0.64 or i== -0.66 or i == -0.68) and count<500:
        
        p1_n.append(count)
    elif (i== 0.68 or i== 0.70 or i == 0.72) and count<600:
        p1_s.append(count)
        
    elif (i== -1.08 or i== -1.06 or i == -1.04) and count<1000:
        
        p2_n.append(count)
    elif (i== 1.28 or i== 1.26 or i == 1.24) and count<1000:
        
        p2_s.append(count)
    elif (i==-1.24 or i== -1.22 or i == -1.20) and count<1300:
        p3_n.append(count)
        
    elif (i== 1.34 or i== 1.32 or i == 1.30) and count<1400:
        p3_s.append(count)
        
    elif i== -1.36 or i== -1.34 or i == -1.32:
        
        p4_n.append(count)
    elif i== 1.38 or i== 1.36:
        
        p4_s.append(count)

l1 = 0
l2 = 0
l3 = 0
l4 = 0
c = 0
for i in p1_n:
    l1 += x[i]/len(p1_n)
for i in p2_n:
    l2 += x[i]/len(p2_n)
for i in p3_n:
    l3 += x[i]/len(p3_n)
for i in p4_n:
    l4 += x[i]/len(p4_n)


# In[4]:


'''Position v/s time graph of a free falling magnet'''


x_t = np.array([l1,l2,l3,l4])+np.array([l1])*(-1)
y_t = np.array([0,20.3,21.2+20.3,21.2+20.3+20.1])*10**(-2)
plt.plot(x_t,y_t,'r*',label='X-axis\n1u = 0.05s\nY-axis\n1u = 0.2m ')
plt.xlabel('time')
plt.ylabel('position')
z = np.polyfit(x_t,y_t,2)
p = np.poly1d(z)
xs = np.linspace(0,0.4,50)
ys = [p ( x ) for x in xs]
plt.title('\n\nValue of "g" form the graph is {}'.format(p[2]*2),fontsize = 10)
plt.suptitle('Position v/s Time graph for free falling magnet')
plt.plot(xs, ys, ":",label='fitted curve')
plt.text(0.2,0.1,'The Eq. of fitted curve is: ',color='r')
plt.text(0.18,0.0,r'4.829*x^2 + 1.538*x + -0.000116',color= 'b')
plt.legend()
plt.grid()
plt.show()


# In[5]:


plt.plot(x,y,'m-',label='Voltage v/s Time')
plt.title('Voltage v/s time graph in free fall')
plt.xlabel('Time(in s)')
plt.ylabel('Voltage in V')
plt.legend()
plt.grid()
plt.show()


# In[6]:


'''B v/s 1/r^(3) graph'''

B = np.array([196.6,182.9,169.5,159.2,148.3,138.3,128.9,122.5,113.5,106.9,100.2,93.3,88.3,83.5,78.7,74.4,69.5])*10**(-4)
r = np.array([1/2.3,1/2.4,1/2.5,1/2.6,1/2.7,1/2.8,1/2.9,1/3.0,1/3.1,1/3.2,1/3.3,1/3.4,1/3.5,1/3.6,1/3.7,1/3.8,1/3.9])**3*10**(6)
print(len(r))
plt.plot(r,B,'r.',label='X-axis\n1u = 10000m\nY-axis\n1u = 0.002T')
z = np.polyfit(r,B,1)
p = np.poly1d(z)
xs = np.linspace(15000,80000,1000)
ys = [p ( x ) for x in xs]
plt.plot(xs, ys, label='fitted curve')
plt.suptitle('B v/s 1/r^3 graph')
plt.title('Slope of the S.L. is {}'.format(p[1]),color= 'm')
plt.xlabel('1/R^3')
plt.ylabel('B')
plt.legend()
plt.grid()
plt.show()


# In[7]:


x_p = tval('pipe.csv')
y_p = voltage('pipe.csv')
plt.plot(x_p,y_p,'g-',label='Voltage v/s time')
plt.suptitle('Voltage v/s time graph for magnet falling through a metal pipe')
plt.xlabel('time')
plt.ylabel('Voltage')
plt.grid()
plt.legend()
plt.show()


# In[8]:


p1_n = []
p1_s = []
p2_n = []
p2_s = []
p3_n = []
p3_s = []
p4_n = []
p4_s = []
count = 0
for i in y_p:
    count += 1
    if (i== -0.1 or i== -0.98 or i == -0.96) and count<500:
        
        p1_n.append(count)
    elif (i== 0.98 or i== 0.96 or i == 0.94) and count<500:
        p1_s.append(count)
        
    elif (i== -0.108 or i== -0.106 or i == -0.104) and count<1000:
        
        p2_n.append(count)
    elif (i== 0.100 or i== 0.104 or i == 0.102) and count<1000:
        
        p2_s.append(count)
    elif (i==-0.09 or i== -0.088 or i == -0.086) and (count<1500 and count>1000):
        p3_n.append(count)
        
    elif (i== 0.086 or i== 0.084 or i == 0.082) and (count<1500 and count>1000):
        p3_s.append(count)
        
    elif (i== -0.084 or i== -0.082 or i == -0.080)and count>1500:
        
        p4_n.append(count)
    elif (i== 0.082 or i== 0.080 or 0.078) and count>1500:
        
        p4_s.append(count)

l1 = 0
l2 = 0
l3 = 0
l4 = 0
c = 0
for i in p1_n:
    l1 += x_p[i]/len(p1_n)
for i in p2_n:
    l2 += x_p[i]/len(p2_n)
for i in p3_n:
    l3 += x_p[i]/len(p3_n)
for i in p4_n:
    l4 += x_p[i]/len(p4_n)


# In[9]:
'''Position v/s time graph for magnet falling through the metal pipe'''

k = np.array([0,20.3,21.2+20.3,21.2+20.3+20.1])*10**(-2)

t = np.array([l1,l2,l3,l4])+np.array([l1])*(-1)

plt.plot(t,k,'r*',label='X-axis\n1u = 0.5s\nY-axis\n1u = 0.1m ')
plt.xlabel('time')
plt.ylabel('position')
z = np.polyfit(t,k,1)
p = np.poly1d(z)
xs = np.linspace(0,3,500)
ys = [p ( x ) for x in xs]
plt.title('\n\nValue of terminal velocity form the graph is {} m/s'.format(p[1]),fontsize = 10)
plt.suptitle('Position v/s Time graph for magnet through metal pipe')
plt.plot(xs, ys, ":",label='fitted curve')
plt.text(1.7,0.05,'The Eq. of fitted curve is: ',color='r')
plt.text(1.8,0.0,r'0.2364 x + 0.0006073',color= 'b')
plt.legend()
plt.grid()
plt.show()


# In[3]:


error('(65*m*g*a**4)/(45*(pi**2)*tau*v*(3.936*10**(-7))**2)')   #the expression for conductivity


# In[ ]:




