#!/usr/bin/python3
print(*["%c" % a for a in range(ord('a'), ord ('z') + 1) if a not in (ord('e'), (ord('q'))], sep='', end='')
