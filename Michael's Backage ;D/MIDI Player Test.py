import time
import fluidsynth

# Path to your SoundFont file
soundfont_path = "soundfont.sf2"  # Replace with the actual path to your .sf2 file
midi_file = "example.mid"  # Replace with your MIDI file

# Initialize FluidSynth
fs = fluidsynth.Synth()
fs.start(driver="alsa" if fluidsynth.system() == "Linux" else "coreaudio")  # Adjust driver if needed
sfid = fs.sfload(soundfont_path)
fs.program_select(0, sfid, 0, 0)

# Play the MIDI file
fs.midi_play(midi_file)

# Wait for playback to complete
while fs.midi_is_playing():
    time.sleep(0.1)

# Cleanup
fs.delete()