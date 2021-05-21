# Tabulated Dynamic Programming:

def bottom_up(p):

    # array declaration

    f = [0] * (p + 1)

    # base case
    f[1] = 1

# calculating the fibonacci and storing the given values

    for i in range(2, p + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[p]


# Driver program to test the above function
def main():
    p = 5
    print("Fibonacci Sum is(Tabular): ", bottom_up(p))


if __name__ == "__main__":
    main()
