import os.path
from exercise_1 import Logger


def read_log(file_name):
    if not os.path.exists(file_name):
        print("{0} doesn't exists".format(file_name))
        return

    print("{0} contains:".format(file_name))
    with open(file_name, "r") as log_file:
        print(log_file.read())


def main():
    obj1 = Logger("class_logger_object_1.log")
    print("{0} contain the following objects: {1}".format(obj1, dir(obj1)))
    obj1.info("This is an info message for obj1")
    read_log("class_logger_object_1.log")
    obj2 = Logger("class_logger_object_2.log")
    print("{0} contain the following objects: {1}".format(obj2, dir(obj2)))
    obj2.info("This is an info message for obj2")
    read_log("class_logger_object_2.log")

if __name__ == "__main__":
    main()
