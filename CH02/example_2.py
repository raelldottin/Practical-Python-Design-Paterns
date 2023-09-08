"""
One line is better than two, so create a function that handles opening and writing to the file:
"""


def log_message(msg):
    with open("filename.log", "a") as log_file:
        log_file.write("{0}\n".format(msg))


"""
You can
