import argparse
import core.utils
import sys


error_text = "DIDN'T MATCH THE THRESHOLD"
info_text = "EVERYTHING'S OK"

CRITICAL_CODE = 2
WARNING_CODE = 1
OK_CODE = 0

def main():
    """Receives the amount of disk space available on the file system given FILE name argument

    Args:
        PATH: path to the directory.
        w: warning threshold in kB.
        c: critical threshold in KB

    Returns:
        The return value of status. 0 for success, 1 for warning, 2 for critical status.

    >> ${PYTHON} ${PYSRCROOT}/monitors/disk_filesystem_status.py ~/Documents -w 3000000 -c 6000000
    2019-02-22 12:22:01      23971-root:WARNING-DIDN'T MATCH THE THRESHOLD


    >> ${PYTHON} ${PYSRCROOT}/monitors/disk_filesystem_status.py ~/Documents/ai -w 200000 -c 400000
    2019-02-22 12:23:19      24047-root:INFO-EVERYTHING'S OK
    """
    helper = "Receives the amount of disk space available on the file system containing each file name argument " \
            "by using bash command du -s [PATH]  along with threshold arguments to compute if file system does not " \
            "use too much memory space. If no file name is given, the space available on all currently mounted file" \
            " systems is being processed."

    parser = argparse.ArgumentParser(description=helper)
    parser.add_argument("PATH", help="path to the directory which will be processed")
    parser.add_argument("-w", help="warning threshold in kB", type=int, required=True)
    parser.add_argument("-c", help="critical threshold in kB", type=int, required=True)
    args = parser.parse_args()

    shell_output = core.utils.subprocessing(["du", "-s", args.PATH])
    space = int(shell_output[0])

    logger = core.utils.configure_logging()

    if space < args.w:
        logger.info(info_text)
        status = OK_CODE
    elif args.w <= space < args.c:
        logger.warning(error_text)
        status = WARNING_CODE
    else:
        logger.critical(error_text)
        status = CRITICAL_CODE
    return status


if __name__ == "__main__":
    sys.exit(main())
