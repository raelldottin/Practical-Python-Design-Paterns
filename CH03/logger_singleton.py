
class Logger(object):
    class __Logger():
        def __init__(self, file_name):
            self.file_name = file_name
        
        def _write_log(self, level, msg):
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)
        
        def warn(self, msg):
            self._write_log("WARN", msg)
            
        def info(self, msg):
            self._write_log("INFO", msg)
        
        def debug(self, msg):
            self._write_log("DEBUG", msg)
        
    instance = None
    
    def __new__(cls, file_name):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(file_name)
            
        return Logger.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)
        
    def __setattr__(self, name):
        return setattr(self.instance, name)
        
        
logger_object = Logger("class_logger_1.log")
logger_object.info("This is an info message")

logger_object = Logger("class_logger_2.log")
logger_object.error("This is an error message")
