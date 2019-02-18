import argparse
import logging
import subprocess
import time
from subprocessing import subprocessing


error_text = "Didn't match the threshold"
info_text = "Everything's OK"


def main():
    helper = "Receives the amount of disk space available on the file system containing each file name argument " \
            "by using bash command du -s [PATH]  along with threshold arguments to compute if file system doesn’t " \
            "use too much memory space. If no file name is given, the space available on all currently mounted file" \
            " systems is being processed."

    parser = argparse.ArgumentParser(description=helper)
    parser.add_argument("PATH", help="path to the directory which will be processed")
    parser.add_argument("-w", help="warning threshold in kB", type=int, required=True)
    parser.add_argument("-c", help="critical threshold in kB", type=int, required=True)
    args = parser.parse_args()

    shell_output = subprocess.check_output(["du", "-s", args.PATH])
    space = int(shell_output.split()[0])
    logging.basicConfig(format='%(asctime)s\t%(process)d-%(name)s-%(levelname)s-%(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    if space < args.w:
        logging.info(info_text)
        status = 0
    elif args.w <= space < args.c:
        logging.warning(error_text)
        status = 1
    else:
        logging.critical(error_text)
        status = 2
    return status, int(time.time()), space


if __name__ == "__main__":
    print(main())
    #print(datetime.fromtimestamp(main()[1]))
