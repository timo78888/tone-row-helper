Motivation:

The "12-tone row" in music is a method of composition that is heavily based on mathematical constructs.
The 12-tone row is a way of arranging the 12 chromatic notes (C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B) such that all 12 notes are used once.
Order matters for a 12-tone row, so a 12-tone row is essentially an array of notes.
There are only 12! = 479001600 unique rows; however, some are derivations from others using basic functions.
To facilitate the discussion of tone rows, each chromatic note is assigned a pitch class value as follows:

0 = C, 1 = C#/Db, 2 = D, 3 = D#/Eb
4 = E, 5 = F, 6 = F#/Gb, 7 = G
8 = G#/Ab, 9 = A, 10 = A#/Bb, 11 = B

Now implementation of those "basic functions" is even easier if we use these pitch class values.

The Basic Functions:
  Transposition: Taking a row then adding an integer to each value in the row.
    Example: take the row [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
    If we transpose by 4, the result is: [4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3].
    Note the wraparound (i.e. we count in modulo 12) from 11 to 0 - this is becuase the chromatic notes repeat: 1 note above B is C.
  Retrograde: Taking a row and then reversing it.
    Example: take the same row: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
    The retrograde will be [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0].
  Inversion: Taking a row and reversing the interval between two notes (that is, the difference between two notes).
    Example: take the row [2, 6, 3, 4, 5, 1, 0, 8, 7, 9, 10, 11].
    Computing the differences (aka intervals between two notes gives: [6-2, 3-6, 4-3, 5-4, 1-5, 0-1, 8-0, 7-8, 9-7, 10-9, 11-10]
      or just [4, -3, 1, 1, -4, -1, 8, -2, 2, 1, 1]
    We flip the signs of each of those differences: [-4, 3, -1, -1, 4, 1, -8, 2, -2, -1, -1] and use these differences to compute the new row, which still starts from 2:
    [2, -2, ...] mod 12 = [2, 10, ...]
