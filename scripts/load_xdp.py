import os
from os.path import expanduser
import sys
import argparse 

interfaces = ["ens3f1"]
programs = {
    "xdp2": ("xdp2_kern", "completed-programs/camera_ready/0630_80b79d0_runtime_xl170/xdp2_kern_xdp1"),
    "xdp_fw": ("xdp_fw_kern", "completed-programs/camera_ready/simple_fw_xdp_fw_kern_xdp_fw_0611_073defe_runtime"),
    "xdp_router_ipv4": ("xdp_router_ipv4_kern", "completed-programs/camera_ready/0630_80b79d0_runtime_xl170/xdp_router_ipv4"),
    "xdp_fwd": ("xdp_fwd_kern", "completed-programs/camera_ready/0630_80b79d0_runtime_xl170/kernel_xdp_fwd"),
    "xdp_pktcntr": ("xdp_pktcntr", "completed-programs/camera_ready/xdp_pktcntr_0611_073defe_runtime"),
}
parser = argparse.ArgumentParser(description='Information about Data')
parser.add_argument('-b', dest="benchmark", type=str, help=f"Benchmark {str(programs.keys())}", required=True)
parser.add_argument('-v', dest="version", type=str, help='Name of version (e.g O1, O2, K0, K1, K2, K3, K4)', required=True)
args = parser.parse_args()

home = expanduser("~")
home = "/usr/local"
# read interfaces
f = open(f"{home}/trex-configuration/scripts/device.config", "r")
device = f.read()
device = device.strip('\n')
f.close()
i = open(f"{home}/trex-configuration/scripts/{device}.config", "r")
interfaces = i.read().split("\n")

os.chdir(f"{home}/throughput-experiments")
for x in interfaces:
    os.system(f"sudo ip link set dev {x} xdp off")

number = list(args.version)[1]
if "k" in args.version.lower():
    os.system(f"sudo cp {programs[args.benchmark][1]}/top-progs/{programs[args.benchmark][0]}{number}.o {programs[args.benchmark][0]}.o")
else:
    os.system(f"sudo cp {args.version.upper()}/{programs[args.benchmark][0]}.o .")

# load program 

if args.benchmark == "xdp1":
    os.system(f"sudo ./xdp1 -N {interfaces[0]}")
elif args.benchmark == "xdp2":
    os.system(f"sudo ./xdp2 -N {interfaces[0]}")
elif args.benchmark == "xdp_pktcntr":
    os.system(f"sudo ip link set dev {interfaces[0]} xdp obj xdp_pktcntr.o sec xdp-pktcntr")
elif args.benchmark == "xdp_redirect":
    if len(interfaces) == 1:
        os.system(f"sudo ./xdp_redirect -N {interfaces[0]} -N {interfaces[0]}")
    else: 
        os.system(f"sudo ./xdp_redirect -N {interfaces[0]} -N {interfaces[1]} ")
elif args.benchmark == "xdp_map_access":
    os.system(f"sudo ./xdp_map_access -N {interfaces[0]}")
elif args.benchmark ==  "xdp_fw":
    os.system(f"sudo ./xdp_fw")
elif args.benchmark ==  "xdp_router_ipv4":
    os.system(f"sudo ./xdp_router_ipv4 -S {interfaces[0]}")
elif args.benchmark ==  "xdp_fwd":
    os.system(f"sudo ./xdp_fwd {' '.join(interfaces)}")