import logging
import logging.config
import subprocess


def subprocessing(args, shl=False):
    return subprocess.check_output(args, shell=shl).decode().split()


def configure_logging():
    logging.config.fileConfig('../../../etc/logging.conf')
    return logging.getLogger()