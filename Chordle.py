import random

#ADD REMAINING NOTES PART
#IMPROVE NUMBER OF GUESSES LEFT (depending on type of chord and number of chords)

TRIADS = {'C maj': ('C', 'E', 'G'),
          'C min': ('C', 'Eb', 'G'),
          'C aug': ('C', 'E', 'G#'),
          'C dim': ('C', 'Eb', 'Gb'),

          'C# maj': ('C#', 'E#', 'G#'),
          'C# min': ('C#', 'E', 'G#'),
          'C# aug': ('C#', 'E#', 'Gx'),
          'C# dim': ('C#', 'E', 'G'),

          'Db maj': ('Db', 'F', 'Ab'),
          'Db min': ('Db', 'Fb', 'Ab'),
          'Db aug': ('Db', 'F', 'A'),
          'Db dim': ('Db', 'Fb', 'Abb'),

          'D maj': ('D', 'F#', 'A'),
          'D min': ('D', 'F', 'A'),
          'D aug': ('D', 'F#', 'A#'),
          'D dim': ('D', 'F', 'Ab'),

          'D# maj': ('D#', 'Fx', 'A#'),
          'D# min': ('D#', 'F#', 'A#'),
          'D# aug': ('D#', 'Fx', 'Ax'),
          'D# dim': ('D#', 'F#', 'A'),

          'Eb maj': ('Eb', 'G', 'Bb'),
          'Eb min': ('Eb', 'Gb', 'Bb'),
          'Eb aug': ('Eb', 'G', 'B'),
          'Eb dim': ('Eb', 'Gb', 'Bbb'),

          'E maj': ('E', 'G#', 'B'),
          'E min': ('E', 'G', 'B'),
          'E aug': ('E', 'G#', 'B#'),
          'E dim': ('E', 'G', 'Bb'),
          
          'F maj': ('F', 'A', 'C'),
          'F min': ('F', 'Ab', 'C'),
          'F aug': ('F', 'A', 'C#'),
          'F dim': ('F', 'Ab', 'Cb'),
          
          'F# maj': ('F#', 'A#', 'C#'),
          'F# min': ('F#', 'A', 'C#'),
          'F# aug': ('F#', 'A#', 'Cx'),
          'F# dim': ('F#', 'A', 'C'),

          'Gb maj': ('Gb', 'Bb', 'Db'),
          'Gb min': ('Gb', 'Bbb', 'Db'),
          'Gb aug': ('Gb', 'Bb', 'D'),
          'Gb dim': ('Gb', 'Bbb', 'Dbb'),
          
          'G maj': ('G', 'B', 'D'),
          'G min': ('G', 'Bb', 'D'),
          'G aug': ('G', 'B', 'D#'),
          'G dim': ('G', 'Bb', 'Db'),
          
          'G# maj': ('G#', 'B#', 'D#'),
          'G# min': ('G#', 'B', 'D#'),
          'G# aug': ('G#', 'B#', 'Dx'),
          'G# dim': ('G#', 'B', 'D'),

          'Ab maj': ('Ab', 'C', 'Eb'),
          'Ab min': ('Ab', 'Cb', 'Eb'),
          'Ab aug': ('Ab', 'C', 'E'),
          'Ab dim': ('Ab', 'Cb', 'Ebb'),
          
          'A maj': ('A', 'C#', 'E'),
          'A min': ('A', 'C', 'E'),
          'A aug': ('A', 'C#', 'E#'),
          'A dim': ('A', 'C', 'Eb'),
          
          'A# maj': ('A#', 'Cx', 'E#'),
          'A# min': ('A#', 'C#', 'E#'),
          'A# aug': ('A#', 'Cx', 'Ex'),
          'A# dim': ('A#', 'C#', 'E'),

          'Bb maj': ('Bb', 'D', 'F'),
          'Bb min': ('Bb', 'Db', 'F'),
          'Bb aug': ('Bb', 'D', 'F#'),
          'Bb dim': ('Bb', 'Db', 'Fb'),

          'B maj': ('B', 'D#', 'F#'),
          'B min': ('B', 'D', 'F#'),
          'B aug': ('B', 'D#', 'Fx'),
          'B dim': ('B', 'D', 'F')
          }

