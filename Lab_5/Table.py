#Table.py
SIZE1 = 4
SIZE2 = 4
table = []
for a in range(SIZE1):
    s = [0]*SIZE2
    table.append(s)

for a in range(SIZE1):
    for b in range(SIZE2-1, -1, -1):
        table[a][b] = a + b * 2.0
        print(str(table[a][b]) + " " + str(a) + " " + str(b))

for a in range(SIZE2, 0, -1):
    value = 0
    for b in range(0, a, 1):
        value = value + table[b][a - 1];
    print(a, value)
