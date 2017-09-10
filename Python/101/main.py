#!/usr/bin/env python3

#this is a single line comment
"""
This is a multi-line string
So this could be a whole block of code 
that would be completely ignored if we wanted...
since we don't set this to a variable it's basically ignored
There is no such thing as a multi-line comment ... 
just put "#"s in front of any lines you don't want interpreted
"""

#import the system module as an example
import sys;#you can also have comments at the end of a line

def main():
    print("Hello world!")
    print(sys.platform)
    print(sys.version)

    #this is basically the same thing as "print"...
    #  but print is easier and does some extras
    #  for you like the "\n" at the end
    sys.stdout.write("Bye!\n")


#This is needed to have the script function as a script
if __name__ == '__main__':#if we are being run as a script instead of imported from somewhere else
    main()#then run our main function
