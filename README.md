# Performance Experiments

This repository was used to evaluate K2. The following README demonstrates how to setup the evaulation setup in cloudlab. 

## Setup 
Please follow the instructions here:
[insert power point here]

## Exercises

### Exercise 1: Run one version of a benchmark that DOES NOT drop packets. 
Estimated Run Time: 30 minutes
1) Change to directory: `cd /usr/local/v2.87`
2) Start run: `nohup python3 -u run_mlffr.py -b xdp_fwd -v o1 -d xdp_fwd/ -n 1 -c 6 &`
3) Check progress of logs `tail -f $HOME/nohup.out`
4) Once it has completed running (it will say *Completed Full Script* in the logs), you will now generate the graphs. 
5) Generate throughput: `python3 rx_plot.py -d ~/xdp_fwd -v O1 -b xdp_fwd -r 0`
6) Generate latency: `python3 latency.py -d ~/xdp_fwd -type avg -v O1 -b xdp_fwd`

### Exercise 2: Run one version of a benchmark that DOES drop packets. 
Estimated Run Time: 30 minutes
1) Change to directory: `cd /usr/local/v2.87`
1) Start run: `nohup python3 -u run_mlffr_user.py -b xdp_map_access -v o1 -d xdp_map -n 1 -c 6 > $HOME/map.txt &`
2) Check progress of logs `tail -f $HOME/map.out`
3) Once it has completed running (it will say *Completed Full Script* in the logs), you will now generate the graphs. 
4) Generate throughput: `python3 generate_user_graphs.py -d ~/xdp_map -v O1 -b xdp_map_access -r 0`

### Exercise 3: Run all versions of a benchmark (that DOES NOT drop packets) three times each. 
Estimated Run time: 6 hours 
1) Change to directory: `cd /usr/local/v2.87`
2) Start run: `nohup python3 -u run_mlffr.py -b xdp_fwd -d xdp_fwd_all -n 3 -c 6 > $HOME/xdp_fwd_log.txt &`
3) Check progress of logs `tail -f $HOME/xdp_fwd_log.out`
4) Once it has completed running (it will say *Completed Full Script* in the logs), you will now generate the graphs. 
5) Generate throughput, drop rate, and latency graphs: `python3 generate_graphs.py -d xdp_fwd_all -b xdp_fwd -r 3`

### Exercise 4: Run all versions of a benchmark (that DOES drop packets) three times each. 
Estimated Run Time: 6 hours 
1) Change to directory: `cd /usr/local/v2.87`
2) Start run: `nohup python3 -u run_mlffr_user.py -b xdp_map_access -d xdp_map_all -n 3 -c 6 > $HOME/map_all.txt &`
3) Check progress of logs `tail -f $HOME/map_all.out`
4) Once it has completed running (it will say *Completed Full Script* in the logs), you will now generate the graphs. 
5) Generate throughput graphs: `python3 generate_user_graphs.py -d ~/xdp_map_all -b xdp_map_access -r 3 -average`

## File Structure