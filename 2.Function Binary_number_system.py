
print("""Function Binary_number_system: """)


while True:
    
    q = ""

    f = []

    u = []

    i = int(input())

    u.append(i)

    while i != 0 and i != 1:
        i //= 2
        u.append(i)

    for k in u:
        k %= 2
        if k == 0:
            f.append('0')
        elif k == 1:
            f.append('1')
        else:
            print('Error')

    f.reverse()
    for w in f:
        q += w

    print(q)
    print("")
    print(u)

