wget --no-check-certificate --no-cache https://trex-tgn.cisco.com/trex/release/latest

tar -xzvf latest
cd v2.87
sudo cp  trex_cfg.yaml /etc/trex_cfg.yaml
sudo ./dpdk_setup_ports.py -s
