# II. Write a program to monitor the applications running on your system. 
# To test: Execute any application like browser, notepad, calculator etc and make sure 
# that not more than 2 instances of the same application can be running

import psutil

def monitor_running_applications():
    app_counts = {}
    for proc in psutil.process_iter(['name']):
        app_name = proc.info['name']
        if app_name in app_counts:
            app_counts[app_name] += 1
        else:
            app_counts[app_name] = 1

    for app_name, count in app_counts.items():
        if count > 2:
            print(f"Warning: More than 2 instances of {app_name} running!")

# Testing the program
monitor_running_applications()