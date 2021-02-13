#!/usr/bin/env python3
# A System Information Gathering Script
import subprocess


def uname():
    cmd = "uname -a"
    print("Gathering system information with %s command:\n" % cmd)
    subprocess.call(cmd, shell=True)


def disk():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering diskspace information %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])


def hostname():
    print("Hostname:")
    subprocess.call("cat /etc/hostname", shell=True)


def main():
    uname()
    disk()
    hostname()


if __name__ == "__main__":
    main()
