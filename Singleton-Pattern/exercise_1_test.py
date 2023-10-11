from exercise_1 import Logger


def read_log(file_name):
    with open(file_name, "r") as log_file:
        log_file.read()


def main():
    obj1 = Logger("class_logger_object_1.log")
    obj1.info("This is na info message for obj1")
    read_log("class_logger_object_1.log")
    obj2 = Logger("class_logger_object_2.log")
    obj2.info("This is na info message for obj2")
    read_log("class_logger_object_2.log")

    print("print obj1: ", obj1)
    print("print obj2: ", obj2)


if __name__ == "__main__":
    main()
