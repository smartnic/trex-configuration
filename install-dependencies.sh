#!/usr/bin/env bash
cd ~
wget http://content.mellanox.com/ofed/MLNX_OFED-5.0-2.1.8.0/MLNX_OFED_LINUX-5.0-2.1.8.0-rhel7.8-x86_64.tgz
sudo yum install pciutils createrepo
tar -xvzf MLNX_OFED_LINUX-5.0-2.1.8.0-rhel7.8-x86_64.tgz
cd MLNX_OFED_LINUX-5.0-2.1.8.0-rhel7.8-x86_64
nohup sudo ./mlnxofedinstall --with-mft --with-mstflint --dpdk --upstream-libs --add-kernel-support &
# sudo dracut -f
# sudo reboot