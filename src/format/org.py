import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import date

plt.style.use('presentation.mplstyle')

#Organization
def make_plot_dir():
    day = date.today().strftime("%d_%m_%Y")
    isDir = os.path.isdir("Plots/Plots_"+day)
    if isDir == False: 
        os.system("mkdir -p Plots_" +day)
        os.system("mv -n Plots_" +day+"/ Plots/")

def save_plot(fname):
    day = date.today().strftime("%d_%m_%Y")
    plt.savefig(fname,bbox_inches = "tight")
    os.system("mv " + fname + "* Plots/Plots_" +day+"/")
