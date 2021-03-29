# trex-configuration

## Steps to configure trex K2 testing setup 

On node1:
1) Clone repository `git clone https://github.com/smartnic/trex-configuration.git`
2) cd trex-configuration
3) Run dependencies `./install-dependencies.sh`
4) `sudo dracut -f`
5) `sudo reboot`
6) cd trex-configuration
7) Install T-Rex `./install-trex.sh`
8) Add `export PYTHONPATH = $HOME/v2.87/automation/trex_control_plane/interactive` to profile 
9) Generate SSH key `ssh-keygen` and add it to cloudlab (takes a while before it comes into effect)

On node0:
1) Clone repository `git clone https://github.com/smartnic/trex-configuration.git`
2) cd trex-configuration
3) `./setup_dut.sh`
4) `cd ~`
5) `git clone https://github.com/smartnic/throughput-experiments.git`
6) cd throughput-experiments
7) Edit load_and_run.sh depending on which program you want to run 

## Steps to Run 
1) Start Trex on Node1:  `cd v2.87; sudo ./t-rex-64 -i -c 14`
2) Load XDP program: `./load_and_run.sh`
3) Start MLFFR: `cd v2.87; python3 mlffr.py`
