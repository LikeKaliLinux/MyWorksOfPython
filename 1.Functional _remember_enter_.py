c = 0
x = ": "

g = " "
g = list(g)

while True:
    s = input()
    if s in x:
        c += 1
    else:
        x += s + ", "
    for a in s:
        if a in g:
            c += 1
        else:
            g.append(a)
    print(x)
    print(g)
     
     