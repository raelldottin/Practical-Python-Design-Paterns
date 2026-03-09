Note Taking Criteria


The Class
Ask: Who or what is performing the action?

The Problem
Ask: What happens to the data when the Actor touches it?

The Constraint
Ask: Where does the logic break or change?

The Inverse
Ask: If I do this, how do I undo it?

What to Igore
The "Why": Author's opinion
The "Context": Historical filler
The "Bridge" Instructional transition


Book: Practical Python Design Patterns: Pythonic Solutions to Common Problems Wessel Badenhorst


Class: print() statement
Problem: it prints debugging statements to console
Constraint: the program is running remotely the console output ins't available
Inverse: you delete the print statements when you're no longer debugging

Class: DRY principle
Problem: don't repeat yourself
Contraint: copying, pasting and repeating the same code
Inverse: you only change that code in that one place

Class: open() statement
Problem: it prints debugging messages to a file
Constraint: the log file has to be opened each time a log message has to be written to the log file
Inverse: close() statement

Class: Logger
Method: __init__()
	Problem: parameters self and file_name are used to create an object with file_name property set with the log file's name
	Contraint: mutliple objects can be created writing to the same or different log file
Method: _write_log()
	Problem: parameters self, level, msg are used to write a log message to a log file
	Constraint: opens and closes the logfile each time it write a new message
Method: critcal() | error() | warn() | info() | debug()
	Problem: parameters self, level, msg are used to write a log message using _write_log()
	Constraint: hard coded levels

Class: SingletonObject
	Problem: parameters object is used to define a singleton class
	Constraint: code in one part of your project may alter its global state and cause unexpected results in a completely unrelated piece of code
	Class: __SingletonObject
		Problem: a private class that should not be used outside of the original class definition
		Method: __init__():
			Problem: parameter self is used to initialize variable val for use within the class
		Method: __str__()
			Problem: parameter self is used to returns a string when the interface is used in a string data type
		Method: __new__()
			Problem: parameter cls passes the class definition data and creates a new object 
			Constraint: the class defintion already has an instance of the private __SingletonObject returns the instance as the new object otherwise create a new object of it, store it in the class instance variable and return the new instance
		Method: __getattr__() | __setattr__()
			Problem: parameters self and name are used to allow the private class to read and write data to the instance class
