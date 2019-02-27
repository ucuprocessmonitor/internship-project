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
import argparse
import mysql.connector
import sys
from core import utils


error_text = "DIDN'T MATCH THE THRESHOLD"
info_text = "EVERYTHING'S OK"

CRITICAL_CODE = 2
WARNING_CODE = 1
OK_CODE = 0

def main():
    helper = "Receives the amount of disk space available on the file system containing each file name argument " \
            "by using bash command du -s [PATH]  along with threshold arguments to compute if file system does not " \
            "use too much memory space. If no file name is given, the space available on all currently mounted file" \
            " systems is being processed."

    parser = argparse.ArgumentParser(description=helper)
    parser.add_argument("PATH", help="path to the directory which will be processed")
    parser.add_argument("-w", help="warning threshold in kB", type=int, required=True)
    parser.add_argument("-c", help="critical threshold in kB", type=int, required=True)
    args = parser.parse_args()

    shell_output = utils.subprocessing(["du", "-s", args.PATH])
    space = int(shell_output.split()[0])

    logger = utils.configure_logging()

    if space < args.w:
        logger.info(info_text)
        status = OK_CODE
    elif args.w <= space < args.c:
        logger.warning(error_text)
        status = WARNING_CODE
    else:
        logger.critical(error_text)
        status = CRITICAL_CODE

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='internship',
                                       user='roman',
                                       password='password',
                                       auth_plugin = 'mysql_native_password')
        if conn.is_connected():
            print('Connected to MySQL database')
            conn.close()

    except mysql.connector.Error as e:
        print(e)

    return status


if __name__ == "__main__":
    sys.exit(main())
