import subprocess


def subprocessing(args):
    return subprocess.check_output([" ".join(args)])
