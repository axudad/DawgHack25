import streamlit as st
from Information import Information


info = Information()

message = st.empty()

# Title of the app
st.title('Bach')

# A simple message
st.write('Create music with little effort . . . no AI')

# Tempo Drop
# st.selectbox( label , inputs , index )
tempos = ["Very Fast","Fast","Moderate","Slow","Very Slow"]
tempo = st.selectbox( 'Tempo', tempos , 2)
info.set_tempo(tempos[2])

# Tempo Drop
# st.selectbox( label , inputs)
moods = ["Happy","Cool","Dark","Dreamy","Funky","Sad","Tense"]
mood = st.selectbox( 'Mood', moods , 0)
info.set_mood(moods[0])

# Jazz slider
jazz = st.slider('Jazz')

# Zane Slider
zany = st.slider('Zany')

# Random


if st.button("Randomize"):
    info.randomize()
    message.success("Random With: " + info.get_tempo() + ', ' + info.get_mood() + ", " + str(info.get_jazzy()) + ", " + str(info.get_zany()))



# Download
if st.button("Create!"):
    info.set_jazzy(jazz)
    info.set_zany(zany)
    info.set_tempo(tempo)
    info.set_mood(mood)
    message.success("Created With: " + info.get_tempo() + ', ' + info.get_mood() + ", " + str(info.get_jazzy()) + ", " + str(info.get_zany()))
