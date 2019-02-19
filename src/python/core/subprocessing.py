import subprocess


def subprocessing(argss, shl=False):
    return subprocess.check_output(argss, shell=shl)
