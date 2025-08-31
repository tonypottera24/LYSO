import os
import uproot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

colors = np.array(
    [
        "black",
        "tab:blue",
        "tab:orange",
        "tab:green",
        "tab:red",
        "tab:purple",
        "tab:brown",
        "tab:pink",
        "tab:gray",
        "tab:olive",
        "tab:cyan",
        "gold",
        "lime",
        "navy",
        "teal",
        "crimson",
        "darkorange",
        "deepskyblue",
        "orchid",
        "black",
        "magenta",
        "yellow",
        "salmon",
        "chartreuse",
        "dodgerblue",
        "firebrick",
    ]
)


def read_root(fname):
    with uproot.open(fname) as f:
        tree = f["LYSO"]
        # arrays = tree.arrays(["S1", "S2", "S3", "S4", "S5", "S6", "ID"], library="np")
        arrays = tree.arrays(["S1", "S3", "S5", "ID"], library="np")
    df = pd.DataFrame(arrays)
    df["ID"] = df["ID"].astype(int)
    return df


def plot2d(df, x="S1", y="S2", size=1, output_fname="output.png"):
    sgmin = 0.0
    sgmax = 2000.0
    plt.figure(20)
    plt.title(f"{x} signal vs {y} signal")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xlim([sgmin, sgmax])
    plt.ylim([sgmin, sgmax])
    # plt.scatter(s2,s3,marker='.',s=1,linewidths=0)
    sizes = np.full(len(df), float(size))
    plt.scatter(df[x], df[y], c=colors[df["ID"]], s=sizes, marker=".", linewidths=0)
    plt.tight_layout()
    plt.savefig(os.path.join("output", output_fname), dpi=150)
    plt.close()
