N = 100
i = 2
for i in range(2, N):
    j = 2
    for j in range(2, i):
        if i % j == 0:  # to check the remainder
            break
    else:
        print(i, end=' ')  # to change all the numbers in one row
print('-' * 60)

num = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.append(i)
print(num)
