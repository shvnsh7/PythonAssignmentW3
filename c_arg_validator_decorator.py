"""A decorator to validate arguments passed to a function based on a condition"""
def range_validator(min_value, max_value):
    """it generates validator in the range of min,max"""
    def decorator(func):
        def wrapper(num):
            if num < min_value or num > max_value:
                raise ValueError(f"Number {num} is out of range ({min_value} to {max_value})")
            return func(num)
        return wrapper
    return decorator

@range_validator(1, 10)
def generate_square_sequence(num):
    """it generates square sequence"""
    return [x**2 for x in range(1, num+1) if x % 2 == 0]

# Test the function with valid input
valid_result = generate_square_sequence(8)
print("Valid Result:", valid_result)

# Test the function with invalid input
try:
    invalid_result = generate_square_sequence(15)
except ValueError as e:
    print("Invalid Result:", str(e))
