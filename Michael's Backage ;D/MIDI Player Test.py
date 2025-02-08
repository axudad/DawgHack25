import time
import fluidsynth

# Path to your SoundFont file
soundfont_path = r"./nintendo_soundfont.sf2"  # Replace with the actual path to your .sf2 file
midi_file = r"MIDIS/basicChordProgression13.mid"  # Replace with your MIDI file

# Initialize FluidSynth
fs = fluidsynth.Synth()
fs.start(driver='waveout', midi_driver= 'winmidi')  # Adjust driver if needed
sfid = fs.sfload(soundfont_path)
fs.program_select(0, sfid, 0, 0)

# Play the MIDI file
fs.play_midi_file(midi_file)

