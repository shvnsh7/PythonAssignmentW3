""""Input -  "My name is Suraj" output - "Suraj is name My"""
import time
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
def Rev(SENTENCE):
    """this is for reversing the string"""
    word=SENTENCE.split(' ')
    #print(word)
    rev=' '.join(reversed(word))
    return rev

# if __name__=="__main__":
#     input="My name is Suraj"
#     print(reverseStr(input))

SEN="My name is Suraj"
print(Rev(SEN))
