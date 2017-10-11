#!/usr/bin/env python3

def main(): 
    x = int(input("Factorial of:"))
    ff = fact_for(x)
    fw = fact_while(x)
    f  = fact(x)
    print_facts(ff, fw, f)

def print_facts(ff, fw, f):
    print("""for loop(%i)
while loop(%i)
recursive(%i)""" % (ff,fw,f))
    
def fact_for(x):
    ret = 1
    for i in range(x,0,-1):
        ret *= i 
    return ret

def fact_while(x):
    ret = 1
    i = 1
    while i <= x:
        ret *= i
        i += 1
    return ret

def fact(x):
    if x <= 1:
        return 1
    return x * fact(x-1)

if __name__ == '__main__':
    main()
