import argparse
import logging
import logging.config
import subprocess
import sys
sys.path.insert(0, '../core/')
import subprocessing

critical_text = "TOO MANY PROCESSES RUNNING"
warning_text = "NO SUCH PROCESSES RUNNING"
info_text = "EVERYTHING'S OK"


def main():
    """Receives the process name and the number of the maximal amount of processes allowed

    Args:
        NAME: name of process
        COUNT: threshold of running processes

    :return:
        The return value of status. 0 for success, 1 for warning, 2 for critical status.

    """
    helper = "Receives the process name and the number of the maximal amount of " \
    		"processes allowed. If the number of processes is bigger than the indicated " \
    		"threshold, the user is informed that the number is excessive with an error " \
    		"message. Otherwise, an OK message is displayed. Warning if no processes."

    parser = argparse.ArgumentParser(description=helper)
    parser.add_argument("NAME", help="name of the process that is checked")
    parser.add_argument("COUNT", help="critical threshold of processes", type=int)
    args = parser.parse_args()

    logging.config.fileConfig('../../../etc/logging.conf')
    logger = logging.getLogger()

    process_output = subprocessing.subprocessing(["ps -aux | awk '{print $11}' | grep " + args.NAME], True)
    num_of_processes = process_output.count(args.NAME)
    status = 0

    if num_of_processes > args.COUNT:
        logger.critical(critical_text)
        status = 2
    elif num_of_processes == 0:
        logger.warning(warning_text)
        status = 1
    else:
        logger.info(info_text)
    return status


if __name__ == "__main__":
    sys.exit(main())
