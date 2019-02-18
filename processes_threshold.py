import subprocess
import sys

str = sys.argv[1] + ' ' + sys.argv[2] + '|' + "awk '{print $11}'"
output = subprocess.check_output([str], shell=True)
output = output.decode().split('\n')
count = 0
for i in range(len(output)):
	if(output[i]==sys.argv[3]):
		count += 1
if(count <= int(sys.argv[4]) and count != 0):
	print("OK")
if(count > int(sys.argv[4])):
	print("CRITICAL")
if(count == 0):
	print("WARNING: NO SUCH PROCESSES RUNNING")