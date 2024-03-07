"""print fibonacci series"""
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
def fibonacci(n):
    """this function gives the fibonacci series"""
    #n=int(input("Enter the number "))
    n1,n2=0,1
    count=0

    if n<=0:
        print("Enter a positive intiger")

    elif n==1:
        print("1")

    else:
        while count <n:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1

print(fibonacci(6))
