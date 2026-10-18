#!/usr/bin/env python3

def ret_even-odd(num: int) -> None:
    if not num:
        return
    
    if  num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")
    return