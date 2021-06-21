import os
from os.path import expanduser
import sys
import argparse 

programs = {
    "balancer_kern": ("balancer_kern", "completed-programs/camera_ready/katran_balancer_kern"),
}
parser = argparse.ArgumentParser(description='Information about Data')
parser.add_argument('-b', dest="benchmark", type=str, help=f"Benchmark {str(programs.keys())}", required=False, default="balancer_kern")
parser.add_argument('-v', dest="version", type=str, help='Name of version (e.g O1, O2, K0, K1, K2, K3, K4)', required=True)
args = parser.parse_args()

home = "/usr/local"

os.chdir(f"{home}/throughput-experiments")

number = list(args.version)[1]
if "k" in args.version.lower():
    os.system(f"sudo cp {programs[args.benchmark][1]}/top-progs/{programs[args.benchmark][0]}{number}.o {programs[args.benchmark][0]}.o")
else:
    os.system(f"sudo cp {args.version.upper()}/{programs[args.benchmark][0]}.o .")