import streamlit as st
from Information import Information
from src import bigmama


info = Information()
message = st.empty()

c_logo = st.container()
c_title = st.container()
c_values = st.container()
c_inst = st.container()
c_buttons = st.container()
c_logo.image("Recources/Bach.png", width = 200)

# Title of the app
c_title.title(':blue[Bach]')

# A message
c_title.write('Create music with little effort . . . no AI')
c_title.write('Enter parameters below and press create!')

# Tempo Drop
# st.selectbox( label , inputs , index )
tempos = ["Very Fast","Fast","Moderate","Slow","Very Slow"]
tempo = c_values.selectbox( 'Tempo', tempos , 2)
info.set_tempo(tempos[2])

# Moods Drop
# st.selectbox( label , inputs)
moods = ["Happy","Cool","Dark","Dreamy","Funky","Sad","Tense"]
mood = c_values.selectbox( 'Mood', moods , 0)
info.set_mood(moods[0])

# Chords Drop
# st.selectbox( label , inputs)
chords_ = ["Drawbar Organ","Electric Piano","Fantasia","Skakuhachi","Ocarina","Halo"]
chord = c_inst.selectbox( 'Chord', chords_ , 0)
info.set_chord_string(chords_[0])

# Bass Drop
# st.selectbox( label , inputs)
basses_ = ['Synth Bass',"Baratone Sax","Synth Bass 2","Fretless Bass"]
bass = c_inst.selectbox( 'Bass', basses_ , 0)
info.set_bass_string(basses_[0])

# leads Drop
# st.selectbox( label , inputs)
leads_ = ["Solo Vox","Piano","Marimba","Strings","Violin"]
lead = c_inst.selectbox( 'Lead', leads_ , 0)
info.set_lead_string(leads_[0])

# Jazz slider
jazz = c_values.slider('Jazz')
info.set_jazzy(0)

# Zane Slider
zany = c_values.slider('Zany')
info.set_zany(0)

#enable file buttons
if 'button_enabled' not in st.session_state:
    st.session_state.button_enabled = False

# Random
if c_buttons.button("Randomize"):
    info.randomize()
    message.success("Random With: " + info.get_tempo() + ', ' + info.get_mood() + ", " + str(info.get_jazzy()) + ", " + str(info.get_zany())+ ", " + str(info.get_chord_string()) + ", " + info.get_bass_string()+ ", " + str(info.get_lead_string()))
    st.session_state.button_enabled = True

# Create Midi Button
if c_buttons.button("Create"):
    info.set_jazzy(jazz)
    info.set_zany(zany)
    info.set_tempo(tempo)
    info.set_mood(mood)
    message.success("Created With: " + info.get_tempo() + ', ' + info.get_mood() + ", " + str(info.get_jazzy()) + ", " + str(info.get_zany())+ ", " + str(info.get_chord_string()) + ", " + str(info.get_bass_string())+ ", " + str(info.get_lead_string()))
    st.session_state.button_enabled = True

def create():
    bigmama.main(info.get_tempo(), info.get_mood(), jazziness = info.get_jazzy() , zaniness = info.get_zany(), chord = info.get_chord_int(), bass = info.get_bass_int(), lead = info.get_bass_int())

# play and Download buttons
if st.session_state.button_enabled:
    if c_buttons.button('Play',):
        create()
        message.success("play")

    if c_buttons.download_button('Download',"Michael's Backage ;D/MIDIS/basicChordProgression.mid",):
        create()
        message.success("Down")

