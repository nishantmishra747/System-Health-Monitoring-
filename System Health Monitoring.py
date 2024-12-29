#!/bin/bash

# Set the maximum threshold for CPU and memory usage
MAX_THRESHOLD=80

while true; do
    # Get CPU usage
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | \
                sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | \
                awk '{print 100 - $1}')
    
    # Get memory usage
    mem_total=$(grep MemTotal /proc/meminfo | awk '{print $2}')
    mem_free=$(grep MemFree /proc/meminfo | awk '{print $2}')
    mem_usage=$(awk "BEGIN {print ($mem_total - $mem_free) / $mem_total * 100}")

    # Print CPU and memory usage
    echo "CPU Usage: $cpu_usage%"
    echo "Memory Usage: $mem_usage%"

    # Check if CPU usage exceeds the threshold
    if (( $(echo "$cpu_usage > $MAX_THRESHOLD" | bc -l) )); then
        echo "Warning: CPU usage exceeds $MAX_THRESHOLD%!"
    fi

    # Check if memory usage exceeds the threshold
    if (( $(echo "$mem_usage > $MAX_THRESHOLD" | bc -l) )); then
        echo "Warning: Memory usage exceeds $MAX_THRESHOLD%!"
    fi

    # Sleep for 1 second
    sleep 1
done
