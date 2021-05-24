echo "Getting Device Under Test"
read -p "Enter DUT as (username@machine):" input
read -p "Enter Device type (d6515 or xl170):" device
cd ../
wget --no-check-certificate --no-cache https://trex-tgn.cisco.com/trex/release/v2.87.tar.gz
tar -xzvf v2.87.tar.gz
sudo pip3 install numpy
sudo pip3 install pandas
sudo cp  trex-configuration/trex_cfg_$device.yaml /etc/trex_cfg.yaml
cd v2.*
sudo ./dpdk_setup_ports.py -s
sudo rm stl/udp_for_benchmarks.py
cd ../
sudo cp  trex-configuration/udp_for_benchmarks_$device.py v2.87/stl/udp_for_benchmarks.py
sudo bash -c "echo $input > v2.87/node0.config"
sudo cp trex-configuration/scripts/mlffr.py v2.87/
sudo cp trex-configuration/scripts/run_mlffr.py v2.87/
sudo cp trex-configuration/scripts-user/mlffr_user.py v2.87/
sudo cp trex-configuration/scripts-user/run_mlffr_user.py v2.87/
# echo "Generating Public Key:"
# ssh-keygen
# cat $HOME/.ssh/id_rsa.pub