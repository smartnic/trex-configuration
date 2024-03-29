#!/usr/bin/env bash
if [[ ("$#" -ne 2 && "$#" -ne 1) ]]; then
    echo "Illegal number of parameters. Run with ./setup_dut.sh <receiving interface> <sending interface>. If both are the same, just send in one interface."
    exit 
fi
read -p "Enter Device type (d6515 or xl170):" device
sudo bash -c "echo $device > ./scripts/device.config"
cd ../
sudo apt-get update
sudo apt-get install linux-tools-common # for bpftool
sudo apt-get install sysstat # for mpstat
sudo apt-get install htop # generally useful
sudo apt-get install linux-tools-5.4.0-51-generic linux-cloud-tools-5.4.0-51-generic linux-tools-generic linux-cloud-tools-generic
sudo apt install python3-pip
sudo pip3 install matplotlib
sudo pip3 install pandas
sudo pip3 install numpy
echo "Setting up configurations"
for var in "$@"
do
    sudo ifconfig $var mtu 3498
done
sudo ethtool --set-priv-flags $1 rx_striding_rq off
sudo ethtool -G $1 rx 256
cd trex-configuration/
echo "Running RSS"
sudo ./rss.sh $1
echo "Running IRQ"
sudo ./irq.sh $1
cd ../
echo "DONE"