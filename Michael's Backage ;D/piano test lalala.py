from midiutil import MIDIFile
import random

def playChord(pitches, time, duration):
    for p in pitches:
        midi.addNote(0, 0, p, time, duration, 100)


# Create a MIDI file with one track
midi = MIDIFile(1)
midi.addTempo(0, 0, 110)  # Track 0, time 0, 120 BPM

keyRootsToPitch = {"C" : 49,
                   "Db" : 50,
                   "D" : 51,
                   "Eb" : 52,
                   "F" : 53,
                   "Gb" : 54,
                   "G" : 55,
                   "Ab" : 56,
                   "A" : 57,
                   "Bb" : 58,
                   "Bb" : 59}

gmShifts = {
    "Happy" : 0,
    "Cool" : 1,
    "Dark" : 2,
    "Dreamy" : 3,
    "Funky" : 4,
    "Sad" : 5,
    "Tense" : 6
}
greekMode = gmShifts["Sad"]

#SONG INFORMATION
key = random.randint(43,53)

root = key

scaleDegrees = [[root, root + 4, root + 7], #1 TONIC
                [root + 2, root + 4, root + 7], #2 SUPERTONIC
                [root + 4, root + 7, root + 11], #3 MEDIANT
                [root + 5, root + 9, root + 12], #4 SUBDOMINANT
                [root + 7, root + 11, root + 14], #5 DOMINANT
                [root + 9, root + 12, root + 16], #6 SUBMEDIANT
                [root + 11, root + 14, root + 17]] #7 LEADING TONE

# Add a note: track, channel, pitch, start_time, duration, volume
duration = 3
time = -duration
sequence = [random.randint(1, 8),
            random.randint(1, 8),
            random.randint(1, 8),
            random.randint(1, 8)]

chord_amounts = len(sequence)

for i in range (0, chord_amounts):
    time = time + duration

    playChord(scaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, duration)


# Save to file
filenumber = 0
with open("basicChordProgression.mid", "wb") as output_file:
    midi.writeFile(output_file)



print("MIDI file 'random.mid' saved successfully.")