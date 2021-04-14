echo "Getting Device Under Test"
read -p "Enter DUT as (username@machine):" input
read -p "Enter Device type (d6515 or xl170)" device
echo input > $HOME/v2.87/node0.config
cd ~
wget --no-check-certificate --no-cache https://trex-tgn.cisco.com/trex/release/v2.87.tar.gz
tar -xzvf v2.87.tar.gz
cd v2.*
sudo cp  $HOME/trex-configuration/trex_cfg.yaml /etc/trex_cfg.yaml
sudo ./dpdk_setup_ports.py -s
rm stl/udp_for_benchmarks.py
sudo cp  $HOME/trex-configuration/udp_for_benchmarks_$device.py stl/
sudo pip3 install pandas
cp $HOME/trex-configuration/scripts/mlffr.py $HOME/v2.87
cp $HOME/trex-configuration/scripts/run_mlffr.py $HOME/v2.87
echo "Generating Public Key:"
ssh-keygen
cat $HOME/.ssh/id_rsa.pub