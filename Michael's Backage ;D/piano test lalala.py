from midiutil import MIDIFile

# Create a MIDI file with one track
midi = MIDIFile(1)
midi.addTempo(0, 0, 120)  # Track 0, time 0, 120 BPM

# Add a note: track, channel, pitch, start_time, duration, volume
midi.addNote(0, 0, 60, 0, 1, 100)  # Middle C

# Save to file
with open("midiutil_example.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDI file 'midiutil_example.mid' saved successfully.")