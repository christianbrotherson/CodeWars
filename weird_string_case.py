def to_weird_case(s):
    a = s.split(' ')
    b = []

    for i in a:
        b.append(list(i)) 
    
    print(b)
    for i in b:
        for count, x in enumerate(i):
            if count % 2 == 0:
                i[count] = x.upper()
            else:
                i[count] = x.lower()


    c = []
    for i in b:
        c.append("".join(i))

    return " ".join(c)

print(to_weird_case('Hi there hoow are you'))