A = [9,3,9,3,5,6,6]
p = 1
for a in A:
    p = p + a
for a in A:
    p = p - a
    c = p/(len(A)-1)
    if c == 2:
        print a
        break
    p = p + a
