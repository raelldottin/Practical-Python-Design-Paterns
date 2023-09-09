"""
A command to write the output to a file instead of to the console, like this:
"""
with open("filename.log", "a") as log_file:
    log_file.write("Log message goes here.\n")
