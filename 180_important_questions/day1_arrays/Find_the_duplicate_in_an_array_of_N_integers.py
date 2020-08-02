def duplicate(my_list):
    new=[]
    print("the duplicate numbers are: ",end='')
    for i in my_list:
        if i in new:
            print(i,end=', ')
        else:
            new.append(i)
def main():
    n=int(input())
    my_list=list(map(int,input().split()))
    duplicate(my_list)
main()
