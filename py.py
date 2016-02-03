A = [4, 3, 9, 3, 9, 7, 9, 3, 3, 7, 4]
b = 0
k = 0
for i in range(len(A)):
    b = 0
    for j in range(i + 1, len(A) - k):
        if A[i] == A[j]:
            A[j], A[len(A) - k - 1] = A[len(A) - k - 1], A[j]
            b = 1
            k += 1
            break
    if b == 0 and A[i] != 0:
        print A[i]
        break
        # Correctness100% Performance25% Task score
