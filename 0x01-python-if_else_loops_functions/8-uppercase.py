#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(c) - 32)
        print(f"{ch:c}",  end="")
    print("")
