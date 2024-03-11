#Author : Dilip Nikhil Francies
#mapper function


import re
import sys
# Compile the regex pattern outside the loop for better performance
ip_hour_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}')
# Retrieve command-line arguments directly

try:
    start_period, end_period = map(int, sys.argv[1:3]) # pars from arguments
except (ValueError, IndexError):
    print("Invalid input. Please provide a valid range as command-line arguments (e.g., '3 4')")
    sys.exit(1)


for line in sys.stdin: #read from acces.log
    line = line.strip()
    match = ip_hour_pattern.search(line)
    if match:
        ip_address = match.group('ip')
        hour = int(match.group('hour'))
        if start_period <= hour < end_period: # check if start time is less than end time
            print(f"[{hour:02}:00] {ip_address} 1") #print ip and hour.



