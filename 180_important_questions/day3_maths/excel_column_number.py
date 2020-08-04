import string
def excel(s):
    d = dict.fromkeys(string.ascii_uppercase)
    count=0
    for i in d.keys():
        count+=1
        d[i]=count
    tot=0
    for i in s:
        tot=(tot*26)+d[i]
    print(tot)

def main():
    s=input()
    excel(s)

main()
