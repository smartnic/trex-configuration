import os
import time 
import sys
import argparse 

parser = argparse.ArgumentParser(description='Information about Data')
parser.add_argument('-d', dest="directory", type=str, help='Directory', required=True)
parser.add_argument('-v', dest="version", type=str, help='Name of version (e.g o1, o2, k0, k1, k2, k3, k4)', required=False)
parser.add_argument('-n', dest="number", type=int, help='Number of times each version should run', default=5)
args = parser.parse_args()
versionList = []
if (args.version):
    versionList.append(args.version)
else:
    versionList = ["o1", "o2", "k4"]
# Read node0 configuration
f = open("demofile.txt", "r")
node0 = f.read()
for v in versionList:
    print(f"Running {v}")
    print(f"Starting T-rex")
    os.system("nohup sudo ./t-rex-64 -i -c 14 > log.txt &")
    time.sleep(300)
    with open('log.txt') as f:
        if 'ERROR encountered while configuring TRex system' in f.read():
            print("Error while starting Trex")
            exit(0)
    print(f"Loading xdp...")
    os.system(f"ssh -p 22 {node0} 'python3 -u load_xdp.py {v.upper()}; exit'")
    time.sleep(10)

    for x in range (number):
        print(f"Iteration {x}")
        print("Running MLFFR")
        os.system(f"python3 -u mlffr.py -d {args.directory} -v {v} -r {x} -mS 1.3 -mE 1.45 -i 0.01")

    print("Unloading xdp")
    os.system(f"ssh -p 22 {node0} 'python3 unload_xdp.py; exit'")
    print("Stopping T-rex and all its children")
    os.system("sudo pkill t-rex")
    time.sleep(200)

print("Completed Full Script")