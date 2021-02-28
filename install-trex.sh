cd ~
wget --no-check-certificate --no-cache https://trex-tgn.cisco.com/trex/release/v2.87.tar.gz
tar -xzvf latest
cd v2.*
sudo cp  $HOME/trex-configuration/trex_cfg.yaml /etc/trex_cfg.yaml
sudo ./dpdk_setup_ports.py -s
