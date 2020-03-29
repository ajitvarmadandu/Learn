def SORT(a):
    a.sort(key = lambda x : x[1])
    return a


if __name__ == '__main__':
    s=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        ele=[name,score]
        s.append(ele)
    SORT(s)
    s.reverse()
    a=dict(s)
    grade=list(a.values())
    name=list(a.keys())
    x=grade[-1]
    z=len(grade)
    for j in range(z):
        if(grade[j]==x):
            break
    l1=[key for [key,value] in a.items() if value == grade[j-1]]
    l1.sort()
    for k in range(len(l1)):
        print(l1[k])