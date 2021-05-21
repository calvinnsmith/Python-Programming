#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:59:36 2021

@author: calvinsmith
"""
import matplotlib.pyplot as plt
import numpy as np
import math
#%% Uppgift 3.1.1 (REDOVISAD)

# 200 equally spaced points between 12 and 18
vec = np.linspace(12,18,200)

# 1) even sum
# from 0 through the whole vector with steplength 2
even_sum = sum(vec[0::2])
print(even_sum)
# 2) odd sum
# from 1 through the whole vector with steplength 2
odd_sum = sum(vec[1::2])
print(odd_sum)
# 3)
# from 10 through the whole vector with steplength 10
ten_sum = sum(vec[10::10])
print(ten_sum)
# 4)
index_sum = sum(vec[[2,5,19,92]])
print(index_sum)
#%% Uppgift 3.1.3 (REDOVISAD)

# 4 x 5 matris med slumpmässiga heltal mellan 0 och 11

mat = np.random.randint(12,size =(4,5))

# 1) row sum

row_sum = np.sum(mat, axis = 1)

# 2) col sum

col_sum = np.sum(mat,axis = 0)

# 3) col with even index

even_col_sum = np.sum(mat[:,[0,2,4]],axis = 0)

# 4) column mean

col_mean = np.mean(mat,axis = 0)

# 5)

mat_mean = sum(mat.reshape(20,1))/20


# 6)

mat_std = np.std(mat.reshape(20,1))

#%% 3.2.1 (REDOVISAD)

#
A = np.random.randint(1,100,size = (4,4))
B = np.random.randint(1,100,size = (4,4))


C = np.hstack((np.vstack((A,B)),np.vstack((B,A))))


D = np.diag(C).reshape((4,2))

#%% Uppgift 3.3.2 (REDOVISAD)


x = np.linspace(-6*math.pi,6*math.pi,100)

type = input("Choose plot type (same,separate or sub):")


if type == "same":

    plt.plot(x,np.sin(x),'r',label = 'sin(x)')
    plt.plot(x,np.cos(x),'b',label = 'cos(x)')
    plt.plot(x,np.sin(x)/x,'g',label = 'sin(x)/x')
    plt.legend()
    plt.show()

elif type == "separate":
    
    plt.plot(x,np.sin(x),'r')
    plt.title('sin(x)')
    
    plt.figure()
    
    plt.plot(x,np.cos(x),'b')
    plt.title('cos(x)')
    
    plt.figure()
    
    plt.plot(x,np.sin(x)/x,'g')
    plt.title('sin(x)/x')
    
    plt.show()

elif type == "sub":
    
    plt.subplot(3,1,1)
    plt.plot(x,np.sin(x),'r', label = 'sin(x)')
    plt.legend()
    
    plt.subplot(3,1,2)
    plt.plot(x,np.cos(x),'b', label = 'cos(x)')
    plt.legend()
    
    
    plt.subplot(3,1,3)
    plt.plot(x,np.sin(x)/x,'g',label = 'sin(x)/x')
    plt.legend()
    
    plt.tight_layout()
    
    plt.show()
    
#%% Uppgift 3.4.2 (REDOVISAD)

def integ_trap(function,limits,step):
    
    a = limits[0]
    b = limits[1]
    
    N = round((b-a)/step)
    
    x = np.linspace(a,b,N)
    
    
    
    approx = step*(np.sum(eval(function,{'x': x[0:N-1], 'np': np})) + 
                   (eval(function,{'x':x[N-1],'np': np}) + 
                    eval(function,{'x':x[0],'np': np}))/2)
    
    
    
    return approx
    

from scipy import integrate


func = lambda x: np.sin(x)


actual = integrate.quad(func,-3,3)
print(actual[0])               



