cd ~
sudo apt-get update
sudo apt-get install linux-tools-common # for bpftool
sudo apt-get instal sysstat # for mpstat
sudo apt-get install htop # generally useful
sudo apt-get install linux-tools-5.4.0-51-generic linux-cloud-tools-5.4.0-51-generic linux-tools-generic linux-cloud-tools-generic
cd /proj/heartbeat-PG0/linux
echo "Setting up configurations"
sudo ifconfig ens3f0 mtu 3498
sudo ifconfig ens3f1 mtu 3498
sudo ethtool --set-priv-flags ens3f0 rx_striding_rq off
sudo ethtool -G ens3f0 rx 256
cp $HOME/trex-configuration/scripts/load_xdp.py $HOME/
cp $HOME/trex-configuration/scripts/unload_xdp.py $HOME/
echo "DONE"