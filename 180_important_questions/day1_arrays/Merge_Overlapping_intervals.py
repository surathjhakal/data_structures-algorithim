def overlaping(my_list):
    my_list.sort(key = lambda x:x[0])
    i = 1
    while i < len(my_list):
        if my_list[i][0] <= my_list[i-1][1]:
            my_list[i-1][0] = min(my_list[i-1][0], my_list[i][0])
            my_list[i-1][1] = max(my_list[i-1][1], my_list[i][1])
            my_list.pop(i)
        else:
            i += 1
    print(my_list)
def main():
    my_list=[[1,9],[1,2],[5,7],[2,11]]
    overlaping(my_list)
main()
