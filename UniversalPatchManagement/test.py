# import module
import subprocess

# Traverse the ipconfig information
data = subprocess.check_output(['ifconfig','/all']).decode('utf-8').split('\n')

# Arrange the bytes data
for item in data:
	print(item.split('\r')[:-1])
