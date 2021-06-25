#!/usr/bin/env bash
# remove file and copy file 
cd $HOME
cd trex-configuration/katran
python3 -u copy_katran.py -v $1
sleep 10
interface="ens1f1"
export interface
mac_addr="9c:dc:71:49:98:31"
export mac_addr
file="./deps/bpfprog/bpf/balancer_kern.o"
cd $HOME/katran/_build
echo "Starting Katran.  -v6 provides higher debug"
nohup sudo ./build/example_grpc/katran_server_grpc -v 6 -balancer_prog $file -default_mac $mac_addr -hc_forwarding=false -intf=$interface  -lru_size=10000 > ~/log.txt &
sleep 5
cd $HOME/katran
./katran_goclient -A -u 10.200.200.1:1025
sleep 1
for i in $(seq 1 100); do ./katran_goclient -u 10.200.200.1:1025 -a -r 10.0.0.$i; done;
sleep 5
#./katran_goclient -a -u 10.200.200.1:1025 -r 10.10.1.2
#./katran_goclient -l