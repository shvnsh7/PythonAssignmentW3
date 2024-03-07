"""psutil is used to retrieve information about running processes
subprocess is used to execute system commands."""
import subprocess
import time
import psutil

def count_running_instances(app_name):
    """this function is for counting running instances"""
    count = 0
    for proc in psutil.process_iter(['name']):
        # It iterates over all running processes using psutil.process_iter()
        if proc.info['name'] == app_name:
            count += 1 #+1 if name matches
    return count

def close_application(app_name, pid):
    """This function, close_application, takes app_name and pid parameters."""
    subprocess.call(['taskkill', '/F', '/PID', str(pid)])
    #subprocess.call() function to execute a system command to forcefully terminate a process

def monitor_applications():
    """this function monitors applications"""
    app_names = ['chrome.exe', 'msedge.exe', 'Teams.exe', 'calc.exe', 'notepad.exe']
    max_instances = 2

    while True:
        for app_name in app_names:
            running_instances = count_running_instances(app_name)
            if running_instances > max_instances:
                print(f"Warning: {running_instances} instances of {app_name} detected.")
                instances_to_close = running_instances - max_instances
                closed_count = 0
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] == app_name:
                        close_application(app_name, proc.info['pid'])
                        closed_count += 1
                        if closed_count >= instances_to_close:
                            break
            else:
                print(f"{running_instances} instances of {app_name} running.")

        # Delay for a few seconds between each check
        time.sleep(5)

monitor_applications()
