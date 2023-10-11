"""
Implement your own logger singleton
Chapter 2, Exercise 1
"""


class Logger:
    """A file-based message logger with the following properties

    Attributers:
        file_name: a string representing the full path of the log file to which this logger will write its messages
    """

    _instance = None

    def __new__(cls, file_name):
        """Return the class object if the class was already created; otherwise, create a new class"""
        if cls._instance == None:
            cls._instance = super(Logger, cls).__init__(file_name)

        return cls._instance

    def __init__(self, file_name):
        """Return a Logger object whose file_name is *file_name*"""
        self.file_name = file_name

    def _write_log(self, level, msg):
        """Writes a message to the file_name for a specific Logger instance"""
        with open(self.file_name, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, msg, level="CRITICAL"):
        self._write_log(level, msg)

    def error(self, msg, level="ERROR"):
        self._write_log(level, msg)

    def warn(self, msg, level="WARN"):
        self._write_log(level, msg)

    def info(self, msg, level="INFO"):
        self._write_log(level, msg)

    def debug(self, msg, level="DEBUG"):
        self._write_log(level, msg)
