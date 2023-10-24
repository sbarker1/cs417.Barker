# Samuel Barker
# sbarker1@my.athens.edu
# Assignment 6, Problem 1

# Note: I have attached my LogFile.txt to my GitHub Repo if you would like to review log output. 

# References:
# https://docs.python.org/3/howto/logging-cookbook.html
# https://realpython.com/python-logging/

import enum
import os

class Severity(enum.Enum):
    WARNING = "WARNING"
    ERROR = "ERROR"
    UNRECOVERABLE = "UNRECOVERABLE"

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = None
        return cls._instance

    @classmethod   # Startup method
    def Startup(cls, log_file_path):
        if cls._instance.log_file is not None:
            cls.Shutdown()
        try:
           
            log_dir = os.path.dirname(log_file_path) # Create a directory
            os.makedirs(log_dir, exist_ok=True)

            cls._instance.log_file = open(log_file_path, "a")
        except Exception as e:
            print(f"Error: Failed to open log file. {str(e)}")

    @classmethod   # Shutdown method
    def Shutdown(cls):
        if cls._instance.log_file is not None:
            cls._instance.log_file.close()
            cls._instance.log_file = None

    @classmethod
    def LogMessage(cls, severity, service, error_text):
        if cls._instance.log_file is not None:
            log_entry = f"Severity: {severity}, Service: {service}, Error Text: {error_text}\n"
            cls._instance.log_file.write(log_entry)

if __name__ == "__main__":
    log_file_path = r"C:\Users\erbab\Desktop\LogFile.txt" # This can be changed. 
    logger = Logger()
    logger.Startup(log_file_path)

    while True:
        severity = input("Enter severity by typing WARNING, ERROR, or UNRECOVERABLE: ")
        if severity not in [Severity.WARNING.value, Severity.ERROR.value, Severity.UNRECOVERABLE.value]:
            print("Error: Invalid severity, enter a valid severity.")
            continue

        service = input("Please enter the service name: ")

        error_text = input("Enter the error text: ")

        logger.LogMessage(severity, service, error_text)

        more_entries = input("Do you want to log more messages? Type (yes) to continue OR (no) to shutdown and write to file: ")

        if more_entries.lower() != "yes":
            break

    logger.Shutdown()
