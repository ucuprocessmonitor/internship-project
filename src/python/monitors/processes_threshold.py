import subprocess
import argparse
import logging
import time
import sys


def main():
    with open('../../help/processes_threshold_help.txt', 'r') as myfile:
        descr = myfile.read()
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument("FILE", help="name of process that will be checked")
    parser.add_argument("-c", help="critical threshold of processes", default=1, type=int)
    args = parser.parse_args()
    critical_text = "Didn't match the threshold"
    warning_text = "No such process running"
    info_text = "Everything's OK"
    shell_output = subprocess.check_output(["ps -aux | awk '{print ($11)}' | grep " + args.FILE], shell=True)
    logging.basicConfig(format='%(asctime)s\n\t%(process)d-%(name)s:%(levelname)s:%(message)s', level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')

    num_of_processes = shell_output.decode().split().count(args.FILE)
    if num_of_processes > args.c:
        logging.critical(critical_text)
        return 2, time.time(), num_of_processes
    elif num_of_processes == 0:
        logging.warning(warning_text)
        return 1, time.time(), num_of_processes
    logging.info(info_text)
    return 0, time.time(), num_of_processes




def bred():
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


if __name__ == "__main__":
    print(main())
    #print(datetime.fromtimestamp(main()[1]))
