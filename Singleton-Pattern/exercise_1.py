"""
Implement your own logger singleton
Chapter 2, Exercise 1
"""


class Logger(object):
    class __Logger:
        def __init__(self, file_name):
            """Return a Logger object whose file_name is *file_name*"""
            self.file_name = file_name

        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)

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

    _instance = None

    def __new__(cls, file_name):
        if not Logger._instance:
            Logger._instance = Logger.__Logger(file_name)

        return Logger._instance

    def __getattr__(self, name):
        return getattr(self._instance, name)

    def __setattr__(self, name):
        return setattr(self._instance, name)
