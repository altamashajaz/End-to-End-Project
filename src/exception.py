import sys
import logging
from logger import logging


def error_message_details(error, error_details: sys):
    """
    Constructs an error message with details about the file name, line number, and the error message.
    
    Args:
        error (Exception): The exception that was raised.
        error_details (module): The sys module to access exception information.
    
    Returns:
        str: A formatted string containing details about the error.
    """
    _, _, exc_tb = error_details.exc_info()  # Extract traceback object from exception info
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the error occurred
    line_number = exc_tb.tb_lineno  # Get the line number where the error occurred
    
    # Format and return the error message
    error_message = "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    
    return error_message

class CustomException(Exception):
    """
    A custom exception class that captures and formats detailed error messages.
    
    Args:
        error_message (Exception): The exception that was raised.
        error_details (module): The sys module to access exception information.
    """
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)  # Initialize the base Exception class
        # Capture the detailed error message using the provided function
        self.error_message = error_message_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message


if __name__=='__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
    