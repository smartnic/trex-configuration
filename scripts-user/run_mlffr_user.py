import os
import time 
import sys
import argparse 
from os.path import expanduser

default_ranges = {
    "xdp1": (17,19,0.1),
    "xdp_map_access": (14.6,16,0.1),
    "xdp_redirect": (1,30,1),
}
startTime = time.time()
benchmarks = ["xdp1", "xdp_map_access", "xdp_redirect"]
parser = argparse.ArgumentParser()
parser.add_argument('-b', dest="benchmark", type=str, help=f"Benchmark {str(benchmarks)}", required=True)
parser.add_argument('-d', dest="directory", type=str, help='Directory', required=True)
parser.add_argument('-v', dest="version", type=str, help='Name of version (e.g o1, o2, k0, k1, k2, k3, k4)', required=False)
parser.add_argument('-n', dest="number", type=int, help='Number of times each version should run', default=5)
parser.add_argument('-c', dest="cores", type=int, help='Number of cores', default=14)
parser.add_argument('-mS', dest="start", type=int, help='Start Mpps')
parser.add_argument('-mE', dest="end", type=int, help='End Mpps')
parser.add_argument('-i', dest="increment", type=int, help='Increment Mpps')

args = parser.parse_args()
versionList = []
if (args.version):
    versionList.append(args.version)
else:
    versionList = ["o1", "o2", "k0", "k1", "k2", "k3", "k4"]
if (not args.benchmark in benchmarks):
    print(f"Invalid benchmark name. {str(benchmarks)}")
if not args.start:
    start = default_ranges[args.benchmark][0]
else:
    start = args.start
if not args.end:
    end = default_ranges[args.benchmark][1]
else:
    end = args.end
if not args.increment:
    increment = default_ranges[args.benchmark][2]
else:
    increment = args.increment
# Read node0 configuration
f = open("node0.config", "r")
node0 = f.read()
node0 = node0.strip('\n')
f.close()
print(f"Starting T-rex")
os.system(f"nohup sudo ./t-rex-64 -i -c {args.cores} > $HOME/log.txt &")
time.sleep(60)
home = expanduser("~")
with open(f'{home}/log.txt') as f:
    if 'ERROR encountered while configuring TRex system' in f.read():
        print("Error while starting Trex")
        exit(0)
for x in range (args.number):
    print(f"Iteration {x}")
    for v in versionList:
        print(f"Running {v}")
        print("MLFFR...")
        os.system(f"python3 -u mlffr_user.py -b {args.benchmark} -d {args.directory} -v {v} -r {x} -mS {start} -mE {end} -i {increment} -rx 0")
        time.sleep(10)

print("Stopping T-rex and all its children")
os.system("sudo pkill t-rex")
time.sleep(200)
endTime = time.time()
print(f"Total Time: {endTime-startTime}")
print("Completed Full Script")