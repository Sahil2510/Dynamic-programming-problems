
def memoization(n, search):

    if n == 0 or n == 1:
        search[n] = n


    if search[n] is None:
        search[n] = memoization(n - 1, search) + memoization(n - 2, search)


    return search[n]




def main():
    n = 5


    search = [None] * (101)
    print("The Fibonacci sum is (Memoized): ", memoization(n, search))


if __name__ == "__main__":
   main()
