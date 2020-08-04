def Two_sum(l,check):
    hash_map={}
    for i in range(len(l)):
        hash_map[l[i]]=i
    sol=[]
    for j in range(len(l)):
        if (check-l[j]) in hash_map:
            if i!=hash_map[check-l[j]]:
                sol.append([j,hash_map[check-l[j]]])
                del hash_map[l[j]],hash_map[check-l[j]]
    print(sol)
def main():
    l=[2,7,11,-2]
    check=int(input("Enter the sum number:"))
    Two_sum(l,check)

main()
