from midiutil import MIDIFile
import random
import generateChordProgression
import pygame

# Initialize pygame mixer
pygame.init()


def play_midi():
    pygame.mixer.init(channels=4)
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()

def randomFloat():
    return random.randint(1, 101) / 101


def playChord(track, channel, pitches, time, duration):
    currentNote = 1
    midi.addNote(track, channel, pitches[3] - 24, time, duration, 90)
    for p in pitches:
        #ADDING CHORD EXTENSIONS FOR MORE COMPLEXITY
        if (currentNote > 3):
            extensionChance = randomFloat()
            seventhChance = 0.7
            ninthChance = 0.3
            if (currentNote == 4 and extensionChance < seventhChance):
                midi.addNote(track, channel, p, time + 0.02 * p, duration - 0.02 * p, 90)
            elif (currentNote == 5 and extensionChance < ninthChance):
                midi.addNote(track, channel, p, time + 0.02 * p, duration - 0.02 * p, 80)
            else:
                pass
        else:
            midi.addNote(track, channel, p, time + 0.02 * p, duration - 0.02 * p, 100)
        currentNote += 1

def playNote(track, channel, pitch, time, duration):
    midi.addNote(track, channel, pitch, time, duration, 90)


#SYNTH IS BEING PLAYED ON CHANNEL AND TRACK 0
#BASS IS BEING PLAYED ON TRACK

# Create a MIDI file with two tracks
midi = MIDIFile(2)
midi.addTempo(0, 0, 140)  # Track 0, time 0, 120 BPM
midi.addTempo(1, 0, 140)  # Track 1, time 0, 120 BPM
midi.addProgramChange(0, 0, 0, 95)
midi.addProgramChange(1, 1, 0, 37)
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
greekMode = gmShifts["Tense"]

#SONG INFORMATION
key = random.randint(43,53)
root = key
zanyChance = 0.53

happyScaleDegrees = [[root, root + 4, root + 7, root + 11, root + 14], #1 TONIC
                    [root + 2, root + 5, root + 9, root + 12, root + 16], #2 SUPERTONIC
                    [root + 4, root + 7, root + 11, root + 14, root + 17], #3 MEDIANT
                    [root + 5, root + 9, root + 12, root + 16, root + 19], #4 SUBDOMINANT
                    [root + 7, root + 11, root + 14, root + 17, root + 21], #5 DOMINANT
                    [root + 9, root + 12, root + 16, root + 19, root + 23], #6 SUBMEDIANT
                    [root + 11, root + 14, root + 17, root + 21, root + 24]] #7 LEADING TONE

zanyScaleDegrees = [[root, root + 4, root + 7, root + 11, root + 14], #1 TONIC
                    [root + 2, root + 5, root + 8, root + 12, root + 16], #2 SUPERTONIC
                    [root + 4, root + 6, root + 11, root + 13, root + 17], #3 MEDIANT
                    [root + 6, root + 9, root + 12, root + 16, root + 19], #4 SUBDOMINANT
                    [root + 7, root + 11, root + 14, root + 17, root + 21], #5 DOMINANT
                    [root + 8, root + 12, root + 16, root + 19, root + 23], #6 SUBMEDIANT
                    [root + 11, root + 14, root + 17, root + 22, root + 24]] #7 LEADING TONE

sadScaleDegrees = [[root, root + 3, root + 7, root + 10, root + 14], #1 TONIC
                    [root + 2, root + 5, root + 8, root + 12, root + 15], #2 SUPERTONIC
                    [root + 3, root + 7, root + 10, root + 14, root + 17], #3 MEDIANT
                    [root + 5, root + 8, root + 12, root + 15, root + 19], #4 SUBDOMINANT
                    [root + 7, root + 10, root + 14, root + 17, root + 20], #5 DOMINANT
                    [root + 8, root + 12, root + 15, root + 19, root + 22], #6 SUBMEDIANT
                    [root + 10, root + 14, root + 17, root + 20, root + 24]] #7 LEADING TONE

if (greekMode == 0 or greekMode == 3 or greekMode == 4):
    scaleDegrees = happyScaleDegrees
    scale = "major"
else:
    scaleDegrees = sadScaleDegrees
    scale = "minor"

phrases = 4
bars = 4
firstDegree = 0
time = 0
for i in range (0, phrases):

    sequence = generateChordProgression.generateChordProgression(4,firstDegree, scale)

    for i in range (0, len(sequence)):
        root = key
        time = time + bars

        octaveModChance = random.randint(1, 101) / 101
        if (octaveModChance < 0.20):
            root -= 12 #DROPS an Octave
        elif (octaveModChance > 0.85):
            root += 12 #DROPS an Octave


        firstPhrase = happyScaleDegrees[((sequence[i] + greekMode) % 7) - 1][0]

        zanyRoll = (random.randint(1, 101) / 101) * 0.65
        if zanyRoll > zanyChance:
            playChord(0, 0, zanyScaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, bars)
        else:
            playChord(0, 0, happyScaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, bars)
            #playNote(1, 1, scaleDegrees[((sequence[i] + greekMode) % 7) - 1][3] - 24, time, duration)


# Save to file
filenumber = 16

# with open("basicChordProgression" + str(filenumber) + ".mid", "wb") as output_file:
    # midi.writeFile(output_file)

print("MIDI file 'random.mid' saved successfully.")

# Load and play MIDI file using FluidSynth
midi_file = r"./basicChordProgression" + str(filenumber) + ".mid"

# Start MIDI playback
play_midi()


# Keep running while music is playing
while pygame.mixer.music.get_busy():
    continue
