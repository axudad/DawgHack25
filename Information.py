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
        self.chord = self.chords[chord]
        self.bass = bass
        self.lead = lead

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
        return self.mood
    
    def get_zany(self):
        return self.zany
    
    def set_bass(self,bass):
        self.bass = self.basses[bass]

    def set_chord(self,chord):
        self.chord = self.chords[chord]

    def set_jazzy(self,jazzy):
        self.jazzy = jazzy

    def set_lead(self,lead):
        self.lead = self.leads[lead]

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
        greek = ['Mixolydian','Dorian','Ionian','Lydian','Phrygian','Locrian','Aeolian']
        self.jazz = rand.random()*100
        self.mood = greek[rand.randint(0,6)]
        self.tempo = temp[rand.randint(0,4)]
        self.set_bass(basses[rand.randint(0,len(basses)-1)])
        self.set_chord(chords[rand.randint(0,len(chords)-1)])
        self.set_lead(leads[rand.randint(0,len(leads) -1)])
        self.zane = rand.random()*100