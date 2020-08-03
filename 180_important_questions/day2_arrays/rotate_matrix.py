  def rotate(l):
    k=int(input("how many times do you want to rotate"))
    n=len(l)
    for i in range(k):
        l=[l[-1]]+l[0:-1]
    print(l)
def main():
    l=[1,2,3,4,5,6,7]
    rotate(l)
main()
