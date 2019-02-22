import logging
import logging.config
import os
import subprocess


def subprocessing(args, shl=False):
    return subprocess.check_output(args, shell=shl).decode()


def configure_logging():
    logging.config.fileConfig(os.environ["CONFROOT"] + "/logging.conf")
    return logging.getLogger()
