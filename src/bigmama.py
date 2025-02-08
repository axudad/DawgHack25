from midiutil import MIDIFile
import random
import pygame
import generateChordProgression

def randomFloat():
    return random.randint(1, 101) / 101

def playChord(midi, track, channel, pitches, time, duration, strum):
    currentNote = 1
    for p in pitches:
        #ADDING CHORD EXTENSIONS FOR MORE COMPLEXITY
        if (currentNote > 3):
            extensionChance = randomFloat()
            seventhChance = 0.7
            ninthChance = 0.3
            if (currentNote == 4 and extensionChance < seventhChance):
                midi.addNote(track, channel, p, time + strum * p, duration - strum * p, 75)
                pass
            elif (currentNote == 5 and extensionChance < ninthChance):
                midi.addNote(track, channel, p, time + strum * p, duration - strum * p, 70)
                pass
            else:
                pass
        else:
            pass
            midi.addNote(track, channel, p, time + strum * p, duration - strum * p, 80)
        currentNote += 1

def playBass(midi, track, channel, pitch, time, duration):
    midi.addNote(track, channel, pitch - 24, time, duration, 80)


def main(inputTempo, mood, jazziness, zaniness, chord, bass, lead):
    #SYNTH IS BEING PLAYED ON CHANNEL AND TRACK 0
    #BASS IS BEING PLAYED ON TRACK

    tempoOptions = {"Very Slow": [60, 80],
                    "Slow": [80, 100],
                    "Moderate": [100, 125],
                    "Fast": [125, 150],
                    "Very Fast": [150, 180]}

    tempo = random.randint(tempoOptions[inputTempo][0], tempoOptions[inputTempo][0])


    # Create a MIDI file with two tracks
    midi = MIDIFile(4)
    midi.addTempo(0, 0, tempo)  # Track 0, time 0, 120 BPM
    midi.addProgramChange(0, 0, 0, chord)
    #midi.addProgramChange(0, 1, 0, 37)
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

    pygame.init()
    pygame.mixer.init(channels=4)


    gmShifts = {
        "Happy" : 0,
        "Cool" : 1,
        "Dark" : 2,
        "Dreamy" : 3,
        "Funky" : 4,
        "Sad" : 5,
        "Tense" : 6
    }


    #SONG INFORMATION
    key = random.randint(43,53)
    root = key
    zanyChance = zaniness
    greekMode = gmShifts[mood]
    beat = generateChordProgression.createChordBeat(mood)
    print("BEAT: " + str(beat))

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

        sequence = generateChordProgression.generateChordProgression(beat[2], firstDegree, scale)

        for i in range (0, len(sequence)):
            root = key
            time = time + beat[0]*2 + beat[1]*2

            octaveModChance = random.randint(1, 101) / 101
            if (octaveModChance < 0.20):
                root -= 12 #DROPS an Octave
            elif (octaveModChance > 0.85):
                root += 12 #DROPS an Octave


            firstPhrase = scaleDegrees[((sequence[i] + greekMode) % 7) - 1][0]

            zanyRoll = (random.randint(1, 101) / 101) * 0.65
            if zanyRoll > zanyChance:
                playChord(midi, 1, 0, zanyScaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, beat[0]*2, 0.0)
            else:
                playChord(midi, 1, 0, scaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, beat[0]*2, 0.0)
                #playNote(1, 1, scaleDegrees[((sequence[i] + greekMode) % 7) - 1][3] - 24, time, bars)

    time = time + beat[0]*2 + beat[1]*2
    playChord(midi, 1, 0, scaleDegrees[((sequence[-1] + greekMode) % 7) - 1], time, beat[0]*5, 0)

    # Save to file
    filenumber = 19

    #with open("./chord1.mid", "wb") as output_file:
        #midi.writeFile(output_file)

    print("MIDI file 'random.mid' saved successfully.")

    midi2 = MIDIFile(4)
    midi2.addTempo(2, 0, tempo)  # Track 0, time 0, 120 BPM
    midi2.addProgramChange(2, 0, 0, bass)
    time = 0
    for i in range (0, phrases):

        for i in range (0, len(sequence)):
            root = key
            time = time + beat[0]*2 + beat[1]*2

            octaveModChance = random.randint(1, 101) / 101
            if (octaveModChance < 0.20):
                root -= 12 #DROPS an Octave
            elif (octaveModChance > 0.85):
                root += 12 #DROPS an Octave


            firstPhrase = scaleDegrees[((sequence[i] + greekMode) % 7) - 1][0]

            zanyRoll = (random.randint(1, 101) / 101) * 0.65
            if zanyRoll > zanyChance:
                playBass(midi2, 2, 0, zanyScaleDegrees[((sequence[i] + greekMode) % 7) - 1][0], time, beat[0]*2)
            else:
                playBass(midi2, 2, 0, scaleDegrees[((sequence[i] + greekMode) % 7) - 1][0], time, beat[0]*2)
                #playNote(1, 1, scaleDegrees[((sequence[i] + greekMode) % 7) - 1][3] - 24, time, bars)

    #with open("./bass1.mid", "wb") as output_file:
        #midi.writeFile(output_file)

    def play_midi():
        #pygame.mixer.music.load(r"./basicChordProgression" + str(filenumber) + ".mid")
        pygame.mixer.music.load(r"./merged_output.mid")
        pygame.mixer.music.play()

    play_midi()
    while pygame.mixer.music.get_busy():
        continue


main("Fast", "Dreamy",jazziness = 0.5, zaniness = 0.20, chord = 105, bass = 35, lead = 6)

