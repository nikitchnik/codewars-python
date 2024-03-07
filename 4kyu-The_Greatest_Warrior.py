class Warrior:
    def __init__(self):
        self._experience = 100
        self.achievements = []
        self.ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]


    def training(self, info):
        achieve = info[0]
        points = info[1]
        require_level = info[2]
        
        if self.level < require_level: return "Not strong enough"
        
        self._experience += points
        self.achievements.append(achieve)
        return achieve


    def battle(self, level):
        if level < 1 or level > 100: return "Invalid level"
        elif self.level // 10 != level // 10 and self.level - level <= -5: return "You've been defeated"
        
        
        elif level == self.level:
            self._experience += 10
            return "A good fight"
        elif self.level - level == 1:
            self._experience += 5
            return "A good fight"
        elif self.level < level:
            self._experience += 20 * ((level - self.level) ** 2)
            return "An intense fight"
        else:
            return "Easy fight"


    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.ranks[self.experience // 1000]

    @property
    def experience(self):
        return min(self._experience, 10000)
