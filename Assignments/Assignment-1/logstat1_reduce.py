#Author: Dilip
#reducer function

import sys
from operator import itemgetter
from collections import defaultdict
from datetime import datetime, timedelta

hourly_ip_count = defaultdict(lambda: defaultdict(int))
for line in sys.stdin: #input 
    line = line.strip()
    hour, ip, count = line.split('\t', 2)
    count = int(count)
    hourly_ip_count[hour][ip] += count

# Iterate through each hour
for hour, ip_counts in hourly_ip_count.items():
    start_time = datetime.strptime(hour, "%H")
    end_time = start_time + timedelta(hours=1) - timedelta(seconds=1) # from 00:00:00  to 00:00:59 every hour
    hour_range = f"{start_time.strftime('%H:%M:%S')} to {end_time.strftime('%H:%M:%S')}"
    # Sort IP addresses based on their counts
    sorted_ips = sorted(ip_counts.items(), key=itemgetter(1), reverse=True)
    # Output the top 3 IP addresses for each hour
    top_3_ips = sorted_ips[:3] #once sorted, get the top three IPs
    for ip, count in top_3_ips:
        print(f"From {hour_range}, IP: {ip}, Count: {count}") #print