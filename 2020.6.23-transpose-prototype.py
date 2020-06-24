def transpose(row, x):
    trans_row = [0] * 12
    for i in range(12):
        trans_row[i] = (row[i] + x) % 12
    print(trans_row)

x = int(input("A: "))

row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]

transpose(row, x)
