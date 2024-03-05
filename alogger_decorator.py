# """import logging and datetime to have real time logs of file"""
# import logging 
# import datetime 
# def logger_decorator(func):
#     """this is the logger decorator which takes func as a parameter"""
#     def wrapper(*args, **kwargs):
#         """this can accept any no.of positional and keywords args"""
#         # Get the current date and time
#         current_datetime = datetime.datetime.now()

#         # Get the module name and function name
#         module_name = func.__module__
#         function_name = func.__name__

#         # Get the log file name
#         log_file_name = f"{module_name}_{current_datetime.strftime('%Y%m%d')}.log"

#         # Configure the logger
#         logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(message)s')

#         # Log the details
#         logging.info(f"{module_name} {function_name} {current_datetime.strftime('%d-%m-%Y %H:%M:%S')} {str(args)} {str(kwargs)}")

#         # Call the original function
#         return func(*args, **kwargs)

#     return wrapper

# # Example usage
# @logger_decorator
# def example_function(arg1, arg2, kwarg1=None, kwarg2=None):
#     "This is an example function"
#     print("This is the example function")
#     return arg1 + arg2

# # Test the decorator
# result = example_function(3, 4, kwarg1='Hello hi Kat', kwarg2='World is beau')
# print("Result:", result)