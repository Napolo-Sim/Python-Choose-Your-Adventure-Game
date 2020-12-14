#Initialize all Character Types in Dictionaries
Goliath = {
    "type": "Goliath",
    "health": 250,
    "attack": 150,
    "defense": 200,
    "speed": 50,
    "description": "They're huge. They hit hard, don't feel pain often and are slow. Nothing is going to stop them from\n"
                   "where they wanna go, even though they might show up very very late."
}
Imp = {
    "type": "Imp",
    "health": 50,
    "attack": 100,
    "defense": 50,
    "speed": 250,
    "description": "A speedy one. Though attack and defense, health, lifespan, toe length, facial structure,\n"
                   "and everything you could imagine are lackluster, his speed makes up for his many flaws. You know, I\n"
                   "heard imps are quite good at marathons."
}
Dark_Elf = {
    "type": "Dark Elf",
    "health": 100,
    "attack": 100,
    "defense": 100,
    "speed": 150,
    "description": "These elfs are creepy. They have the ability to tap into dark magic and revive the undead\n"
                   "to help assist them in their travels. But don't even get me started on their cultural acceptance of\n"
                   "necrophilia. *Throws Up*"
}
Holy_Knight = {
    "type": "Holy Knight",
    "health": 150,
    "attack": 150,
    "defense": 150,
    "speed": 100,
    "description": "Ah yes! Time to Bless Up! The most divine of the characters, our Holy Knights! Known for their\n"
                   "balance in all stats, these knights hold themselves well in all scenarios. YOU would have to mess up\n"
                   "in order for them to die."
}
Human = {
    "type": "Human",
    "health": 100,
    "attack": 50,
    "defense": 100,
    "speed": 100,
    "description": "Seriously. A human. You already play this character outside of this game. C'mon, choose a different\n"
                   "character. Their stats aren't even good either."
}
types = [Goliath, Imp, Dark_Elf, Holy_Knight, Human]

# Class for Game File to print character info
class CharacterInfo():
    def __init__(self):
        print("Welcome to the Game!")

    def printGoliathInfo(self):
        print("Type:", types[0]["type"])
        print("Health:", types[0]["health"])
        print("Attack:", types[0]["attack"])
        print("Defense:", types[0]["defense"])
        print("Speed:", types[0]["speed"])
        print("Description:", types[0]["description"], "\n")

    def printImpInfo(self):
        print("Type:", types[1]["type"])
        print("Health:", types[1]["health"])
        print("Attack:", types[1]["attack"])
        print("Defense:", types[1]["defense"])
        print("Speed:", types[1]["speed"])
        print("Description:", types[1]["description"], "\n")

    def printDarkElfInfo(self):
        print("Type:", types[2]["type"])
        print("Health:", types[2]["health"])
        print("Attack:", types[2]["attack"])
        print("Defense:", types[2]["defense"])
        print("Speed:", types[2]["speed"])
        print("Description:", types[2]["description"], "\n")

    def printHolyKnightInfo(self):
        print("Type:", types[3]["type"])
        print("Health:", types[3]["health"])
        print("Attack:", types[3]["attack"])
        print("Defense:", types[3]["defense"])
        print("Speed:", types[3]["speed"])
        print("Description:", types[3]["description"], "\n")

    def printGoliathInfo(self):
        print("Type:", types[4]["type"])
        print("Health:", types[4]["health"])
        print("Attack:", types[4]["attack"])
        print("Defense:", types[4]["defense"])
        print("Speed:", types[4]["speed"])
        print("Description:", types[4]["description"], "\n")