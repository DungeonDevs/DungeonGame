class Knight():
    def __init__(self, ID = 0, attack = 10, health = 30, healing = 3):
        self.stats = [0,0,0]
        self.stats[0] = ID
        self.stats[1] = attack
        self.stats[2] = health
        self.stats[3] = healing