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
#Prints all of the types and stats respectively
for i in range(0, len(types)):
    print("Type:", types[i]["type"])
    print("Health:", types[i]["health"])
    print("Attack:", types[i]["attack"])
    print("Defense:", types[i]["defense"])
    print("Speed:", types[i]["speed"])
    print("Description:", types[i]["description"], "\n")




