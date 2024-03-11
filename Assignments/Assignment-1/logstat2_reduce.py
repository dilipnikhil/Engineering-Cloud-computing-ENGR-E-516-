#author : Dilip Nikhil Francies
#reducer function for part 2

import sys
# Create an empty dictionary to store IP counts
ip_counts = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith("["):
        # Extract hour and IP address
        hour, ip = line.split()[0], line.split()[1]
        # Strip brackets from hour
        hour = hour.strip("[]")
        # Update IP count in the dictionary
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

sorted_ip_counts = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
# Print the dictionary containing IP counts
for ip, count in sorted_ip_counts[:3]:  #sort top three
    print(f"[{hour}] {ip} {count}")

