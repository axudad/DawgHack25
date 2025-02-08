import random as rand

class Information:
    def __init__(self,mood, tempo, zany, jazzy):
        self.mood = mood
        self.tempo = tempo
        self.zany = zany
        self.jazzy = jazzy

    def __init__(self):
        pass

    
    def get_jazzy(self):
        return self.jazzy
    
    def get_mood(self):
        return self.mood
    
    def get_tempo(self):
        return self.mood
    
    def get_zany(self):
        return self.zany
    
    def set_jazzy(self,jazzy):
        self.jazzy = jazzy

    def set_mood(self, mood):
        self.mood = mood

    def set_tempo(self, tempo):
        self.tempo = tempo

    def set_zany(self, zany):
        self.zany = zany


    def randomize(self):
        temp = ['Very Slow','Slow','Moderate','Fast','Very Fast']
        greek = ['Mixolydian','Dorian','Ionian','Lydian','Phrygian','Locrian','Aeolian']
        self.jazz = rand.random()
        self.mood = greek[rand.randint(0,6)]
        self.tempo = temp[rand.randint(0,4)]
        self.zane = rand.random()