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

home = "/root"
os.system("rm ~/katran/_build/deps/bpfprog/bpf/balancer_kern.o")
os.chdir(f"{home}/throughput-experiments")

if "k" in args.version.lower():
    os.system(f"sudo cp {programs[args.benchmark][1]}/top-progs/{programs[args.benchmark][0]}{number}.o {home}/katran/_build/deps/bpfprog/bpf/balancer_kern.o")
else:
    os.system(f"sudo cp {args.version.upper()}/{programs[args.benchmark][0]}.o {home}/katran/_build/deps/bpfprog/bpf/balancer_kern.o")