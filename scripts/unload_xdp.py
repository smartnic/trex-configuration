import os
from os.path import expanduser
import argparse 
benchmarks = ["xdp1", "xdp2", "xdp_pktcntr", "xdp_redirect", "xdp_map_access", "xdp_fw", "xdp_router_ipv4", "xdp_fwd"]
home = expanduser("~")
parser = argparse.ArgumentParser(description='Information about Data')
parser.add_argument('-b', dest="benchmark", type=str, help=f"Benchmark {str(benchmarks)}", required=True)
args = parser.parse_args()

# read interfaces
f = open("device.config", "r")
device = f.read()
device = node0.strip('\n')
f.close()
i = open(f"{device}.config", "r")
interfaces = f.read().split("\n")
print(interfaces)
for i in interfaces:
    os.system("sudo pkill -f \"{i}\"")
    os.system("sudo ip link set dev {i} xdp off")
os.chdir(f"{home}/throughput-experiments")
os.system(f"rm {args.benchmark}.o")