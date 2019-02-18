import subprocess
import sys
import logging

str = 'ps -aux' + '|' + "awk '{print $11}'"
output = subprocess.check_output([str], shell=True)
output = output.decode().split('\n')
count = 0
for i in range(len(output)):
	if(output[i]==sys.argv[1]):
		count += 1

FORMAT = '%(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('check_output')

if(count <= int(sys.argv[2]) and count != 0):
	logger.warning('System status: %s', 'OK')
if(count > int(sys.argv[2])):
	logger.warning('System status: %s', 'CRITICAL')
if(count == 0):
	logger.warning('System status: %s', 'WARNING: NO SUCH PROCESSES RUNNING')
