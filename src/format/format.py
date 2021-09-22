import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='medium')
plt.rc('ytick', labelsize='medium')

xls = 14 #xy axis
tls = 18 #Title
lls = 14 #Legend 

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
