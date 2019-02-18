import logging
import subprocess
import argparse
import time
from datetime import datetime


def main():
    with open('../../help/disk_filesystem_status_help.txt', 'r') as myfile:
        descr = myfile.read()
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument("PATH", help="path to the directory which will be processed")
    parser.add_argument("-w", help="warning threshold in kB", type=int)
    parser.add_argument("-c", help="critical threshold in kB", type=int)
    args = parser.parse_args()
    error_text = "Didn't match the threshold"
    info_text = "Everything's OK"
    shell_output = subprocess.check_output(["du", "-s", args.PATH])
    space = int(shell_output.split()[0])
    logging.basicConfig(format='%(asctime)s\n\t%(process)d-%(name)s:%(levelname)s:%(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    # if args.w:
    #	print(args.w)
    # if args.c:
    #	print(args.c)
    if space < args.w:
        logging.info(info_text)
        return 0, int(time.time()), space
    elif args.w <= space < args.c:
        logging.warning(error_text)
        return 1, int(time.time()), space
    logging.critical(error_text)
    return 2, int(time.time()), space


if __name__ == "__main__":
    print(main())
    #print(datetime.fromtimestamp(main()[1]))
