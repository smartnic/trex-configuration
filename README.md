# Performance Experiments

This repository was used to evaluate K2. The following README demonstrates how to setup the evaulation setup in cloudlab. 

## Setup 

Estimate Time: 20 minutes

### Step 1: Create Experiment

Visit https://cloudlab.us/ and click the "Log in" button. You can use the reviewer account details (CloudLab account username and password provided in our SIGCOMM21 artifact hotCRP submission) to log into the CloudLab console.

#### Step 1.1: Start Experiment 
<img src="instruction-images/start.png" width="700px" />

#### Step 1.2: Change Profile
<img src="instruction-images/change-profile.png" width="700px" />

#### Step 1.3: Select k2-performance-xl170 Profile
<img src="instruction-images/save-profile.png" width="700px" />

#### Step 1.4: Name Experiment (optional)
<img src="instruction-images/name-expr.png" width="700px" />

#### Step 1.5: Start or Schedule Experiment
You can choose to start the experiment right away (just click "Finish" in the screen below) or schedule it to start at some time in the future. 

The default/initial duration for which an experiment may run (i.e., the time that the machines will be available to you) is 16 hours. You can extend an experiment later after the experiment boots up.

<img src="instruction-images/schedule.png" width="700px" />

##### You may encounter the following failures/slow cases: 

Sometimes, starting an experiment can fail when CloudLab has insufficient resources available. If your experiment fails due to insufficient resources, you can check for future resource availability at https://www.cloudlab.us/resinfo.php -- look for future availability of machine instances of type "xl170" in the Utah cluster. You need at least 2 available machines for our experiment. You can also make reservations for machines at a future time by following instructions from http://docs.cloudlab.us/reservations.html. Please contact us if you have any difficulty.

If your experiment is successfully scheduled, it might still keep you waiting with the message `Please wait while we get your experiments ready`. This can happen sometimes since we use a custom disk image.

Contact us or the CloudLab mailing list (https://groups.google.com/g/cloudlab-users) if you have any difficulties.

### Step 2: Setup The Nodes
#### Step 2.1: Update Node 1 Configurations
1) SSH into node-1.  You can determine the name of the node-1 and node-0 machines from the CloudLab console (go to "list view" once the experiment is ready)
 
 <img src="instruction-images/cloudlab-listview.png" width="700px">
 
 You must use the private key and key password provided as part of our hotCRP submission to login into the machine labeled node-1 (`hp060.utah.cloudlab.us` in our example above). Suppose you've named the file containing the private key (from hotCRP) `my.key`.  You will then type
 
 ```
 ssh -p 22 -i my.key reviewer@hp060.utah.cloudlab.us
 ```

You will need to type in the key password provided on hotCRP.
 
3) Once logged into node-1, use your favorite text editor to add the line 
   ```export PYTHONPATH=/usr/local/v2.87/automation/trex_control_plane/interactive``` 
   to ~/.bash_profile.
4) `cd /usr/local/trex-configuration/`
5) Run ./update-scripts.sh. When prompted, enter the following details for your experiment. The user@DUT (device under test) string is `reviewer@<insert node-0 name you found above>` and the device type should be `xl170`. A complete run might look like the following:

```
reviewer@node-1 trex-configuration]$ ./update-scripts.sh 
Setting up some information
Enter DUT as (username@machine):reviewer@hp073.utah.cloudlab.us
Enter Device type (d6515 or xl170):xl170
```

6) Exit the session and login again. 
 
#### Step 2.2: Create SSH Key
1) Generate ssh key. `ssh-keygen`  (press enter for all the prompts)
2) Add SSH key into Cloudlab

 <img src="instruction-images/create-ssh.png" width="300px"> <img src="instruction-images/add-key.png" width="500px" >
 
4) Wait 5-10 minutes. Cloud lab takes a bit of time to update your ssh key. Then, test ssh into the node0 from node 1. This step is necessary, do not skip!

#### Step 2.3: Update Node0 Configurations
1) SSH into Node0
2) `./setup_dut.sh ens1f1`. Type in Y when it prompts and enter xl170 when it prompts for a device.

## Exercises
*Note: All DATA and logs, graphs are saved in your home directory*

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
