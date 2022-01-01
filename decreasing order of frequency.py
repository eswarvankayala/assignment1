def str_count(a):
    d=dict()
    for key in a:
        if key not in d:
            d[key]=1
        else:
            d[key]=d[key]+1
    return d
c=str(input('please enter a string\n'))
b=str_count(c)

def sorting(b):
    list1=list(b.values())
    list2=list(b.keys())
    list1.sort()
    list1.reverse()
    for k in list1:
        for key in list2:
            if b[key]==k:
                print(key,':',k)
                list2.remove(key)
sorting(b)
