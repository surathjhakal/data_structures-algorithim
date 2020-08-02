def repeat_and_missing(my_list,n):
    missing=[]
    repeated=[]
    check=[]
    for i in range(1,n+1):
        if i not in my_list:
            missing.append(i)
    for i in my_list:
        if i in check:
            repeated.append(i)
        else:
            check.append(i)
    print("Missing: {}".format(str(missing)[1:-1]))
    print("Repeated: {}".format(str(repeated)[1:-1]))

def main():
    n=int(input())
    my_list=list(map(int,input().split()))
    repeat_and_missing(my_list,n)
main()
