import pandas as pd 
import matplotlib.pyplot as plt
import os 
import argparse 

def avg_latency(directory, benchmark, gtype):
    if not gtype in ["max", "min", "avg"]:
        print("Wrong type")
        exit(0)
    df = pd.DataFrame()
    file = pd.read_csv(f'{directory}/MLFFR_o1_{gtype}L.txt', index_col=0)
    df["index"] = list(file.index)
    df.set_index("index", inplace=True)
    versions = ["k0", "k1", "k2", "k3", "k4", "o1","o2"]
    for i in versions:
        file = pd.read_csv(f'{directory}/MLFFR_{i}_{gtype}L.txt', index_col=0)
        file['mean'] = file.mean(axis=1)
        #print(file)
        df[i] = file['mean']
    #print(df)
    df.to_csv(f"{directory}/{gtype}L-data.csv")
    fig = plt.figure()
    plt.plot(df, marker="o")                      
    plt.title(f'Measuring {benchmark} AVG Latency')
    plt.xlabel('TX rate (Mpps)',)
    plt.ylabel('Latency (µs)')
    plt.legend(df.columns)
    savePath = f'{directory}/{gtype}L/'
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    fig.savefig(f'{savePath}/avg.png', bbox_inches='tight')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Information about Data')
    parser.add_argument('-d', dest="directory", type=str, help='Directory', required=True)
    parser.add_argument('-b', dest="benchmark", type=str, help='Benchmark', required=True)
    parser.add_argument('-type', dest="gtype", type=str, help='max, min or avg', required=True)
    args = parser.parse_args()
    avg_latency(args.directory, args.benchmark, args.gtype)