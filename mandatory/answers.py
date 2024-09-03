#!/usr/bin/python

def my_answer0(str):
    return str

def my_answer1(number):
    return number * 2
    
def my_answer2(str):
    return str.upper()
    
def my_answer3(str):
    return str[::-1]
    
def my_answer4(lst):
    x = lst.sort()
    return x
    
def my_answer5(lst):
    return lst[0:3]
    
def my_answer6(lst):
    x = []
    for item in lst:
        x.append(item * 5)
    return x
    
def my_answer7(lst):
    return lst[5]
    
def my_answer8(lst):
    return sorted(set(lst))
    #list(set(lst)) also worked for some reason, cant figure out why it sorted the lits also
    
def my_answer9(str):
    return str.replace("be", "python")
    
def my_answer10(str):
    return str[:-5:] + " " + str[:-5:-1]
    
def my_answer11(i):
    lst = [i]
    for x in range(1, 20):
        lst.append(lst[x - 1] + 5)
    return lst    
    
