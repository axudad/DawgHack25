import random

def generateChordRhythm(phraseLength):
    chordRhythmMap = []
    space = phraseLength

    while space != 0:
        beatmapDecider = random.randint(0, 100) / 101

        if beatmapDecider < 0.4 and space >= 2:
            chordRhythmMap.append(2)
            space -= 2
        elif beatmapDecider < 1 and space >= 1:
            chordRhythmMap.append(1)
            space -= 1


    return chordRhythmMap