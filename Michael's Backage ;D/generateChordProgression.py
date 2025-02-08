import random

def generateChordProgression(length, startDegree):

    chordProgression = []

    startDistribution = {1 : 0.5,
                         2 : 0.65,
                         3 : 0.75,
                         4 : 0.82,
                         5 : 0.96,
                         6 : 0.99,
                         7 : 1}

    chordTransitionProbabilities = {
        1: {1: 0.20, 2: 0.30, 3: 0.35, 4: 0.55, 5: 0.85, 6: 0.95, 7: 1.00},
        2: {1: 0.05, 2: 0.15, 3: 0.25, 4: 0.50, 5: 0.90, 6: 0.95, 7: 1.00},
        3: {1: 0.10, 2: 0.20, 3: 0.25, 4: 0.45, 5: 0.70, 6: 0.95, 7: 1.00},
        4: {1: 0.25, 2: 0.30, 3: 0.40, 4: 0.50, 5: 0.90, 6: 0.95, 7: 1.00},
        5: {1: 0.60, 2: 0.65, 3: 0.70, 4: 0.85, 5: 0.90, 6: 0.95, 7: 1.00},
        6: {1: 0.40, 2: 0.45, 3: 0.50, 4: 0.60, 5: 0.90, 6: 0.95, 7: 1.00},
        7: {1: 0.70, 2: 0.75, 3: 0.80, 4: 0.85, 5: 0.95, 6: 1.00, 7: 1.00}
    }

    for i in range(0, length):
        decision = random.randint(0,100) / 100.1

        if i == 0 and startDegree == 0:
            for j in range(1,8):
                if decision < startDistribution[j]:
                    chordProgression.append(j)
                    break
        elif i == 0 and startDegree != 0:
            if decision < 0.33:
                chordProgression.append(startDegree)
            elif decision < 0.66:
                chordProgression.append(startDegree + 1)
            else:
                chordProgression.append((startDegree + 4) % 7+ 1)
        else :
            thisChordTransitionProbs = chordTransitionProbabilities[chordProgression[i - 1]]
            for j in range(1,8):
                if decision < thisChordTransitionProbs[j]:
                    if j == chordProgression[i - 1] and decision < 0.7:
                        chordProgression.append(j + 1)
                    else:
                        chordProgression.append(j)
                    break

    print(chordProgression)
    return chordProgression
