class Logger(object):
    """A file-based message logger with the following properties

    Attributes:
    file_name: a string represting the full path of the log file to which this logger will write its messages
    """

    def __init__(self, file_name):
        """Return a Logger object whose file_name is *file_name*"""
        self.file_name = file_name

    def _write_log(self, level, msg):
        """Write a message to the file_name for a specific Logger instance"""
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
