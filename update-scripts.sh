echo "Setting up some information"
read -p "Enter DUT as (username@machine):" input
read -p "Enter Device type (d6515 or xl170):" device
cd ../
sudo cp  trex-configuration/trex_cfg_$device.yaml /etc/trex_cfg.yaml
sudo rm v2.87/stl/udp_for_benchmarks.py
sudo cp  trex-configuration/udp_for_benchmarks_$device.py v2.87/stl/udp_for_benchmarks.py
sudo bash -c "echo $input > v2.87/node0.config"
sudo cp trex-configuration/scripts/mlffr.py v2.87/
sudo cp trex-configuration/scripts/run_mlffr.py v2.87/
sudo cp trex-configuration/scripts-user/mlffr_user.py v2.87/
sudo cp trex-configuration/scripts-user/run_mlffr_user.py v2.87/