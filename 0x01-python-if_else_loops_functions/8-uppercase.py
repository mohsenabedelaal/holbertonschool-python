#!/usr/bin/python3
def uppercase(str):
    result=""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            y=chr(ord(i)-32)
            result = result + y
        else:
            result = result + i
     print(result)
