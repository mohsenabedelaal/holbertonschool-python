#!/usr/bin/python3
def roman_to_int(roman_number):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    if isinstance(roman_number, str) and roman_number is not None:
        for i in range(len(roman_number)):
            comp1 = roman_number[i - 1]
            if i > 0 and rom_val[roman_number[i]] > rom_val[comp1]:
                int_val += rom_val[roman_number[i]] - 2 * rom_val[comp1]
            else:
                int_val += rom_val[roman_number[i]]
        return int_val
    return 0
