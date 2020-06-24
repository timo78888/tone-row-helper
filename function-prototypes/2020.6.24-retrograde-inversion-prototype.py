#  calculates retrograde inversion = inversion first and then retrograde

def ri(row):
    intervals = [0] * 11  # initialize interval list to 0
    flipped = [0] * 11
    inv_row = [0] * 12  # initialize inversion to 0
    rinv = [0] * 12  # initialize result to 0
    for i in range(11):
        intervals[i] = row[i+1] - row[i]
    for i in range(11):
        flipped[i] = -1 * intervals[i]
    inv_row[0] = row[0]
    for i in range(11):
        inv_row[i+1] = inv_row[i] + flipped[i]
    for i in range(12):
        inv_row[i] = (inv_row[i]) % 12
    for i in range(12):
        rinv[i] = inv_row[11-i]
    print(rinv)

row = [6, 8, 2, 9, 0, 1, 10, 5, 7, 11, 3, 4]

ri(row)
