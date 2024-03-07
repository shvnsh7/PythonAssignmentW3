"""importing a cross-platform lib for retrieving informn on running processes, system utilization"""  
import csv
import time
import psutil

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
def get_running_processes():
    """it is for all the running processes"""
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_list.append({'pid': proc.info['pid'], 'name': proc.info['name']})
    return process_list

@log_execution_time
def count_processes(process_list):
    """this function count processes """
    process_counts = {}
    for process in process_list:
        name = process['name']
        if name in process_counts:
            process_counts[name] += 1
        else:
            process_counts[name] = 1
    return process_counts

@log_execution_time
def store_process_info_csv(process_list, process_counts):
    """this stores the process into csv"""
    with open('process_info.csv', 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['PID', 'Name', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for process in process_list:
            name = process['name']
            pid = process['pid']
            count = process_counts[name]
            writer.writerow({'PID': pid, 'Name': name, 'Count': count})

# Get the list of running processes
running_processes = get_running_processes()

# Count the processes
process_counts = count_processes(running_processes)

# Display the count of each running process
for name, count in process_counts.items():
    print(f"{name}: {count}")

# Store the process information in a CSV file
store_process_info_csv(running_processes, process_counts)
