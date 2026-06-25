for y in range(5):

    for space in range(4 - y):
        print(" ", end="")

    for star in range(2 * y + 1):
        print("*", end="")

    print()