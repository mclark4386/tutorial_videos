#!/usr/bin/env python3
def main():
    x = 10.0
    y = float(10)
    print(x,y)
    x,y = "blue",42
    print(x,y)

    list = [ 'this', 'can have', 'whatever in it', 42, 'and can be edited at runtime']
    tup = ('can have whatever', 64, 'but read-only')
    dict = {'name':'Bob', 42:"age"}
    
    y = input("What is your name:")
    print("Welcome, %s!" % y)

    x = int(input("Please enter a number:"))
    print("You entered the number \"%d\". (%d^2) == %d" % (x,x,x**2))

    x = 42
    print(dict["name"] + ' is 42 years of ' + dict[x])
    
if __name__ == '__main__':
    main()
