Note Taking Criteria
    Class
        Ask: Who or what is performing the action?
    Problem
        Ask: What happens to the data when the Actor touches it?
    Constraint
        Ask: Where does the logic break or change?
    Inverse
        Ask: If I do this, how do I undo it?

    What to Igore
        The "Why": Author's opinion
        The "Context": Historical filler
        The "Bridge" Instructional transition

Book: Practical Python Design Patterns: Pythonic Solutions to Common Problems Wessel Badenhorst

Class: 
Problem: 
Constraint: 
Inverse: 

Class:
Problem:
Constraint:

	Class:
    Problem:

		Method:
        Problem:

		Method:
        Probem:

		Method:
        Problem:
        Constraint:

		Method:
        Problem:

Filename: rts-simple.py

Problem:Creates a barracks and stables object, uses barracks to generate a warrior, archer, spearman, crossbowman objects, passes those objects individually as a string to print() displaying the stats of the objects, uses stables to generate a horseman and knight objects, passes those objects individually as a string to print() displaying the stats of the objects.
Constraint: The script only runs if its executed not if its imported

    Class: Warrior
    Problem: parameters object is used to define a Warrior class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variables using the self parameter when the object is created

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Archer
    Problem: parameters object is used to define a Archer class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variables using the self parameter when the object is created

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Spearman
    Problem: parameters object is used to define a Spearman class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variables using the self parameter when the object is created

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat


    Class: Crossbowman
    Problem: parameters object is used to define a Crossbowman class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variables using the self parameter when the object is created

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Barracks
    Problem: parameters object is used to define a Barracks class

        Method: generate-warrior
        Problem: parameters self to return an object to a Warrior class
        Constraint: 100, 1, 1, 1, "wooden sword" are used as parameters to crearte a Warrior object

        Method: generate-archer
        Problem: parameters self to return an object to a Archer class
        Constraint: 100, 1, 1, 2, "short bow" are used as parameters to create an Archer object

        Method: generate-spearman
        Problem: parameters self to return an object to a Spearman class
        Constraint: 600, 1, 2, 1, "spear" are used as parameters to create a Spearman object

        Method: generate-crossbowman
        Problem: parameters self to return an object to a Crossbowman class
        Constraint: 400, 1, 3, 2, "long bow" are used as parameters to create a Crossbowman object

    Class: Horseman
    Problem: parameters object is used to define a Horseman class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variables using the self parameter when the object is created

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Knight
    Problem: parameters object is used to define a Knight class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variable susing the self parameter when the object is created

     Class: Stables
     Problem: parameter object is used to define a Stables class

         Method: generate-knight
         Problem: parameters self to return an object to a Knight class
         Constraint: Knight properties are hardcoded as 400, 4, 3, 1, "long sword" are used as parameters to create a Knight

         Method: generate-horseman
         Problem: parameters self to return an object to a Horseman class
         Constraint: 200, 4, 2, 1, "short sword" are used as parameters to create a Horseman object


Filename rts-multi-unit.py


