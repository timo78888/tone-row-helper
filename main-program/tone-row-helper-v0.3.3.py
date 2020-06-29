import time

row = [0] * 12  # initialize row to nothing
notes = list(range(12))  # initialize notes remaining to all of them

def print_key():  # prints the key for easy access
    print("Note key: ")
    print("0 = C, 1 = C#/Db, 2 = D, 3 = D#/Eb")
    print("4 = E, 5 = F, 6 = F#/Gb, 7 = G")
    print("8 = G#/Ab, 9 = A, 10 = A#/Bb, 11 = B\n\n")

def save_result(result, function):  # offers option to save results from a tone row calculation
    s = input("Would you like to save your result? (Y/N) ").lower()
    if s == 'y' or s == 'ye' or s == 'yes':
        print(f"Result saved in file tone_row.txt")
        res_file = open("tone_row.txt", "a")
        res_file.write(f"\n\n{function}: {result}")
    else:
        print("Result not saved.\n")

def transpose(row, x):  # transposes row
    trans_row = [0] * 12
    for i in range(12):
        trans_row[i] = (row[i] + x) % 12
    time.sleep(0.5)
    print(f"Original row: {row}")
    print(f"Row transposed by {x} semitones: {trans_row}\n")
    print_key()
    time.sleep(0.5)
    save_result(trans_row, f"Transposition by {x}")

def retrograde(row):  # writes retrograde of a row
    time.sleep(0.5)
    print(f"Original row: {row}")
    retro = [0] * 12
    for i in range(12):
        retro[i] = row[11-i]
    print(f"Retrograde: {retro}\n")
    print_key()
    time.sleep(0.5)
    save_result(retro, "Retrograde")

def invert(row):  # implemented to simplify down inversion and ri functions
    global inverted
    inverted = [0] * 12
    intervals = [0] * 11  # initialize interval list to 0
    inverted = [0] * 12  # initialize result to 0
    for i in range(11):
        intervals[i] = row[i+1] - row[i]
    inverted[0] = row[0]
    for i in range(11):
        inverted[i+1] = (inverted[i] - intervals[i]) % 12

def inversion(row):  # writes inversion of a row
    invert(row)
    inv_row = inverted
    time.sleep(0.5)
    print(f"Original row: {row}")
    print(f"Inversion: {inv_row}\n")
    print_key()
    time.sleep(0.5)
    save_result(inv_row, "Inversion")

def ri(row):  # calculates retrograde inversion
    rinv = [0] * 12
    invert(row)
    inv_row = inverted
    for i in range(12):
        rinv[i] = inv_row[11-i]
    print(f"Original row: {row}")
    print(f"Retrograde inversion: {rinv}\n")
    print_key()
    time.sleep(0.5)
    save_result(rinv, "Retrograde Inversion")

print("Tone Row Helper, v. 0.3.3")
print("Welcome! This program will do calculations for 12-tone row matrices.\n")
time.sleep(0.5)
print("Input notes as follows:")
print("0 = C, 1 = C#/Db, 2 = D, 3 = D#/Eb")
print("4 = E, 5 = F, 6 = F#/Gb, 7 = G")
print("8 = G#/Ab, 9 = A, 10 = A#/Bb, 11 = B")
time.sleep(0.5)
print("Integers less than 0 or greater than 12 will be converted modulo 12.\n")

for i in range(12):
    initial = input(f"Note #{i+1}: ")  # gets note input from user
    while initial.isdigit() == False:  # makes sure input is an integer
        initial = input(f"Input pitch classes as integers! Note #{i+1}: ")
    integer = int(initial) % 12  # converts input from string to integer in range [0, 12]

    # start checking for repeated values!!
    if i == 0:
        row[i] = integer
        notes.remove(integer)  # removes the value from the list of available notes
    else:
        if integer in notes:
            row[i] = integer
            notes.remove(integer)  # removes the value from the list of available notes
        else:  # i.e. if we find a repeat
            print("Oops: repeat detected!")
            print("Please select a note from the following list: ")
            print(notes)  # displays available notes
            rep = int(input("Make a selection; make sure that it is an integer and in the list: "))
            while rep not in notes:
                rep = int(input("Make a selection; make sure that it is an integer and in the list: "))
            row[i] = rep
            notes.remove(rep)

print("Your Tone Row:")  # prints inputted tone row
print(row)
time.sleep(0.5)

print("Row is being automatically saved in a file called tone_row.txt.\n")  # program auto-saves file in tone_row.txt
row_file = open("tone_row.txt", "w+")  # creates file called tone_row.txt
row_file.write("Calculations from Tone Row Helper\n\n")
row_file.write("Key:\n0 = C, 1 = C#/Db, 2 = D, 3 = D#/Eb\n4 = E, 5 = F, 6 = F#/Gb, 7 = G\n8 = G#/Ab, 9 = A, 10 = A#/Bb, 11 = B\n\n")
row_file.write(f"Original row: {row}")
row_file.close()

time.sleep(0.5)

print("There are a multitude of functions that this program will do once it is finished, such as transposition, inversion, and retrograde.")
print("Retrograde inversion can also be called easily.")
print("You can not stack functions yet... The dev is still working on this!")
print("Which function would you like to exceute?\n")

# list of commands that call functions
transpose_commands = ['t', 'trans', 'transpose', 'transposition', 'transpose row']
retrograde_commands = ['r', 'ret', 'retro', 'retrograde', 'rg', 'retrograde row', 'row retrograde']
inversion_commands = ['i', 'inv', 'invert', 'inversion', 'inverted', 'invert row', 'row inversion']
ri_commands = ['ri', 'rinv', 'retro inv', 'retrograde inversion', 'regrograde-inversion']

while True:
    print("T = transposition, I = inversion")
    print("R = retrograde, RI = retrograde inversion")
    print("K = see note key, Q = quit\n")
    get_function = input("Select function or quit: ").lower()

    if get_function == "q" or get_function == "quit":  # quits program
        print("Program will quit now.")
        time.sleep(0.25)
        quit()

    if get_function == 'k' or get_function == 'key':  # prints note key
        print_key()
        time.sleep(0.5)

    if get_function in transpose_commands:  # transposes row
        try:
            t = int(input("Number of semitones to transpose by (negative indicates downward): "))
            print("\n")
            transpose(row, t)
        except ValueError:
            print("Oops! That was not an integer; please try again.")

    if get_function in retrograde_commands:  # finds retrograde
        print("\n")
        retrograde(row)

    # inverts row
    if get_function in inversion_commands:
        print("\n")
        inversion(row)

    # finds retrograde inversion
    if get_function in ri_commands:
        print("\n")
        ri(row)
