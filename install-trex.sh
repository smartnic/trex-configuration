cd ~
wget --no-check-certificate --no-cache https://trex-tgn.cisco.com/trex/release/v2.87.tar.gz
tar -xzvf v2.87.tar.gz
cd v2.*
sudo cp  $HOME/trex-configuration/trex_cfg.yaml /etc/trex_cfg.yaml
sudo ./dpdk_setup_ports.py -s
rm stl/udp_for_benchmarks.py
sudo cp  $HOME/trex-configuration/udp_for_benchmarks.py stl/
sudo pip3 install pandas
cp scripts/mlffr.py $HOME/v2.87
cp scripts/load_xdp.py $HOME/
cp scripts/unload_xdp.py $HOME/