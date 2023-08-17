from prototype_1 import Prototype
from copy import deepcopy

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"
        
        filename = "{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter