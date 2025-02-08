import random as rand

class Information:

    basses = {'Synth Bass': 38,"Baratone Sax":67,"Synth Bass 2":87,"Fretless Bass":35}
    chords = {"Drawbar Organ":17,"Electric Piano":6,"Fantasia":89,"Skakuhachi":78,"Ocarina":79,"Halo":94}
    leads = {"Solo Vox":85,"Piano":1,"Marimba":12,"Strings":45,"Violin":40}

    def __init__(self,mood, tempo, zany, jazzy, chord, bass, lead):
        
        self.mood = mood
        self.tempo = tempo
        self.zany = zany
        self.jazzy = jazzy
        self.chord_int = self.chords[chord]
        self.chord_string = chord
        self.bass_int = self.basses[bass]
        self.bass_string = bass
        self.lead_int = self.leads[lead]
        self.lead_string = lead
        

    def __init__(self):
        pass

    def get_bass(self):
        return self.bass
    
    def get_chord(self):
        return self.chord
    
    def get_jazzy(self):
        return self.jazzy
    
    def get_lead(self):
        return self.lead
    
    def get_mood(self):
        return self.mood
    
    def get_tempo(self):
        return self.tempo
    
    def get_zany(self):
        return self.zany
    
    def set_bass_int(self,bass):
        self.bass_int = self.basses[bass]

    def set_bass_string(self,bass):
        self.bass_string = bass

    def set_chord_int(self,chord):
        self.chord_int = self.chords[chord]

    def set_chord_string(self,chord):
        self.chord_string = chord

    def set_jazzy(self,jazzy):
        self.jazzy = jazzy

    def set_lead_int(self,lead):
        self.lead_int = self.leads[lead]

    def set_lead_string(self, lead):
        self.lead_string = lead

    def set_mood(self, mood):
        self.mood = mood

    def set_tempo(self, tempo):
        self.tempo = tempo

    def set_zany(self, zany):
        self.zany = zany


    def randomize(self):
        basses = ['Synth Bass',"Baratone Sax","Synth Bass 2","Fretless Bass"]
        chords = ["Drawbar Organ","Electric Piano","Fantasia","Skakuhachi","Ocarina","Halo"]
        leads = ["Solo Vox","Piano","Marimba","Strings","Violin"]

        temp = ['Very Slow','Slow','Moderate','Fast','Very Fast']
        moods = ['Happy','Cool','Dark','Funky','Dreamy','Sad','Tense']
        self.jazzy = round(rand.random()*100)
        self.mood = moods[rand.randint(0,6)]
        self.tempo = temp[rand.randint(0,4)]
        self.set_bass(basses[rand.randint(0,len(basses)-1)])
        self.set_chord(chords[rand.randint(0,len(chords)-1)])
        self.set_lead(leads[rand.randint(0,len(leads) -1)])
        self.zany = round(rand.random()*100)