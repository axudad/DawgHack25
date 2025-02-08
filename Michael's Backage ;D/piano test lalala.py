from midiutil import MIDIFile

def playMajorChord(root_pitch, time, duration):
    midi.addNote(0, 0, root_pitch, time, duration, 100)
    midi.addNote(0, 0, root_pitch + 4, time, duration, 100)
    midi.addNote(0, 0, root_pitch + 7, time, duration, 100)

def playMinorChord(root_pitch, time, duration):
    midi.addNote(0, 0, root_pitch, time, duration, 100)
    midi.addNote(0, 0, root_pitch + 3, time, duration, 100)
    midi.addNote(0, 0, root_pitch + 7, time, duration, 100)

def playDiminChord(root_pitch, time, duration):
    midi.addNote(0, 0, root_pitch, time, duration, 100)
    midi.addNote(0, 0, root_pitch + 3, time, duration, 100)
    midi.addNote(0, 0, root_pitch + 6, time, duration, 100)

# Create a MIDI file with one track
midi = MIDIFile(1)
midi.addTempo(0, 0, 170)  # Track 0, time 0, 120 BPM

# Add a note: track, channel, pitch, start_time, duration, volume
pitch = 60
time = 0

playMajorChord(60, 1, 2)
playMinorChord(62, 3, 2)
playMinorChord(64, 5, 2)
playMajorChord(65, 7, 2)
playMajorChord(67, 9, 2)
playMinorChord(69, 11, 2)
playMinorChord(71, 13, 2)

# Save to file
with open("chordScales.mid", "wb") as output_file:
    midi.writeFile(output_file)



print("MIDI file 'midiutil_example.mid' saved successfully.")