SEVENTHS = {'C major 7': TRIADS['C maj'] + ('B',),
            'C dominant 7': TRIADS['C maj'] + ('Bb',),
            'C minor 7': TRIADS['C min'] + ('Bb',),
            'C half dim 7': TRIADS['C dim'] + ('Bb',),
            'C full dim 7': TRIADS['C dim'] + ('Bbb',),

            'C# major 7': TRIADS['C# maj'] + ('B#',),
            'C# dominant 7': TRIADS['C# maj'] + ('B',),
            'C# minor 7': TRIADS['C# min'] + ('B',),
            'C# half dim 7': TRIADS['C# dim'] + ('B',),
            'C# full dim 7': TRIADS['C# dim'] + ('Bb',),

            'Db major 7': TRIADS['Db maj'] + ('C',),
            'Db dominant 7': TRIADS['Db maj'] + ('Cb',),
            'Db minor 7': TRIADS['Db min'] + ('Cb',),
            'Db half dim 7': TRIADS['Db dim'] + ('Cb',),
            'Db full dim 7': TRIADS['Db dim'] + ('Cbb',),

            'D major 7': TRIADS['D maj'] + ('C#',),
            'D dominant 7': TRIADS['D maj'] + ('C',),
            'D minor 7': TRIADS['D min'] + ('C',),
            'D half dim 7': TRIADS['D dim'] + ('C',),
            'D full dim 7': TRIADS['D dim'] + ('Cb',),

            'D# major 7': TRIADS['D# maj'] + ('Cx',),
            'D# dominant 7': TRIADS['D# maj'] + ('C#',),
            'D# minor 7': TRIADS['D# min'] + ('C#',),
            'D# half dim 7': TRIADS['D# dim'] + ('C#',),
            'D# full dim 7': TRIADS['D# dim'] + ('C',),

            'Eb major 7': TRIADS['Eb maj'] + ('D',),
            'Eb dominant 7': TRIADS['Eb maj'] + ('Db',),
            'Eb minor 7': TRIADS['Eb min'] + ('Db',),
            'Eb half dim 7': TRIADS['Eb dim'] + ('Db',),
            'Eb full dim 7': TRIADS['Eb dim'] + ('Dbb',),

            'E major 7': TRIADS['E maj'] + ('D#',),
            'E dominant 7': TRIADS['E maj'] + ('D',),
            'E minor 7': TRIADS['E min'] + ('D',),
            'E half dim 7': TRIADS['E dim'] + ('D',),
            'E full dim 7': TRIADS['E dim'] + ('Db',),

            'F major 7': TRIADS['F maj'] + ('E',),
            'F dominant 7': TRIADS['F maj'] + ('Eb',),
            'F minor 7': TRIADS['F min'] + ('Eb',),
            'F half dim 7': TRIADS['F dim'] + ('Eb',),
            'F full dim 7': TRIADS['F dim'] + ('Ebb',),

            'F# major 7': TRIADS['F# maj'] + ('E#',),
            'F# dominant 7': TRIADS['F# maj'] + ('E',),
            'F# minor 7': TRIADS['F# min'] + ('E',),
            'F# half dim 7': TRIADS['F# dim'] + ('E',),
            'F# full dim 7': TRIADS['F# dim'] + ('Eb',),

            'Gb major 7': TRIADS['Gb maj'] + ('F',),
            'Gb dominant 7': TRIADS['Gb maj'] + ('Fb',),
            'Gb minor 7': TRIADS['Gb min'] + ('Fb',),
            'Gb half dim 7': TRIADS['Gb dim'] + ('Fb',),
            'Gb full dim 7': TRIADS['Gb dim'] + ('Fbb',),

            'G major 7': TRIADS['G maj'] + ('F#',),
            'G dominant 7': TRIADS['G maj'] + ('F',),
            'G minor 7': TRIADS['G min'] + ('F',),
            'G half dim 7': TRIADS['G dim'] + ('F',),
            'G full dim 7': TRIADS['G dim'] + ('Fb',),

            'G# major 7': TRIADS['G# maj'] + ('Fx',),
            'G# dominant 7': TRIADS['G# maj'] + ('F#',),
            'G# minor 7': TRIADS['G# min'] + ('F#',),
            'G# half dim 7': TRIADS['G# dim'] + ('F#',),
            'G# full dim 7': TRIADS['G# dim'] + ('F',),

            'Ab major 7': TRIADS['Ab maj'] + ('G',),
            'Ab dominant 7': TRIADS['Ab maj'] + ('Gb',),
            'Ab minor 7': TRIADS['Ab min'] + ('Gb',),
            'Ab half dim 7': TRIADS['Ab dim'] + ('Gb',),
            'Ab full dim 7': TRIADS['Ab dim'] + ('Gbb',),

            'A major 7': TRIADS['A maj'] + ('G#',),
            'A dominant 7': TRIADS['A maj'] + ('G',),
            'A minor 7': TRIADS['A min'] + ('G',),
            'A half dim 7': TRIADS['A dim'] + ('G',),
            'A full dim 7': TRIADS['A dim'] + ('Gb',),

            'Bb major 7': TRIADS['Bb maj'] + ('A',),
            'Bb dominant 7': TRIADS['Bb maj'] + ('Ab',),
            'Bb minor 7': TRIADS['Bb min'] + ('Ab',),
            'Bb half dim 7': TRIADS['Bb dim'] + ('Ab',),
            'Bb full dim 7': TRIADS['Bb dim'] + ('Abb',),

            'B major 7': TRIADS['B maj'] + ('A#',),
            'B dominant 7': TRIADS['B maj'] + ('A',),
            'B minor 7': TRIADS['B min'] + ('A',),
            'B half dim 7': TRIADS['B dim'] + ('A',),
            'B full dim 7': TRIADS['B dim'] + ('Ab',)
            }

