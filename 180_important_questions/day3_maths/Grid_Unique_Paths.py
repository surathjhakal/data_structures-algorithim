def uniquePaths(n,m):
    matrix=[]
    for i in range(n):   
        a =[]
        for j in range(m):
            a.append(1)
        matrix.append(a)
    print(matrix)
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    print(matrix[n-1][m-1])

def main():
    n=int(input("enter no. of rows you want:"))
    m=int(input("enter no. of columns you want:"))
    uniquePaths(m,n)

main()
