# Find all IPv4 Addresses in "TEXT" variable
import re; ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', TEXT)