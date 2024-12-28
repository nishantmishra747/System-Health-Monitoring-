import psutil
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0
PROCESS_THRESHOLD = 300

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk usage detected: {disk_usage}%')
    return disk_usage

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f'High number of processes running: {process_count}')
    return process_count

def monitor_system():
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    processes = check_processes()

    logging.info(f'System Health - CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}')

if __name__ == "__main__":
    monitor_system()