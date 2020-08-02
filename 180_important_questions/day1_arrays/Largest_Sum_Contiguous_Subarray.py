def largest(my_list):
    maxi=0
    large=0
    for i in my_list:
        maxi+=i
        if maxi<0:
            maxi=0
        else:
            if large<maxi:
                large=maxi
    print(large)

def main():
    n=int(input())
    my_list=list(map(int,input().split()))
    largest(my_list)
main()
