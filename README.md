# trex-configuration

## Steps to configure trex K2 testing setup 

On node1:
1) Clone repository `git clone https://github.com/smartnic/trex-configuration.git`
2) cd trex-configuration
3) Run dependencies `./install-dependencies.sh`
4) `sudo dracut -f`
5) `sudo reboot`
6) cd trex-configuration
7) Install T-Rex `./install-trex.sh`. Enter the DUT machine.
8) Add outputted key to cloudlab.
9) Add `export PYTHONPATH=$HOME/v2.87/automation/trex_control_plane/interactive` to profile 


On node0:
1) Clone repository `git clone https://github.com/smartnic/trex-configuration.git`
2) cd trex-configuration
3) `./setup_dut.sh`
4) `cd ~`
5) `git clone https://github.com/smartnic/throughput-experiments.git`
6) cd throughput-experiments
7) Edit load_and_run.sh depending on which program you want to run 

## Scripts

### Run all versions  
`python3 run_mlffr_no_stop.py -d $directory`
*Note: Takes several hours to run*

### Run a specific version 
`python3 run_mlffr_no_stop.py -d $directory -v o1`  
*Note: Takes about 3 minutes per run and ~20 for a set of 5 runs*

### Run with manual loading
1) Start Trex on Node1:  `cd v2.87; sudo ./t-rex-64 -i -c 14`
2) Load XDP program: `./load_and_run.sh`
3) Start MLFFR: `cd v2.87; python3 mlffr.py -d $directory -v $version`

### Run through t-rex console
**Node 1 (Traffic Generator):**
`cd MLNX_OFED_LINUX-5.0-2.1.8.0-rhel7.8-x86_64/v2.87/`
Start the t-rex on node 1: `sudo ./t-rex-64 -i -c 14`  

**Node 0 (Device Under Test):**
Load Sample xdp Programs
Load xdp_fwd = `sudo ./samples/bpf/xdp_fwd ens3f0 ens3f1`
Load xdp_rxq = 
`sudo ./samples/bpf/xdp_rxq_info --dev ens3f0 --action XDP_DROP`
`sudo ./samples/bpf/xdp_rxq_info --dev ens3f0 --action XDP_TX --swapmac`
Detach xdp_fwd = `sudo ./xdp_fwd -d ens3f0 ens3f1`  

**Node 1 (Traffic Generator):**
`cd MLNX_OFED_LINUX-5.0-2.1.8.0-rhel7.8-x86_64/v2.87/`  
`./trex-console`  
`tui`  
`start -f stl/udp_for_benchmarks.py -t packet_len=64,stream_count=2 --port 0 -m 148mpps # you might have to do stl/`

Note: To open latency statistics in the traffic generator console press ESC then L .

## Device Under Test Configurations

| Command | Description |
| --- | --- |
| `sudo ./rss.sh <receive interface>` | Linux Receive Side Scaling | 
| `sudo ./irq.sh <recieve interface>` | IRQ Affinities for NIC receive queues |
| `sudo ethtool --set-priv-flags <recieve interface> rx_striding_rq off` | PCIe descriptor compression |
| `sudo ifconfig <recieve interface> mtu 3498; sudo ifconfig <send interface> mtu 3498; ` | Maximum MTU for Mellanox Driver to support BPF |
| `sudo ethtool -G <recieve interface> rx 256`| RX descriptor ring size for the NIC |
