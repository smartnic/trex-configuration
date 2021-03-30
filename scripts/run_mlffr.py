import os
import time 
import sys
import argparse 

parser = argparse.ArgumentParser(description='Information about Data')
parser.add_argument('-d', dest="directory", type=str, help='Directory', required=True)
parser.add_argument('-v', dest="version", type=str, help='Name of version (e.g o1, o2, s0, s1, s2, s3, s4)', required=True)
args = parser.parse_args()
node0 = "tnw39@amd015.utah.cloudlab.us"
for x in range (2):
    print(f"Iteration {x}")
    print(f"Starting T-rex")
    os.system("nohup sudo ./t-rex-64 -i -c 14 > log.txt &")
    time.sleep(100)
    with open('log.txt') as f:
        if 'ERROR encountered while configuring TRex system' in f.read():
            print("Error while starting Trex")
            break
    print(f"Loading xdp...")
    os.system(f"ssh -p 22 {node0} 'python3 -u load_xdp.py {args.version.upper()}; exit'")
    time.sleep(10)
    print("Running MLFFR")
    os.system(f"python3 -u mlffr.py -d {args.directory} -v {args.version} -r {x} -mS 1.3 -mE 1.45 -i 0.01")

    print("Unloading xdp")
    os.system(f"ssh -p 22 {node0} 'python3 unload_xdp.py; exit'")
    print("Stopping T-rex and all its children")
    os.system("sudo pkill t-rex")
    time.sleep(100)
print("DONE")