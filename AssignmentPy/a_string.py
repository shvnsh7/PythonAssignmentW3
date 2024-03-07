"""importing time and counter """
import time
# from collections import Counter

def log_execution_time(func):
    """log exceution"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("execution_logs.txt", "a",encoding="utf-8") as f:
            f.write(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds\n")
        return result
    return wrapper

@log_execution_time
def print_common_characters(string):
    """this functions prints common characters"""
    character_counts = {}
    for char in string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    common_characters = sorted(character_counts.items(), key=lambda x: (-x[1], x[0]))
    common_characters = common_characters[:3]
    #using slicing we take 3 most common tuples

    for character, count in common_characters:
        print(f"Character: {character}, Count: {count}")

# Test the program
INPUTSTR = "abracadabra"
print_common_characters(INPUTSTR)
