"""Receives the process name and the number of the maximal amount of processes allowed

Args:
    NAME: name of process
    COUNT: threshold of running processes

:return:
    The return value of status. 0 for success, 1 for warning, 2 for critical status.


>> ${PYTHON} ${PYSRCROOT}/monitors/processes_threshold.py bash 2
2019-02-22 12:08:55      23181-root:CRITICAL-TOO MANY PROCESSES RUNNING

>> ${PYTHON} ${PYSRCROOT}/monitors/processes_threshold.py du 1
2019-02-22 12:26:18      24202-root:WARNING-NO SUCH PROCESSES RUNNING

"""

import argparse
import sys
from core import utils

CRITICAL_TEXT = "TOO MANY PROCESSES RUNNING"
WARNING_TEXT = "NO SUCH PROCESSES RUNNING"
INFO_TEXT = "EVERYTHING'S OK"

CRITICAL_CODE = 2
WARNING_CODE = 1
OK_CODE = 0


def main():
    helper = "Receives the process name and the number of the maximal amount of " \
    		"processes allowed. If the number of processes is bigger than the indicated " \
    		"threshold, the user is informed that the number is excessive with an error " \
    		"message. Otherwise, an OK message is displayed. Warning if no processes."

    parser = argparse.ArgumentParser(description=helper)
    parser.add_argument("NAME", help="name of the process that is checked")
    parser.add_argument("COUNT", help="critical threshold of processes", type=int)
    args = parser.parse_args()

    logger = utils.configure_logging()
    process_output = utils.subprocessing(["ps -aux | awk '{print $11}' | grep " + args.NAME], True)
    num_of_processes = process_output.count(args.NAME)

    if num_of_processes > args.COUNT:
        logger.critical(CRITICAL_TEXT)
        status = CRITICAL_CODE
    elif num_of_processes == 0:
        logger.warning(WARNING_TEXT)
        status = WARNING_CODE
    else:
        logger.info(INFO_TEXT)
        status = OK_CODE
    return status


if __name__ == "__main__":
    sys.exit(main())
