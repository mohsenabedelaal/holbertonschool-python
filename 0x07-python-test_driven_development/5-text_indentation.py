#!/usr/bin/python3
"""
    5-text_indentation.py
    Module defining text indentation
    prints text indentation
"""


def text_indentation(text):
    """Print name if it is string """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        prev = 0
        for i in range(0, len(text)):
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print(text[prev:i+1].strip(), end="\n\n")
                prev = i+1
            if i == len(text)-1:
                print(text[prev:i+1].strip(), end="")
