"""import logging and datetime to have real time logs of file."""

import datetime
import functools

def log_function_calls(log_file_path):
    """this function is for logging function calls"""
    def decorator(func):
        """decorator function"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the current date and time
            current_datetime = datetime.datetime.now()
            
            # Format the log message
            log_message = f"{func.__module__} {func.__name__} {current_datetime.strftime('%d-%m-%Y %H:%M:%S')} {dict(zip(func.__code__.co_varnames, args))}"

            # Write the log message to the log file
            with open(log_file_path, "a",encoding="utf-8") as log_file:
                log_file.write(log_message + "\n")

            # Call the original function
            return func(*args, **kwargs)

        return wrapper

    return decorator

# Example usage:

# Define the log file path
log_file_path = f"example_{datetime.datetime.now().strftime('%Y%m%d')}.log"

@log_function_calls(log_file_path)
def add_numbers(a, b):
    """adding two no """
    return a + b

@log_function_calls(log_file_path)
def multiply_numbers(a, b):
    """multiplying two no"""
    return a * b

# Call the decorated functions
add_numbers(11, 10)
multiply_numbers(30, 2)
