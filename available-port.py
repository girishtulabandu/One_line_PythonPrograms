import os
import sys


# Def function log
# print a new line to debug


def log(msg):
    print(print_prefix + msg)


args = sys.argv
port = ''
print_prefix = "-> "
if len(args) > 1:
    port = args[1]
else:
    log("please indicate a port")
    log("ex: python available-port.py {port-number}")
    log("{port-number} must be replaced with de port number what you want to check")
    exit(0)

log("checking port: " + port)
stream = os.popen('netstat -lntu | grep :' + port + ' | awk \'{print $6}\'')
output = stream.read()

if len(output) > 0:
    log("status: " + output)
else:
    log("port " + port + " is not listening")

