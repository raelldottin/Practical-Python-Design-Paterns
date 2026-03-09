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
	Problem: parameters object is used to define a singleton class and initialize the instance variable as None
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


Exercises:


1. Implement your own logger singleton.

Class: Logger
    Problem: parameters object is used to define a Logger class and initialize the instance variable as None
	Constraint: code in one part of your project may alter its global state and cause unexpected results in a completely unrelated piece of code
    Class: __Logger
        Problem: a private class that should not be used outside of the original class definition
        Method: __init__():
            Problem: parameters self and filename are used to create an object with filename property set with the log filename
		Method: __str__()
			Problem: parameter self is used to returns the name of the instance and its log filename when the interface is used in a string data type
		Method: __new__()
			Problem: parameter cls, *args, **kwargs passes the class definition data and arguments from outer class and creates a new object 
		Method: __getattr__()
			Problem: parameters self and name are used to allow the private class to read data from the instance class
		Method: __setattr__()
			Problem: parameters self and name and value are used to allow the private class to write data to the instance class
        Method: __write_log()
            Problem: parameters self, level, msg are used to write a log message to a log file
            Constraint: opens and closes the logfile each time it write a new message
            Inverse: with context manager automatically calls close() when the code exits the indented block, even if an error occurs
        Method: critcal() | error() | warn() | info() | debug()
            Problem: parameters self, msg are used to write a log message using _write_log()
            Constraint: hard coded levels - CRITICAL | ERROR | WARN | INFO | DEBUG

Filename: loggerclass.py
class Logger(object):
  instance = None
  class __Logger():
    def __init__(self, filename):
      self.filename = filename

    def __str__(self):
      return("{0!r} {1}".format(self, self.filename))

    def __new__(cls, *args, **kwargs):
      if not Logger.instance:
        Logger.instance = Logger.__Logger(*args, **kwargs)

      return(Logger.instance)

    def __getattr__(self, name):
      return(getattr(self.instance, name))

    def __setattr__(self, name, value):
      return(setattr(self.instance, name, value))

    def __write_log(self, level, msg):
      with open(self.filename, "a") as logfile:
        logfile.write("[{0}] {1}\n".format(level, msg))

    def critical(self, msg):
      self.__write_log("CRITICAL", msg)

    def error(self, msg):
      self.__write_log("ERROR", msg)

    def warn(self, msg):
      self.__write_log("WARN", msg)

    def info(self, msg):
      self.__write_log("INFO", msg)

    def debug(self, msg):
      self.__write_log("DEBUG", msg)

2. How would you create using the singleton pattern?
Filename: new-script-with-loggerclass.py
from loggerclass import Logger

loggerobject = Logger("./classlogger.log")

loggerobject.info("This is an info message")

try:
  a = 1 / 0
except:
  loggerobject.critical("Division by zero is not possible in mathematics")

for e in ["CRITICAL", "ERROR", "WARN", "INFO", "DEBUG"]:
    method = getattr(loggerobject, e.lower())
    method("{0} log level message is sent!".format(e))

anotherloggerobject = Logger("./differentlogger.log")
print("Are they the same? {0}".format(loggerobject is anotherloggerobject))
print("Active log file name: {0}".format(anotherloggerobject.filename))
