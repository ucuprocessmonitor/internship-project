<<<<<<< HEAD
=======
import logging
import logging.config
>>>>>>> 1bfa8d06295576b8a1837040c064824c04635295
import subprocess


def subprocessing(args, shl=False):
    return subprocess.check_output(args, shell=shl).decode().split()
<<<<<<< HEAD
=======


def configure_logging():
    logging.config.fileConfig('../../../etc/logging.conf')
    return logging.getLogger()
>>>>>>> 1bfa8d06295576b8a1837040c064824c04635295
