#!/usr/bin/env python3

from pysysinfo import disk
import subprocess


def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print("Space used in /tmp directory")
    subprocess.call([tmp_usage, tmp_arg, path])


def main():
    disk()
    tmp_space()


if __name__ == "__main__":
    main()
