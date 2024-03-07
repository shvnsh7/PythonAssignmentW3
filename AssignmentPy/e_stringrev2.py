""""importing time for logging"""
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
def reverse_sentence(sentence):
    """this function reverses the given sentence"""
    words=[]  #empty list is initialised to store the words in sentence
    current_word=' ' #empty string
    for character in sentence:
        if character==' ':
            words.append(current_word)
            current_word=''
        else:
            current_word+=character
    words.append(current_word)
    reversed_sentence=' '.join(reversed(words))
    return reversed_sentence

input_sentence=input("Enter a sentence: ")
#input_sentence="My name is Suraj"
REV=reverse_sentence(input_sentence)
print("Reversed Sentence: ",REV)
