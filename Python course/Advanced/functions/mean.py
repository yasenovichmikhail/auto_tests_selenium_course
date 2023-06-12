def mean(*args):
    lst = []
    for i in args:
        if type(i) == int or type(i) == float:
           lst.append(i) 
        else:
            continue
    if len(lst) == 0:
        return(0.0)
    else:
        x = sum(lst) / len(lst)
    return(x)

print(mean())
    