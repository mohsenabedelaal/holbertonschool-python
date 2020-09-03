#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv)-1 < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)
    else:
        lists = sys.argv
        a = int(lists[1])
        b = int(lists[3])
        if lists[2] == '+':
            print('{} {} {} = {}'.format(a, lists[2], b, add(a, b)))
            exit(0)
        elif lists[2] == '-':
            print('{} {} {} = {}'.format(a, lists[2], b, sub(a, b)))
            exit(0)
        elif lists[2] == '*':
            print('{} {} {} = {}'.format(a, lists[2], b, mul(a, b)))
            exit(0)
        elif lists[2] == '/':
            print('{} {} {} = {}'.format(a, lists[2], b, div(a, b)))
            exit(0)
        else:
            s = "Unknown operator. Available operators: +, -, * and /"
            print(s, end="\n")
            exit(1)
