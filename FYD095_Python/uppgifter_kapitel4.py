#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 10:47:21 2021

@author: calvinsmith
"""

#%% Uppgift 4.1.2 (REDOVISAD)

class Matris:
    
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.list = [[0]*columns for i in range(rows)]
        for i in range(0,rows):
            for j in range(0,columns):
                self.list[i][j] = int(input("ange element:"))
                
    def minimum(self):
         import numpy as np  
         self.min = np.min(self.list)
         print(self.min)
         
    def maximum(self):
        import numpy as np
        self.max = np.max(self.list)
        print(self.max)
        
    def mean(self):
        import numpy as np
        mat = np.array(self.list)
        rows = mat.shape[0]
        columns = mat.shape[1]
        elements = rows*columns
        self.mean = np.sum(mat.reshape(elements,1))/elements
        print(self.mean) 
         
    def std(self):
        import numpy as np
        mat = np.array(self.list)
        rows = mat.shape[0]
        columns = mat.shape[1]
        elements = rows*columns
        self.std = np.std(mat.reshape(elements,1))
        print(self.std) 
    
    
#%% 4.2,1 (REDOVISAD)

class Student:
     
    def __init__(self):
        self._name = input("Name:")
        self._lastname = input("Last name:")
        self._age = input("Age:")
      
#%%

L = [Student()]

#%%
#### MENY
choice = int(input("What do you want to do?\n1=Add Student\n2=Remove Student\n3=Sort\n4=Print "))

if choice == 1:
    L.append(Student())
elif choice == 2:
    remove = input("Who do you want to remove?")
    for i in L:
        if i._name == remove:
            L.remove(i)
elif choice == 3 :
    sort = input("sort by name,last name or age?")
    if sort == "name":
        L.sort(key = lambda x: x._name)
    if sort == "lastname":
        L.sort(key = lambda x: x._lastname)
    if sort == "age":
        L.sort(key = lambda x: x._age)
elif choice == 4:
    print('Name\t\tLast Name\t\tAge')
    print("-----------------------------")
    for i in range(0,len(L)):
        print(f'{L[i]._name}\t{L[i]._lastname}\t\t{L[i]._age}')
        
#%% Uppgift 4..3.1 (REDOVISAD)

class Vektor:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def R(self):
        import numpy as np
        self.R = np.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)
        print(self.R)
     
        
    def __str__(self):
        return f'The vector coordinates are [{self.x},{self.y},{self.z}]\nThe length of the vector is {self.R}'
        
    @classmethod
    def new(cls,x,y,z):
        p = cls(x,y,z)
        a = int(input("scalar:"))
        b = int(input("scalar:"))
        c = int(input("scalar:"))
        p.x = x*a
        p.y = y*b
        p.z = z*c
        return p
    
#%% 4.4.1 (REDOIVSAD)
class Person:
    
    def __init__(self,namn,personnummer):
        self.namn = namn
        self.pn = personnummer
        
    def __str__(self):
        return f'Namn:{self.namn}\nPersonnummer:{self.pn}'
    
    def ID(self):
        print("Objekt: Person")
       

class Bilist(Person):
    
    def __init__(self,namn,personnummer,körkort):
        
        super().__init__(namn,personnummer)
        self.korkort = körkort
        
    def __str__(self):
        return f'Namn:{self.namn}\nPersonnummer:{self.pn}\nKörkort:{self.korkort}' 
    
    def ID(self):
        print("Objekt: Bilist")
        

#Function  to identify which class object belongs to
def harKorkort(obj):
    
    return obj.ID()
    
#%% 4.5.1 (REDOVISAD)
class Bråk:
    
    def __init__(self,nämnare,täljare):
    
        
        def Förkorta(self,nämnare,täljare):
            from  fractions import Fraction
            
            self.n = Fraction(täljare,nämnare).denominator
            self.t = Fraction(täljare,nämnare).numerator
            self.d = self.t/self.n
        Förkorta(self,nämnare,täljare)
        
    def __add__(self,obj):
        return self.d + obj.d 
    
    def __sub__(self,obj):
        return self.d - obj.d
    
    def __mul__(self,obj):
        return self.d*obj.d
    
    def __truediv__(self,obj):
        return self.d/obj.d
    
    def __str__(self):
        return f'The fraction is {self.t}/{self.n}'
        
        
            
        

