#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:15:14 2021

@author: calvinsmith
"""

#%% Uppgift 2.1.1 (2p) (REDOVISAD)

def func_convert(number,s):
    if s == "hex":
        out = hex(number)
    elif s == "bin":
        out = bin(number)
    elif s == "oct":
        out = oct(number)
    
    return out 
        
#%% Uppgift 2.1.3 (REDOVISAD)

def is_prime(number):
    
    prime = True
    
    for i in range(2,number):
        if number % i == 0:
            prime = False
            
    return prime
    
#%% Uppgift 2.2.1 (redovisad)

def n_geom(a_1,q,n):
    
    a = [0]*n
    a[0] = a_1
    
    for i in range(1,n):
        a[i] = a[i-1]*q
    
    return a[n-1]

    

#%% 2.3.1 (REDOVISAD)

def kvadrat(*arg):
    
       
   s = 0
    
   # check if empty 
   if len(arg) == 0:
       print("Empty argument")
       return
       
   # check if numeric 
   for i in range(0,len(arg)):
        if isinstance(arg[i],(float,int)) == False:
            print("Wrong datatype")
            return
        else:
            s = s + arg[i]**2    
    
   return s

           
            
#%%

file_one = open("file_one.txt","w")  
    
file_one.write("Hej jag heter calvin\nHej då\nhej igen Calvin\nhej hej hej\nhej")
file_one.close()

#%% Uppgift 2.5.2 (REDOVISAD)
def counts(file,word):
    
    word = word.lower()
    
    file_read = open(file,"r")
    
    count = 0
    
    for s in file_read:
        
        text = s.lower()
        count = count + text.count(word)
    
    file_read.close()    
    return count        
    
#%% 2.6.3 (REDOVISAD)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 



def morse(text):
    
    text = text.upper()
    
    morse_code = ''
    
    for i in text:
        
        if i.isalpha() == True:
            morse_code += MORSE_CODE_DICT[i] + ' '
        else: 
            morse_code += ' '
    
    return  morse_code


code = morse("My name is Calvin")


def unmorse(morse_code):
    
    text_out = ''
    
    s = morse_code.split()
    
    morse_alphabet = list(MORSE_CODE_DICT.values())
    alphabet = list(MORSE_CODE_DICT.keys())
    

    for i in range(len(s)):
        for j in range(len(morse_alphabet)):
            if s[i] == morse_alphabet[j]:
                text_out += alphabet[j]
    
    return text_out
        
        
        
        
        
    
    
    
    