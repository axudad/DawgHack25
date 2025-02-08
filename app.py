import random as rnd

import streamlit as st

class Information:
    def __init__(self):
        self.mood = "Happy"
        self.tempo = "Normal"
        self.jazzy = 50
        self.zany = 50
info = Information()
# Title of the app
st.title('Bach')

# A simple message
st.write('Create music with little effort . . . no AI')

# Tempo Drop
# st.selectbox( label , inputs)
tempos = ["Normal","Very Fast","Fast","Slow","Very Slow"]
info.tempo = st.selectbox( 'Tempo', tempos)

# Tempo Drop
# st.selectbox( label , inputs)
moods = ["Happy","Cool","Dark","Dreamy","Funky","sad","Tense"]
info.mood = st.selectbox( 'Mood', moods)

# Jazz slider
info.jazzy = st.slider('Jazz')

# Zane Slider
info.zany = st.slider('Zane')

# Random
if st.button("Randomize"):

# Download
st.button("Create!")
