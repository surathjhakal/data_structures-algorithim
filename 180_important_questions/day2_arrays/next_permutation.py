def permute(s):
    output = []

    if len(s) <= 1:
        output = [s]
    else:
        for i, num in enumerate(s):
            for p in permute(s[:i] + s[i + 1:]):
                output += [[num] + p]
    return output

def main():
    s=[3,9,4,1,2]
    s.sort()
    o=permute(s)
    for i in range(len(o)):
        if o[i]==[3,9,4,1,2]:
            print(o[i+1])
            break
main()
