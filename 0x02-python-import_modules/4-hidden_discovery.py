#!/usr/bin/python3
import hidden_4


def hidden(str):
    for i in dir(str):
        if i[0] != "_":
            print(i, end="\n")
if __name__ == "__main__":
    hidden(hidden_4)
