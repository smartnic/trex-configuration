import os
from os.path import expanduser
home = expanduser("~")
os.system("sudo ip link set dev ens3f0 xdp off")
os.system("sudo ip link set dev ens3f1 xdp off")
os.chdir(f"{home}/throughput-experiments")
os.system("rm xdp_fwd_kern.o")