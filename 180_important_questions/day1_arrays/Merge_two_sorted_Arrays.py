def merge(arr1,arr2):
    new=arr1+arr2
    new.sort()
    print("arr1: {}".format(new[:len(arr1)]))
    print("arr2: {}".format(new[len(arr1):]))
def main():
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    merge(arr1,arr2)
main()
