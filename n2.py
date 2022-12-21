print("i = ",end= " ")
ii = int(input())
for i in range(1,50):
    if 2 ** i >= ii + i + 1:
        print(i)
        break

