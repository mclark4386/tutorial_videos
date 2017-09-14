#!/usr/bin/env python
import sys

def main():
    loopItems(sys.argv)
    fullSum = add(10,123)
    print(fullSum)
    sum,_,_ = add(10,123)
    print("10+123="+str(sum))

def loopItems(argv):
    print("Looping through %i item%s" % (len(argv), ('s' if len(argv)>1 else '')))
    for arg in argv :
        print(arg)
    print("=========================")

def add(x, y):
    return x+y,x,y

if __name__ == '__main__':
    main()
