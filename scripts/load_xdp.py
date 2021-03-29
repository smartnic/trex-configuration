import os
from os.path import expanduser
import sys
if len(sys.argv) != 2:
    exit(1)
home = expanduser("~")
os.chdir(f"{home}/throughput-experiments")
os.system("sudo ip link set dev ens3f0 xdp off")
os.system("sudo ip link set dev ens3f1 xdp off")
os.system(f"cp {sys.argv[1]}/xdp_fwd_kern.o .")
os.system(f"sudo ./xdp_fwd ens3f0 ens3f1")