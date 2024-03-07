class Warrior:
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.require_experience = 200
        self.rank = 'Pushover'
        self.achievements = []
        
        self.ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        
    def training(self, info):
        achieve = info[0]
        points = info[1]
        require_level = info[2]
        
        if self.level < require_level:
            return "Not strong enough"
        
        self.experience += points
        self.achievements.append(achieve)
        self.up_level()
        return achieve
    
    def battle(self, level):
        if level < 1 or level > 100:
            return "Invalid level"
        
        enemy_rank = self.ranks[level // 10]
        
        if self.ranks.index(self.rank) < self.ranks.index(enemy_rank) and level - self.level > 5:
            return "You've been defeated"
        
        
        if level == self.level:
            points = 10
            self.experience += points
            self.up_level()
            return "A good fight"
            
        elif self.level - level == 1:
            points = 5
            self.experience += points
            self.up_level()
            return "A good fight"
        
        elif self.level - level <= 2:
            points = 0
            return "An intense fight"
            
        elif level - self.level >= 2:
            points = 20 * (level - self.level) ** 2
            if points == 0:
                points = 20
            self.experience += points
            self.up_level()
            return "Easy fight"
        
        
    
    def up_level(self):
        while self.experience >= self.require_experience:
            self.require_experience += 100
            
            self.level += 1
            self.rank = self.ranks[self.level // 10]
            if self.level >= 100:
                self.level = 100
                break
