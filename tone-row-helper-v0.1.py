import time

row = [0] * 12  # initialize row to nothing
notes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # initialize notes remaining to all of them

def print_key():  # prints the key for easy access
    print("Note key: ")
    print("0 = C, 1 = C#/Db, 2 = D, 3 = D#/Eb")
    print("4 = E, 5 = F, 6 = F#/Gb, 7 = G")
    print("8 = G#/Ab, 9 = A, 10 = A#/Bb, 11 = B")

def save_result(result, function):  # offers option to save results from a tone row calculation
    s = input("Would you like to save your result?").lower()
    if s == 'y' or s == 'ye' or s == 'yes':
        print(f"Result saved in file tone_row.txt")
        res_file = open("tone_row.txt", "a")
        res_file.write(f"\n\n{function}: {result}")
    else:
        print("Result not saved.")

def transpose(row, x):  # transposes row
    trans_row = [0] * 12
    for i in range(12):
        trans_row[i] = (row[i] + x) % 12
    time.sleep(0.5)
    print(f"Original row: {row}")
    print(f"Row transposed by {x} semitones: {trans_row}")
    print_key()
    time.sleep(0.5)
    save_result(trans_row, f"Transposition by {x}")

print("Tone Row Helper, v. 0.1")
time.sleep(0.25)
print("This program will do calculations for 12-tone row matrices.")
time.sleep(0.5)
print("Input notes as follows:")
print("0 = C, 1 = C#/Db, 2 = D, 3 = D#/Eb")
print("4 = E, 5 = F, 6 = F#/Gb, 7 = G")
print("8 = G#/Ab, 9 = A, 10 = A#/Bb, 11 = B")
time.sleep(0.5)
print("Integers less than 0 or greater than 12 will be converted modulo 12.")

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

print("Row is being automatically saved in a file called tone_row.txt.")  # program auto-saves file in tone_row.txt
row_file = open("tone_row.txt", "w+")  # creates file called tone_row.txt
row_file.write("Key:\n0 = C, 1 = C#/Db, 2 = D, 3 = D#/Eb\n4 = E, 5 = F, 6 = F#/Gb, 7 = G\n8 = G#/Ab, 9 = A, 10 = A#/Bb, 11 = B\n\n")
row_file.write(f"Original row: {row}")
row_file.close()

time.sleep(0.5)

print("There are a multitude of functions that this program will do once it is finished, such as transposition, inversion, retrograde, and retrograde inversion.")
print("You can not stack functions yet... The dev is still working on this!")
print("Which function would you like to exceute?")

while True:
    print("T = transposition, I = inversion")
    print("R = retrograde, RI = retrograde inversion")
    print("K = see note key, Q = quit")
    get_function = input("Select function or quit: ").lower()
    if get_function == "q" or get_function == "quit":  # quits program
        print("Program will quit now.")
        time.sleep(0.25)
        quit()

    if get_function == 'k' or get_function == 'key':  # prints note key
        print_key()
        time.sleep(0.5)

    if get_function == 't' or get_function == 'transpose' or get_function == 'transposition':  # transposes row
        try:
            tfactor = int(input("Number of semitones to transpose by (negative indicates downward): "))
            transpose(row, tfactor)
        except ValueError:
            print("Oops! That was not an integer; please try again.")