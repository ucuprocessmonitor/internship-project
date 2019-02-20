import subprocess


def subprocessing(args, shl=False):
    return subprocess.check_output(args, shell=shl).decode().split()