Problem: Creates a barracks and stables object, creates each unit using lowercase of the unit class name and 1 or 2 as the level, subsequently passes those objects individually as a string to print() displaying the stats of the objects
Constraint: The script only runs if its executed not if its imported

    Class: Warrior
    Problem: parameters object is used to define a Warrior class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Warrior" and uses if-else statements to set class variables life, speed, attack_power, attack_range, weapon to 100, 1, 1, 1, "wooden sword" for a level 1 unit, and 200, 1, 2, 1, "wooden sword" for a level 2 unit 

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

     Class: Archer
     Problem: parameters object is used to define a Archer class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Archer" and uses if-else statements to set class variables life, speed, attack_power, attack_range, weapon to 100, 1, 1, 2, "short bow" for a level 1 unit, and 200, 1, 2, 2, "short bow" for a level 2 unit 


        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type

    Class: Spearman
    Problem: parameters object is used to define a Spearman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Spearman" and uses if-else statements to set class variables life, speed, attack_power, attack_range, weapon to 600, 1, 2, 1, "spear" for a level 1 unit, and 1200, 1, 4, 1, "spear" for a level 2 unit 

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

     Class: Crossbowman
     Problem: parameters object is used to define a Crossbowman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Crossbowman" and uses if-else statements to set class variables life, speed, attack_power, attack_range, weapon to 100, 1, 1, 2, "long bow" for a level 1 unit, and 200, 1, 2, 2, "long bow" for a level 2 unit 

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Barracks
    Problem: parameter object is used to define a Barracks class

        Method: build_unit()
        Problem: parameters self, unit_type, and level are used to return a Warrior | Archer | Spearman | Crossbow object
        Constraint: unity_type must be set the respective class name in lowercase and level number between 1 and 2 must be specified. using if-else statement checks the unit_type and uses the level parameter to create the requested object

    Class: Horseman
    Problem: parameters object is used to define a Horseman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Horseman" and uses if-else statements to set class variables life, speed, attack_power, attack_range, weapon to 200, 4, 2, 1, "short sword" for a level 1 unit, and 400, 4, 4, 1, "short sword" for a level 2 unit 

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Knight
    Problem: parameters object is used to define a Knight class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Knight" and uses if-else statements to set class variables life, speed, attack_power, attack_range, weapon to 400, 4, 3, 1, "long sword" for a level 1 unit, and 800, 4, 6, 1, "long sword" for a level 2 unit 

    Class: Stables
    Problem: parameter object is used to define a Stables class

        Method: build_unit()
        Problem: parameters self, unit_type, and level are used to create a Horseman | Knight object
        Constraint: unity_type must be set the respective class name in lowercase and level number between 1 and 2 must be specified. using if-else statement checks the unit_type and uses the level parameter to create the requested object

Filename: warrior-1.dat
    Problem: Stores stats of a unit
    Constraint: life, speed, attack_power, atack_range, weapon is seperated by a newline

Filename: archer-1.dat
    Problem: Stores stats of a unit
    Constraint: life, speed, attack_power, atack_range, weapon is seperated by a newline

Filename: spearman-1.dat
    Problem: Stores stats of a unit
    Constraint: life, speed, attack_power, atack_range, weapon is seperated by a newline

Filename: crossbowman-1.dat
    Problem: Stores stats of a unit
    Constraint: life, speed, attack_power, atack_range, weapon is seperated by a newline

Filename: horseman-1.dat
    Problem: Stores stats of a unit
    Constraint: life, speed, attack_power, atack_range, weapon is seperated by a newline

Filename: knight-1.dat
    Problem: Stores stats of a unit
    Constraint: life, speed, attack_power, atack_range, weapon is seperated by a newline

Filename: rts_file_based.py
Problem: Creates a barracks and stables object, creates each unit using lowercase of the unit class name and 1 or 2 as the level, subsequently pass those objects individually as a string to print() displaying the stats of the objects
Constraint: The script only runs if its executed not if its imported

    Class: Warrior
    Problem: parameters object is used to define a Warrior class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Warrior", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

     Class: Archer
     Problem: parameters object is used to define a Archer class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Archer", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file


        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Spearman
    Problem: parameters object is used to define a Spearman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Spearman", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

     Class: Crossbowman
     Problem: parameters object is used to define a Crossbowman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Crossbowman", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Barracks
    Problem: parameter object is used to define a Barracks class

        Method: build_unit()
        Problem: parameters self, unit_type, and level are used to return a Warrior | Archer | Spearman | Crossbow object
        Constraint: unity_type must be set the respective class name in lowercase and level number between 1 and 2 must be specified. using if-else statement checks the unit_type and uses the level parameter to create the requested object

    Class: Horseman
    Problem: parameters object is used to define a Horseman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Horseman", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Knight
    Problem: parameters object is used to define a Knight class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Knight", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

    Class: Stables
    Problem: parameter object is used to define a Stables class

        Method: build_unit()
        Problem: parameters self, unit_type, and level are used to return a Horseman | Knight object
        Constraint: unity_type must be set the respective class name in lowercase and level number between 1 and 2 must be specified. using if-else statement checks the unit_type and uses the level parameter to create the requested object

Class: Prototype Pattern
Problem: creates a copy an existing object
Constraint: must use the clone() method of the existing object to create the object and the existing object's clone() method must define how to copy itself 

Class: [] list operator
Problem: Stores the value of a list
Constraint: returns the list at the same address (shallow copy)

