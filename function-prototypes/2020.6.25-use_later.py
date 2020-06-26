#  save result to use later
def use_later(result):
    global saved_result
    saved_result = [0] * 12
    u = input("Do you wish to save this result for later use? ")
    if u == 'yes' or u == 'ye' or u == 'y':
        saved_result = result
    else:
        return


def transpose(row):
    x = int((input("Transposition factor: ")))
    trans_row = [0] * 12
    for i in range(12):
        trans_row[i] = (row[i] + x) % 12
    print(trans_row)
    use_later(trans_row)

row = [0, 2, 1, 3, 4, 6, 5, 7, 8, 9, 11, 10]

transpose(row)
transpose(saved_result)