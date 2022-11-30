#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i and i != 8:
            print("{}{}".format(i, j), end=", ")
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
            break
#!/usr/bin/python3
for a1 in range(0, 10):
    for a2 in range(a1 + 1, 10):
        if a1 == 8 and a2 == 9:
            print("{}{}".format(a1, a2))
        else:
            print("{}{}".format(a1, a2), end=", ")
