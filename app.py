import streamlit as st

# Title of the app
st.title('Bach')

# A simple message
st.write('Create music with little effort . . . no AI')

# Mood Toggle
st.toggle('Mood')

# Tempo Drop
# st.selectbox( label , inputs)
st.selectbox( 'Tempo', ["Happy","Cool","Dark","Dreamy","Funky","sad","Tense"])

# Jazz slider
st.slider('Jazz')

# Zane Slider
st.slider('Zane')

# Random
st.button("Randomize")

# Download
st.button("Create!")