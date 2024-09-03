#!/usr/bin/pyton

def odd_or_even():
    num = input("type a number\n")
    try:
        if int(num) % 2 == 0:
            print("number is even")
        else:
            print("number is odd")
    except:
        print("not a number")
        odd_or_even()

odd_or_even()

    