INVERSIONS = {0: 'Root position', 1: '1st inversion', 2: '2nd inversion', 3: '3rd inversion'}

COLORS = {'W': '\033[90m', 'Y': '\033[33m', 'G': '\033[32m'}

def game(chord_dict, num_notes, chord_nums):
    attempts = int(num_notes*2 + chord_nums*1.5)
    valid_notes = set()
    for chord in chord_dict:
        for note in chord_dict[chord]:
            valid_notes.add(note)

    chords = tuple(chord_dict.keys())
    inversions = [random.randint(0, num_notes-1) for i in range(chord_nums)]
    chosen_chords = [[chords[random.randint(0, len(chords)-1)], ' ' + INVERSIONS[inversions[i]]] for i in range(chord_nums)]
    new_chords = [[chord_dict[chosen_chords[j][0]][(inversions[j]+i) % num_notes] for i in range(num_notes)] for j in range(chord_nums)]
    guess_storage = []
        
    while attempts:
        if attempts == 1:
            print('\nYou have 1 attempt left')
        else:
            print('\nYou have', attempts, 'attempts left')

        guess = tuple(input('Guess the chord: ').split())
        
        if len(guess) != num_notes:
            print('Invalid chord, try again (length error)')
            continue

        note_continue = True
        for note in guess:
            if note not in valid_notes:
                note_continue = False
                continue

        if note_continue == False:
            print('Invalid chord, try again (note error)')
            continue

        chord_continue = False
        for key in chord_dict:
            if set(chord_dict[key]) == set(guess):
                chord_continue = True

        if chord_continue == False:
            print('Invalid chord, try again (chord error)')
            continue

        matches = [['W' for i in range(num_notes)] for j in range(chord_nums)]
        for j in range(chord_nums):
            for i in range(num_notes):
                if guess[i] in new_chords[j]:
                    matches[j][i] = 'Y'
            if guess[0] == new_chords[j][0]:
                matches[j][0] = 'G'
            if matches[j].count('W') == 0 and matches[j][0] == 'G':
                matches[j] = ['G' for i in range(num_notes)]

        colored_chords = []
        for i in range(chord_nums):
            if chosen_chords[i] == 'done':
                colored_chords += ['    ' * num_notes]
            else:
                colored_chords += [COLORS[matches[i][j]] + guess[j] + ' '*(4-len(guess[j])) for j in range(num_notes)]
            colored_chords += COLORS['W'] + '|'

        guess_storage.append(''.join(colored_chords))
        for item in guess_storage:
            print(item)

        for i in range(len(matches)):
            if matches[i][0] == 'G' and matches[i].count('W') == 0:
                chosen_chords[i] = 'done'

        print('\033[0m')
        if chosen_chords.count('done') == chord_nums:
            break
        
        attempts -= 1

    solved = chosen_chords.count('done')
    if solved < chord_nums:
        remaining = []
        for chord in chosen_chords:
            if chord != 'done':
                remaining.append(chord)
        print('\033[96m' + "Sorry, you lost the game. The remaining chords were:")
        for i in range(len(remaining)):
            print(' '.join(remaining[i]))
    else:
        print('\033[96m' + "Yay, you won!")
    print('\033[0m')

while True:
    print("\nWelcome to CHORDLE!")
    print("Rules:\n  Inputs can be any of these triads/sevenths in any inversion:")
    print("    Triads: Major, Minor, Augmented, Diminished")
    print("    Sevenths: Major, Dominant, Minor, Half Diminished, Full Diminished")
    print("    Inversions: Root, 1st, 2nd, 3rd (for seventh chords)")
    print("    Example Triad: C E G")
    print("    Example Seventh: C E G B")
    print("  White key note names must be captitalized")
    print("  Sharp: #")
    print("  Double-sharp: x")
    print("  Flat: b")
    print("  Double-flat: bb")
    print("  Put a space in between each note for a valid guess")
    print("    You are given 6 attempts")
    print(COLORS['Y'] + "  If a note is yellow, that means that it is in the chord but not the base of the chord")
    print(COLORS['G'] + "  If a note is green, that means that it is the base of the chord")
    print(COLORS['W'] + "  If a note is gray, that means that the note is not in the chord\n")
    game_mode = input('\033[0m' + "Type 1 for Triads or type 2 for Sevenths: ")

    while game_mode != '1' and game_mode != '2':
        game_mode = input("Type 1 for Triads or type 2 for Sevenths: ")

    while True:
        num_chords = input("Type a number between 1 and 6 for number of chords to guess: ")
        if num_chords.isnumeric() and float(num_chords) % 1 == 0 and int(num_chords) >= 1 and int(num_chords) <= 6:
            break
    
    if game_mode == '1':
        game(TRIADS, 3, int(num_chords))
    else:
        game(SEVENTHS, 4, int(num_chords))
    
    cont = input("Press Y/y to play again or any key to quit: ")
    
    if cont.upper() != 'Y':
        print()
        break