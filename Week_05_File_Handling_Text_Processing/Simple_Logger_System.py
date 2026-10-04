"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import logging

def create_logger(filename):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename, mode="a")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

def add_log(logger, info):
    logger.info(info)

def view_log(filename):
    with open(filename, "r") as log:
        logs = log.readlines()
    for log in logs:
        print(log)

def clear_log(filename):
    with open(filename, 'w'):
        pass

def main():
    logger = create_logger("simple.log")
    add_log(logger, "HELP ME")
    add_log(logger, "this is a test log")
    view_log("simple.log")
    clear_log("simple.log")
    add_log(logger, "New Log")
    view_log("simple.log")


if __name__ == "__main__":
    main()
