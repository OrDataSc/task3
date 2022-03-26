#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#a
Created on Tue Mar 22 14:12:53 2022

@author: ortzadok
"""
def read_line(n, file):
    try:
        if type(n) != int or type(file) != str:
            return "invalid input detected"
        text = open(file,'r')
        count = 0
        lines = text.readlines()
        for line in lines:
            count = count + 1
        if n >= count:
            return f"line {n} doen't exist"
        elif lines[n-1] == ' \n':
            return f'" "'
        else:
            return lines[n-1].rstrip()
        
    except:
        return "file not found"

print(read_line(20, 'ex3_text.txt')) 
print(read_line(9, 'ex4_text.txt')) 
print(read_line(233, 'ex3_text.txt')) 
print(read_line("c", 'ex3_text.txt'))
print(read_line(9, 'ex3_text.txt')) 

#b
def longest_words(file) :
    try:
        text = open(file,'r')    
        mylist = []
        lines = []
        word_len = dict()
        for line in text:
            line = line.rstrip('\n,-[]"". ')
            lines.append(line)
        length1 = len(lines)
        for words in range(length1):
           mylist.append(lines[words].split())
        for word in mylist:
            for keys in word:
                word_len[keys] = len(keys)
        return sorted(word_len, key=word_len.get, reverse=True)[:5]    
    except:
        return f"file not found\n[]"

    
print(longest_words('ex3_text.txt')) 
print(longest_words('ex3_text.xt')) 

