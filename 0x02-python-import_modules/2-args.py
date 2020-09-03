#!/usr/bin/python3
import sys


def list_arg(arg):
    if len(arg)-1 == 0:
        print('{} arguments.'.format(len(arg)-1))
    elif len(arg)-1 == 1:
        print('{} argument:'.format(len(arg)-1))
        print('{} : {}'.format(1, arg[1]))
    else:
        print('{} arguments:'.format(len(arg)-1))
        for i in range(1, len(arg)):
            print('{}: {}'.format(i, arg[i]))
if __name__ == '__main__':
    list_arg(sys.argv)
