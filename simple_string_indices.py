def solve(st,idx):

    if st[idx] == '(':
        parens_counter = 0
        for counter,i in enumerate(list(st)[idx:]):
            if i == '(': parens_counter += 1
            if i == ')': parens_counter -= 1
            if parens_counter == 0: return counter + idx

    return -1

print(solve("((1)23(45))(aB)",0))
print(solve("((1)23(45))(aB)",1))
print(solve("((1)23(45))(aB)",2))
print(solve("((1)23(45))(aB)",6))
print(solve("((1)23(45))(aB)",11))
print(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",11))
print(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",0))
print(solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))",19))
