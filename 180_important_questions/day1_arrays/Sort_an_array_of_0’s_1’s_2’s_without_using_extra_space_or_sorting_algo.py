  
def sorting(my_list,n):
    for i in range(n-1,0,-1):
        maxi=i
        for j in range(i-1):
            if my_list[maxi]<my_list[j]:
                maxi=j
        my_list[i],my_list[maxi]=my_list[maxi],my_list[i]
    print(my_list)

def main():
    n=int(input())
    my_list=list(map(int,input().split()))
    sorting(my_list,n)
main()
