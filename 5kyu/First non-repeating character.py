def first_non_repeating_letter(string):
    char_dict = dict.fromkeys(set(string.lower()),0)

    for c in string.lower(): 
        char_dict[c] += 1
    for c in string:
        if char_dict[c.lower()] < 2:
            return c
            break
    return ''

print(first_non_repeating_letter('abc'))