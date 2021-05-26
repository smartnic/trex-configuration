import os
import time
from prettytable import PrettyTable


def get_data():
    benchmarks = ["xdp2", "xdp_fw", "xdp_router_ipv4", "xdp_fwd", "xdp_pktcntr"]
    version_list = ["k0", "k1", "k2", "k3", "k4"]

    accept_num_arr = []

    for benchmark in benchmarks:
        accept_num = 0
        if benchmark == "xdp_pktcntr":
            accept_num = -2 # since there are only three versions for xdp_pktcntr
        for version in version_list:
            cmd1 = "sh -c 'python3 -u /usr/local/trex-configuration/safety_chk/load_xdp.py -b " + benchmark + ' -v ' + version + " 1>load_log.txt 2>load_err.txt &' "
            #print(cmd1)
            os.system(cmd1)
            time.sleep(4)
            cmd2 = 'python3 /usr/local/trex-configuration/scripts/unload_xdp.py'
            os.system(cmd2)
            f = open('load_err.txt')
            lines = f.readlines()
            flag = True
            for line in lines:
                if 'failed to load program' in line:
                    flag = False
                    break
            f.close()
            if flag:
                accept_num = accept_num + 1
            os.system("rm -rf load_log.txt load_err.txt")

        accept_num_arr.append(accept_num)

    # ----------------------------------------------------------------
    benchmarks_2 = ["xdp1", "xdp_map_access", "xdp_redirect"]

    for benchmark in benchmarks_2:
        accept_num = 0
        for version in version_list:
            cmd1 = "sh -c 'python3 -u /usr/local/trex-configuration/safety_chk/load_xdp_user.py -b " + benchmark + ' -v ' + version + " -m 0 -r 0 -d 0 &'"
            #print(cmd1)
            os.system(cmd1)
            time.sleep(2)
            cmd2 = 'python3 -u /usr/local/trex-configuration/scripts/unload_xdp.py'
            os.system(cmd2)
            f = open('/users/reviewer/err.txt')
            lines = f.readlines()
            flag = True
            for line in lines:
                if 'failed to load program' in line:
                    flag = False
                    break
            f.close()
            if flag:
                accept_num = accept_num + 1

        accept_num_arr.append(accept_num)
    total_num_arr = [5]*(len(benchmarks)+len(benchmarks_2))
    total_num_arr[4] = 3 # xdp_pktcntr has 3 versions
    benchmarks.extend(benchmarks_2)
    return benchmarks, accept_num_arr, total_num_arr


def print_table(benchmarks, accept_num_arr, total_num_arr):
    table_ins = PrettyTable()
    table_ins.add_column('Benchmark', benchmarks)
    table_ins.add_column('# variants produced', total_num_arr)
    table_ins.add_column('# accepted by kernel checker', accept_num_arr)
    print(table_ins)
    return 0


def sys_main():
    benchmarks, accept_num_arr, total_num_arr = get_data()
    print_table(benchmarks=benchmarks, accept_num_arr=accept_num_arr, total_num_arr=total_num_arr)
    return 0


if __name__ == '__main__':
    sys_main()

