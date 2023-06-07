#!/usr/bin/python3
i = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print(f"{(ch - i):c}", end="")
    i = 32 if i == 0 else 0
