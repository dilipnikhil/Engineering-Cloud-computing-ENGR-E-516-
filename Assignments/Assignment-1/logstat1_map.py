#Dilip Nikhil Francies
#Part 1 mapper function

import sys
import re
from datetime import datetime

# Regular expression pattern to match IP addresses and timestamps
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* \[(?P<timestamp>[^\]]+)\]')

for line in sys.stdin:
    match = log_pattern.search(line.strip()) #find matches in the input
    if match:
        ip_address = match.group('ip')
        timestamp_str = match.group('timestamp').split()[0]  # Extracting date from timestamp
        try:
            timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S") #strip the time into Hour, minutes and seconds
            hour = timestamp.strftime("%H")
            print(f"{hour}\t{ip_address}\t1")  # print the hour and the associated IP address
        except ValueError:
            pass
