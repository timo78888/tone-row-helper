#  finds inversion of row:
#  calculate intervals between notes
#  reverse said list of intervals
#  add in reversed intervals

def inversion(row):
    intervals = [0] * 11  # initialize interval list to 0
    flipped = [0] * 11
    inv_row = [0] * 12  # initialize result to 0
    for i in range(11):
        intervals[i] = row[i+1] - row[i]
    for i in range(11):
        flipped[i] = -1 * intervals[i]
    inv_row[0] = row[0]
    for i in range(11):
        inv_row[i+1] = inv_row[i] + flipped[i]
    for i in range(12):
        inv_row[i] = (inv_row[i]) % 12
    print(f"Original row: {row}")
    print(f"Inversion: {inv_row}")

row = [2, 3, 6, 5, 4, 7, 9, 1, 8, 0, 11, 10]

inversion(row)