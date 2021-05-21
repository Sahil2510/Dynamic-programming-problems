def LCS(X, Y):
    # To find the length of the strings...
    m = len(X)
    n = len(Y)

    # Declaring the array for storing the given dp values...
    T = [[None] * (n + 1) for i in range(m + 1)]


    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])


    return T[m][n]






X = "XYZZDCY"
Y = "DYZZYXX"
print("Length of LCS is ", LCS(X, Y))
