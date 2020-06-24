def retrograde(row):
    print(row)
    retro = [0] * 12
    for i in range(12):
        retro[i] = row[11-i]
    print(retro)

row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

retrograde(row)