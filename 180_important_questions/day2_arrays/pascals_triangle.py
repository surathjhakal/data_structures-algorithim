def triangle(n):
    fixed=[]
    for i in range(n):
        temp=[]
        for j in range(i+1):
            if j==0 or j==i:
                temp.append(1)
            else:
                num=fixed[i-1][j-1]+fixed[i-1][j]
                temp.append(num)
        fixed.append(temp)

    #for printing
    for i in fixed:
        print((str(i)[1:-1]).replace(',',''))

def main():
    n=int(input())
    triangle(n)
main()
