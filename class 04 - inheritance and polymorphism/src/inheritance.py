class Prophet:
    def speak(self):
        return "Hear the word of God!"

class Moses(Prophet):
    def speak(self):
        return "Let my people go!"

class Elijah(Prophet):
    def speak(self):
        return "Fire from heaven!"

prophets = [Moses(), Elijah()]
for p in prophets:
    print(p.speak())