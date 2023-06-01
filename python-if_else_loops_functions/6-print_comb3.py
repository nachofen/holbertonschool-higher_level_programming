#!/usr/bin/python3
for i in range(1, 10):
    print('{:02d}'.format(i), end=", ")
for i in range(10, 89):
    if i // 10 < i % 10:
        print("{:02d}".format(i), end=", ")
    if i == 88:
        print("89")
