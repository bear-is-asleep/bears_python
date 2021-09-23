import matplotlib.pyplot as plt
import os
from datetime import date

def use_science_style():
  plt.style.use('science')

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
