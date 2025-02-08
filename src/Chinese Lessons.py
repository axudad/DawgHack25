import mido


def merge_midi(file1, file2, output_file):
    # Load both MIDI files
    midi1 = mido.MidiFile(file1)
    midi2 = mido.MidiFile(file2)

    # Create a new MIDI file for the merged output
    merged_midi = mido.MidiFile()

    # Copy tracks from both MIDI files
    for track in midi1.tracks:
        merged_midi.tracks.append(track.copy())

    for track in midi2.tracks:
        merged_midi.tracks.append(track.copy())

    # Save the merged MIDI file
    merged_midi.save(output_file)
    print(f"Merged MIDI saved as {output_file}")


if __name__ == "__main__":
    file1 = r"./chord1.mid"  # Replace with your first MIDI file
    file2 = r"./bass1.mid"  # Replace with your second MIDI file
    output_file = "merged_output.mid"  # Replace with your desired output file

    merge_midi(file1, file2, output_file)