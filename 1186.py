sm = input()

m = [[0 for i in range(12)] for j in range(12)]

c = 0

for i in range(12):
    for j in range(12):
        m[i][j] = float(input())

        if i + j > 11:
            c += m[i][j]

if sm == "M":
    c = c / 66

print("%.1f" %c)