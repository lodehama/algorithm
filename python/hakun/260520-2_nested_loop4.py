for y in range(5):

    for space in range(y):
        print(" ", end="")

    for star in range(9 - 2 * y):
        print("*", end="")

    print()