from "Characters" import CharacterInfo

class ChoosePath():
    def __init__(self):
        self.player_name = input("What is your name?")
        self.player_health = 100
        self.player_type = input("What type ")

    def getPlayerStats(self):
        player_stats = [self.player_name, self.player_health, self.player_type]
        return self.player_name

test = CharacterInfo()
test.printGoliathInfo()