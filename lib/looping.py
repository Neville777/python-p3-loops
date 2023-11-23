#!/usr/bin/env python3

def happy_new_year():
     s = 10
     while s >= 1:
         print(f"{s}")
         if s == 1:
             print("Happy New Year!")
         s -= 1

def square_integers(int_list):
    return [x**2 for x in int_list]
def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)