Class: [:] list slicing operator
Problem: Stores the value of a list at specific offsets of that list
Constraint: returns the list at a new address (deep copy), however nested list retains the list operator behavior returning the at the same address (shallow copy)

Module: copy
Problem: a standard library used for making clones of objects
    Class: deepcopy
    Problem: allows you to fully copy a list to a new address

Method: clone()
Problem: Uses an abstract base class to implement the clone() method
Constraint: Every object must clone itself using the abstract base class, if an existing object exists, new objects must be created using its clone() method

Filename: prototype_1.py
Problem: Creates an abstract base class which objects will use as a parameter in their class definitions

Module: abc
Class: ABCMeta | abstractmethod

Metaclass: Prototype
    Problem: using parameters metaclass=ABCMeta to create an abstract base class which can be inherited by other classes
        Method: clone
        Problem: clones an existing object
        Constraint: using @abstractmethod ensures that the method is implemented before an object is created when this class is inherited

Filename: concrete.py

Module: prototype_1
Class: Prototype

Module: copy
Class: deepcopy

    Class: Concrete
    Problem: uses the abstract class Prototype as a parameter
        Method: clone
        Problem: returns a copy an existing object using deepcopy() 

Filename: rts_prototype.py
Problem: Creates a barracks and stables object, creates each unit using lowercase of the unit class name and 1 or 2 as the level, subsequently pass those objects individually as a string to print() displaying the stats of the objects
Constraint: The script only runs if its executed not if its imported

Module: prototype_1
Class: Prototype

Module: copy
Class: deepcopy

    Class: Warrior
    Problem: parameter Prototype class is inherited to define a Warrior class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Warrior", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

        Method: clone()
        Problem: returns a copy of this object by using deepcopy() with parameter self

     Class: Archer
     Problem: parameter Prototype class is inherited to define a Archer class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Archer", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file


        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

        Method: clone()
        Problem: returns a copy of this object by using deepcopy() with parameter self

    Class: Spearman
    Problem: parameter Prototype class is inherited to define a Spearman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Spearman", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

        Method: clone()
        Problem: returns a copy of this object by using deepcopy() with parameter self

     Class: Crossbowman
     Problem: parameter Prototype class is inherited to define a Crossbowman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Crossbowman", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

        Method: clone()
        Problem: returns a copy of this object by using deepcopy() with parameter self

    Class: Barracks
    Problem: parameter Prototype class is inherited to define a Barracks class

        Method: __int__()
        Problem: using self parameter, it creates one instance of every available unit level with their corresponding unit types
        Constraint: uses the class variable units to store a dictionary with keys of each unit class name in lowercase set to dictionary of keys of the corresponding unit level which has a value of the class initializing the unit with its level number

        Method: build_unit()
        Problem: parameters self, unit_type, and level are used to return a Warrior | Archer | Spearman | Crossbow object
        Constraint: the class variable units using parameter unit_type as a key and parameter level as a key within unit_type key to call unit prototype object clone() method to return a clone object for the unit type and level

    Class: Horseman
    Problem: parameter Prototype class is inherited to define a Horseman class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Horseman", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

        Method: clone()
        Problem: returns a copy of this object by using deepcopy() with parameter self

    Class: Knight
    Problem: parameter Prototype class is inherited to define a Knight class

        Method: __init__()
        Problem: parameters self and level are used to initialized the class variables
        Constraint: sets unit_type to "Knight", sets filename to unity type, underscore, level, and ".dat" concatenated then open() the file using context manager with, reads the file contents splitting it by newline occurences, and sets the class variables life, speed, attack_power, attack_range, weapon to their respectively values stored in the file

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type
        Contraint: the title of the stat, colon, space, stat value, newline for each stat

        Method: clone()
        Problem: returns a copy of this object by using deepcopy() with parameter self

    Class: Stables
    Problem: parameter Prototype class is inherited to define a Stables class

        Method: build_unit()
        Problem: using self parameter, it creates one instance of every available unit level with their corresponding unit types
        Constraint: the class variable units using parameter unit_type as a key and parameter level as a key within unit_type key to call unit prototype object clone() method to return a clone object for the unit type and level


