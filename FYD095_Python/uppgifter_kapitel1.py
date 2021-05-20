#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:41:17 2021

@author: calvinsmith


"""
import numpy as np
import cmath 
import math
# Delkapitel 1.1


#%% Uppgift 1.1.1 
## Programmet hittar och skrivet ut lösningen till en andragradsekvation.


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))


coeff = [a,b,c] 

print(f'Lösningen är {np.roots(coeff)}')


#%% Uppgift 1.1.2
## Ange två tal av typen int

## a) Hexadecimal
tal_1 = int(input("välj första talet:"))
print(f' {tal_1} i hexadecimal form är {hex(tal_1)}')

tal_2 = int(input("välj andra talet:"))
print(f'{tal_2} i hexadecimal form är {hex(tal_2)}')


## b) Kvoten av talen, float med 3 siffror efter decimalpunkten

kvot = tal_1/tal_2
print(f'kvoten av {tal_1} och {tal_2} är {kvot:5.3f}')

## c) Resten av divisionen
print(f'resten av divisionen är {tal_1 % tal_2}') 

#%% Uppgift 1.1.3 
## Programmet skriver ut en formatterad tabell 

first_name = input("Förnamn:")
last_name = input("Efternamn:")
year = input("Födelseår:")
gender = input("Kön:")


print(f'Förnamn\t\tEfternamn\tÅr\t\tKön')
print('----------------------------------------------------')
print(f'{first_name}\t\t{last_name}\t\t{year}\t\t{gender}')







# Delkapitel 1.2

#%% Uppgift 1.2.1

# create a str object with spaces in between each number
s = "5" + " " + "3" + " " + "10" + " " + "2" + " " + "32" + " " + "8"

# convert it to a list of char
s_new = s.split(sep = None,maxsplit = -1)

# convert to list of integers
s_int = [int(i) for i in s_new]

#result
print(f'The mean is {np.mean(s_int)}')
print(f'The maximum value is {max(s_int)}')
print(f'The minimum value is {min(s_int)}')

#%% Uppgift 1.2.2

string = "544 cat in 3 2 6 dog "
count_nr = 0
count_letters = 0
for i in string:
    if i.isdigit() == True:
        count_nr = count_nr + 1
    elif i.isalpha() == True:
        count_letters = count_letters + 1 
        
        
#%% Uppgift 1.2.3 Hitta mönster i en sträng


#%% Uppgift 1.3.1
## Avgör om ett tal är komplext eller reellt, om reellt avgör det 
## om talet är ett heltal

tal = 5 + 5j

if isinstance(tal,complex) == True:
    print("Talet är komplext")
elif isinstance(tal,int) == True:
    print("Talet är ett reellt heltal" )

else:
    print("Talet är reellt")



#%% Uppgift 1.3.2
## Programmet avgör om två referenser pekar på samma objekt
ref_1 = "123+"
ref_2 = "123+"
    
    
if id(ref_1) == id(ref_2):
    print("referenserna pekar på samma objekt")
elif ref_1 == ref_2:
    print("Objekten har samma värde men pekar på olika objekt")
else:
    print("Objekten är olika")
    
   
#%% Uppgift 1.3.3
## avgör huruvida en sträng är ett palindrom

#original string
string = "bara gin ni får ge till amal lite grå finnig arab"

#lower case
string = string.lower()

#removing non characters
for i in string:
    if i.isalpha() == False:
        string = string.replace(i,'')

# checking if string is a palindrom         
if string == string[::-1]:
   print(f'{string} är ett palindrom')
else:
   print(f'{string} är inte ett palindrom')            
        
        
#%% Uppgift 1.4.1 

# how many people should we input
people = 4



#first persons name and age
first_age = int(input("age:"))
first_name = input("name:")

print(f'The average age is {first_age}')
print(f'The oldest person is {first_age}')
print(f'The oldest persons name is {first_name}')


#counter variable 
nr = 1

#initial total age
tot_age = first_age

#initial oldest person and his/her name
oldest = first_age
oldest_name = first_name

while nr < people:
    age = int(input("age:"))
    name = input("name:")
    
    nr = nr + 1
    
    tot_age += age
    
    print(f'The average age is {tot_age/nr}')
    
    if age > oldest:
        
        oldest = age
        oldest_name = name
        print(f'The oldest person is {oldest}')
        print(f'The oldest persons name is {oldest_name}')
    else:
        print(f'The oldest person is {oldest}')
        print(f'The oldest persons name is {oldest_name}')
        
#%% Uppgift 1.4.2

 
#%% Uppgift 1.4.3

## multiplying i and j, printing as formatted table :5 = 5 spaces inbetween 
## and end = '' means print on same row
## print() for each column

for i in range(1,10):
    for j in range(1,10):
        print(f'{(i*j):5}', end = '')
    print()
    
#%%  1.5.1 
## Funktion som givet ett heltal skriver ut alla talets delare

tal = int(input("Skriv ett heltal:"))

for i in range(1,tal+1):
    ## om resten vid division = 0 , så är tal delbart med i, print(i)
    if tal % i == 0:
        print(i)
        
#%% 1.5.2 
### summan av geometrisk serie med särskild noggranhet

nog = float(input("nogrannheten = "))
q = float(input("q = "))
a = int(input("a = "))

S = a/(1-q)

S_new = 0

potens = 1 
sum = 0 

while (S - S_new)>nog :
    
    sum = sum + q**potens
    
    S_new = (a*sum)/q
      
    potens = potens + 1 
    
    print(sum)
    

#%% Upggift 1.5.5








#%% Uppgift 1.6.1
import numpy as np

a = float(input("a="))
b = float(input("b="))
N = int(input("N="))



step = (b-a)/(N-1)

sum = a 

L = []
 
while sum <= b:
    
    L.append(sum)
    sum = sum + step
        
    

## same as
l = list(np.linspace(1,10,5))
    
#%% Uppgift 1.6.2

type = input('välj list eller tupel:')
choice = input("välj up eller down:")



if type == "tupel":
    seq = input('ange dina värden för tupel(med mellanslag):')
    seq = seq.split()
    seq = tuple(seq)
    if choice == "up":
       seq = sorted(seq,reverse = True) 
    elif choice == "down":
        seq = sorted(seq)
elif type == "list":
    seq = input('ange dina värden för list(med mellanslag):')
    seq = seq.split()
else: 
    print("Error")
  







        
       
        