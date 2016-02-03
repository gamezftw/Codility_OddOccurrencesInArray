A = [9, 3, 9, 3, 9, 7, 9]
B = {}
for i in range(len(A)):
    B[A[i]] = 0;
for i in range(len(A)):
    B[A[i]] = B[A[i]] + 1;
for i in range(len(A)):
    if B[A[i]] % 2 == 1:
        print A[i]
        break
#100%