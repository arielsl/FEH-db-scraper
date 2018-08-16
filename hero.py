# This class represents the hero with all its stats

class Hero:
    # Hero represents each character in the database

    def __init__(self, url_in, img_url_in):
        # All stats needed for the database
        self.url = url_in
        self.img_url = img_url_in
        self.title = None
        self.name = None
        self.hp = None
        self.attack = None
        self.speed = None
        self.defense = None
        self.resistance = None
        self.max_hp = None
        self.max_attack = None
        self.max_speed = None
        self.max_defense = None
        self.max_resistance = None
        self.bst = None
        self.weapon = None
        self.assist = None
        self.special = None
        self.skill_a = None
        self.skill_b = None
        self.skill_c = None

    def print(self):
        # Print the stats acquired to proofread
        print("Name: " + self.name)
        print("Title: " + self.title)
        print("URL: " + self.url)
        print("Image URL: " + self.img_url)
        print("HP: " + self.hp)
        print("ATK: " + self.attack)
        print("SPD: " + self.speed)
        print("DEF: " + self.defense)
        print("RES: " + self.resistance)
        print("Max HP: " + self.hp)
        print("Max ATK: " + self.attack)
        print("Max SPD: " + self.speed)
        print("Max DEF: " + self.defense)
        print("Max RES: " + self.resistance)
        print("BST: " + self.bst)
        print("Weapon: " + self.weapon)
        print("Assist: " + self.assist)
        print("Special: " + self.special)
        print("Skill A: " + self.skill_a)
        print("Skill B: " + self.skill_b)
        print("Skill C: " + self.skill_c)