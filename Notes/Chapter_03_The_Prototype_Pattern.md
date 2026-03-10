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

Class rts-simple.py


Problem:Creates a barracks and stables object, uses barracks to generate a knight object, passes the knight object as a string to print() displaying the knight object stats, uses stables to generate a horseman object, passes the horseman object as a string to print() displaying the horseman object stats.
Constraint: The script only runs if its executed not if its imported

    Class: Knight
    Problem: parameters object is used to define a Knight class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variablesusing the self parameter when the object is created

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type


    Class: Barracks
    Problem: parameters object is used to define a Barracks class

        Method: generate-knight
        Problem: parameters self to return an object to a Knight class
        Constraint: Knight properties are hardcoded as 400, 5, 3, 1, "short sword" during the object creation

    Class: Horseman
    Problem: parameters object is used to define a Horseman class

        Method: __init__()
        Problem: parameters life, speed, attack_power, attack_range, weapon used to initialized the respective class variablesusing the self parameter when the object is created

        Method: __str__()
        Problem: parameter self is used to returns a string when the object is used in a string data type

    Class: Stables
        Method: generate-horseman
        Problem: parameters self to return an object to a Horseman class
        Constraint: Horseman properties are hardcoded as 200, 3, 2, 1


