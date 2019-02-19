import argparse
import logging
import subprocess
import sys
import time

critical_text = "TOO MANY PROCESSES RUNNING"
warning_text = "NO SUCH PROCESSES RUNNING"
info_text = "EVERYTHING'S OK"

def main():
    helper = "Receives the process name and the number of the maximal amount of " \
    		"processes allowed. If the number of processes is bigger than the indicated " \
    		"threshold, the user is informed that the number is excessive with an error " \
    		"message. Otherwise, an OK message is displayed. Warning if no processes."
    parser = argparse.ArgumentParser(description=helper)
    parser.add_argument("NAME", help="name of the process that is checked")
    parser.add_argument("COUNT", help="critical threshold of processes", type=int)
    args = parser.parse_args()

    general_output = subprocess.check_output(["ps -aux | grep " + args.NAME], shell=True)
    logging.basicConfig(format='%(asctime)s\t%(process)d-%(name)s\t%(levelname)s:%(message)s',
    					level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    process_output = subprocess.check_output(["ps -aux | awk '{print $11}' | grep " + args.NAME], shell=True)
    num_of_processes = process_output.decode().split().count(args.NAME)
    status = 0
    if num_of_processes > args.COUNT:
        logging.critical(critical_text)
        status = 2
    elif num_of_processes == 0:
        logging.warning(warning_text)
        status = 1
    elif num_of_processes <= args.COUNT:
    	logging.info(info_text)
    	status = 0
    return status

if __name__ == "__main__":
    sys.exit(main())