import os
import time 
import sys
import argparse 
benchmarks = ["xdp1", "xdp2", "xdp_pktcntr", "xdp_redirect", "xdp_map_access", "xdp_fw", "xdp_router_ipv4", "xdp_fwd"]
parser = argparse.ArgumentParser()
parser.add_argument('-b', dest="benchmark", type=str, help=f"Benchmark {str(=benchmarks)}", required=True)
parser.add_argument('-d', dest="directory", type=str, help='Directory', required=True)
parser.add_argument('-v', dest="version", type=str, help='Name of version (e.g o1, o2, k0, k1, k2, k3, k4)', required=False)
parser.add_argument('-n', dest="number", type=int, help='Number of times each version should run', default=5)
parser.add_argument('-c', dest="cores", type=int, help='Number of cores', default=14)
args = parser.parse_args()
versionList = []
if (args.version):
    versionList.append(args.version)
else:
    versionList = ["o1", "o2", "k0", "k1", "k2", "k3", "k4"]
if (not args.benchmark in benchmark):
    print(f"Invalid benchmark name. {str(benchmarks)}")

# Read node0 configuration
f = open("node0.config", "r")
node0 = f.read()
node0 = node0.strip('\n')
f.close()
print(f"Starting T-rex")
os.system(f"nohup sudo ./t-rex-64 -i -c {args.cores} > log.txt &")
time.sleep(400)
with open('log.txt') as f:
    if 'ERROR encountered while configuring TRex system' in f.read():
        print("Error while starting Trex")
        exit(0)
for x in range (args.number):
    print(f"Iteration {x}")
    for v in versionList:
        print(f"Running {v}")
        print(f"Loading xdp...")
        os.system(f"ssh -p 22 {node0} \"sh -c 'python3 -u $HOME/trex-configuration/scripts/load_xdp.py -b {args.benchmark} -v O1 1>log.txt 2>err.txt &'\"")
        time.sleep(60)
        print("MLFFR...")
        os.system(f"python3 -u mlffr.py -d {args.directory} -v {v} -r {x} -mS 4.4 -mE 5.4 -i 0.1 -rx 0")
        print("Unloading xdp")
        os.system(f"ssh -p 22 {node0} 'python3 $HOME/trex-configuration/scripts/unload_xdp.py {args.benchmark}; exit'")
        time.sleep(60)

print("Stopping T-rex and all its children")
os.system("sudo pkill t-rex")
time.sleep(200)

print("Completed Full Script")