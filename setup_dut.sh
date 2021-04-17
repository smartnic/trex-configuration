if [[ ("$#" -ne 2 && "$#" -ne 1) ]]; then
    echo "Illegal number of parameters. Run with ./setup_dut.sh <receiving interface> <sending interface>. If both are the same, just send in one interface."
    exit 
fi
cd ~
sudo apt-get update
sudo apt-get install linux-tools-common # for bpftool
sudo apt-get install sysstat # for mpstat
sudo apt-get install htop # generally useful
sudo apt-get install linux-tools-5.4.0-51-generic linux-cloud-tools-5.4.0-51-generic linux-tools-generic linux-cloud-tools-generic
echo "Setting up configurations"
for var in "$@"
do
    sudo ifconfig $var mtu 3498
done
sudo ethtool --set-priv-flags $1 rx_striding_rq off
sudo ethtool -G $1 rx 256
cp $HOME/trex-configuration/scripts/load_xdp.py $HOME/
cp $HOME/trex-configuration/scripts/unload_xdp.py $HOME/
echo "Running RSS"
sudo ./$HOME/trex-configuration/rss.sh $1
echo "Running IRQ"
sudo /$HOME/trex-configuration/irq.sh $1
echo "DONE"