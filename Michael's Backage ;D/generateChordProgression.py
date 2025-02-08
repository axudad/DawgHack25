import random

def generateChordProgression(length, startDegree, scale):
    chordProgression = []

    majStartDistribution = {1 : 0.5,
                         2 : 0.65,
                         3 : 0.75,
                         4 : 0.82,
                         5 : 0.96,
                         6 : 0.99,
                         7 : 1}

    majChordTransitionProbabilities = {
        1: {1: 0.20, 2: 0.30, 3: 0.35, 4: 0.55, 5: 0.85, 6: 0.95, 7: 1.00},
        2: {1: 0.05, 2: 0.15, 3: 0.25, 4: 0.50, 5: 0.90, 6: 0.95, 7: 1.00},
        3: {1: 0.10, 2: 0.20, 3: 0.25, 4: 0.45, 5: 0.70, 6: 0.95, 7: 1.00},
        4: {1: 0.25, 2: 0.30, 3: 0.40, 4: 0.50, 5: 0.90, 6: 0.95, 7: 1.00},
        5: {1: 0.60, 2: 0.65, 3: 0.70, 4: 0.85, 5: 0.90, 6: 0.95, 7: 1.00},
        6: {1: 0.40, 2: 0.45, 3: 0.50, 4: 0.60, 5: 0.90, 6: 0.95, 7: 1.00},
        7: {1: 0.70, 2: 0.75, 3: 0.80, 4: 0.85, 5: 0.95, 6: 1.00, 7: 1.00}
    }

    minStartDistribution = {
        1: 0.55,
        2: 0.56,
        3: 0.68,
        4: 0.76,
        5: 0.94,
        6: 0.98,
        7: 1
    }

    minChordTransitionProbabilities = {
    1: {1: 0.15, 2: 0.25, 3: 0.45, 4: 0.55, 5: 0.80, 6: 0.90, 7: 1.00},
    2: {1: 0.20, 2: 0.30, 3: 0.45, 4: 0.70, 5: 0.80, 6: 0.95, 7: 1.00},
    3: {1: 0.30, 2: 0.40, 3: 0.55, 4: 0.65, 5: 0.85, 6: 0.95, 7: 1.00},
    4: {1: 0.25, 2: 0.35, 3: 0.50, 4: 0.60, 5: 0.85, 6: 0.95, 7: 1.00},
    5: {1: 0.40, 2: 0.45, 3: 0.55, 4: 0.70, 5: 0.80, 6: 0.90, 7: 1.00},
    6: {1: 0.20, 2: 0.35, 3: 0.45, 4: 0.60, 5: 0.80, 6: 0.90, 7: 1.00},
    7: {1: 0.35, 2: 0.40, 3: 0.55, 4: 0.65, 5: 0.85, 6: 0.95, 7: 1.00}
    }

    if scale == "major":
        startDistribution = majStartDistribution
        chordTransitionProbabilities = majChordTransitionProbabilities
    else:
        startDistribution = minStartDistribution
        chordTransitionProbabilities = minChordTransitionProbabilities

    for i in range(0, length):
        decision = random.randint(0,100) / 100.1

        if i == 0 and startDegree == 0:
            for j in range(1,8):
                if decision < startDistribution[j]:
                    chordProgression.append(j)
                    break
        elif i == 0 and startDegree != 0:
            if decision < 0.5:
                chordProgression.append(startDegree)
            elif decision < 0.75:
                chordProgression.append(startDegree + 1)
            else:
                chordProgression.append((startDegree + 3) % 7+ 1)
        else :
            thisChordTransitionProbs = chordTransitionProbabilities[chordProgression[i - 1]]
            for j in range(1,8):
                if decision < thisChordTransitionProbs[j]:
                    if j == chordProgression[i - 1] and decision < 0.6:
                        chordProgression.append(j + 1)
                    else:
                        chordProgression.append(j)
                    break

    print(chordProgression)
    return chordProgression

def createChordBeat(emotion):
    #[length of each chord, Pause, amount of multiplication]
    beatArray = [[0.125, 0.125, 8], #Stutter/EightNotes
                 [3, 1, 4], #Full Notes Per Measure
                 [0.5, 0.5, 4], #Offbeat
                 [2, 0, 2],  # Long and Sustained
                 [4, 0, 1],  # One Long Ambient Chord
                 [1.5, 0.5, 2],  # Three Halves
                 [1, 1, 2],  # Offset Whole
    ]
    emotionalAttribution = {"Happy" : beatArray[5],
                            "Cool" : beatArray[0],
                            "Dark" : beatArray[4],
                            "Dreamy" : beatArray[6],
                            "Funky" : beatArray[2],
                            "Sad" : beatArray[1],
                            "Tense" : beatArray[3]}

    return emotionalAttribution[emotion]
