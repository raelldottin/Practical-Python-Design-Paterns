from prototype_1 import Prototype
from copy import deepcopy


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"

        filename = ("{}_{}.dat".format(self.unit_type, level)).lower()

        with open(filename, "r") as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return (
            "Type: {0}\n"
            "Life: {1}\n"
            "Speed: {2}\n"
            "Attack Power: {3}\n"
            "Attack Range: {4}\n"
            "Weapon: {5}\n".format(
                self.unit_type,
                self.life,
                self.speed,
                self.attack_power,
                self.attack_range,
                self.weapon,
            )
        )

    def clone(self):
        return deepcopy(self)


class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "Archer"
        filename = ("{}_{}.dat".format(self.unit_type, level)).lower()

        with open(filename, "r") as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return (
            "Type: {0}\n"
            "Life: {1}\n"
            "Speed: {2}\n"
            "Attack Power: {3}\n"
            "Attack Range: {4}\n"
            "Weapon: {5}\n".format(
                self.unit_type,
                self.life,
                self.speed,
                self.attack_power,
                self.attack_range,
                self.weapon,
            )
        )

    def clone(self):
        return deepcopy(self)


class Barracks(object):
    def __init__(self):
        self.units = {
            "knight": {1: Knight(1), 2: Knight(2)},
            "archer": {1: Archer(1), 2: Archer(2)},
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


class Knight_Research(Prototype):
    def __init__(self, level):
        self.research_type = "Knight"

        filename = ("{}_{}.dat".format(self.research_type, level)).lower()

        with open(filename, "r") as parameter_file:
            lines = parameter_file.read().split("\n")
            self.description = lines[0]
            self.cost = lines[1]
            self.time = lines[2]

    def __str__(self):
        return (
            "Type: {0}\n"
            "Description: {1}\n"
            "Cost: {2}\n"
            "Time: {3}\n".format(
                self.research_type,
                self.description,
                self.cost,
                self.time,
            )
        )

    def clone(self):
        return deepcopy(self)


class Archer_Research(Prototype):
    def __init__(self, level):
        self.unit_type = "Archer"
        filename = ("{}_{}.dat".format(self.unit_type, level)).lower()

        with open(filename, "r") as parameter_file:
            lines = parameter_file.read().split("\n")
            self.description = lines[0]
            self.cost = lines[1]
            self.time = lines[2]

    def __str__(self):
        return (
            "Type: {0}\n"
            "Description: {1}\n"
            "Cost: {2}\n"
            "Time: {3}\n".format(
                self.research_type,
                self.description,
                self.cost,
                self.time,
            )
        )

    def clone(self):
        return deepcopy(self)


class Laboratory(object):
    def __init__(self):
        self.research_type = {
            "knight research": {1: Knight_Research(1), 2: Knight_Research(2)},
            "archer reserach": {1: Archer_Research(1), 2: Archer_Research(2)},
        }

    def start_research(self, research_type, level):
        return self.research_type[research_type][level].clone()


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 2)
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))
    laboratory = Laboratory()
    knight_research1 = laboratory.start_research("knight research", 1)
    archer_research1 = laboratory.start_research("archer research", 2)
    print("knight_research1"
