import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import filedialog


def plot_columns(file, dom_col):
    """ Plots columns from the file as a 2D line plot
    Args:
        file (string): Route for the file with the columns to plot
        dom_col (int): Specifies which column of the file is the domain. If 0, no domain is used.
    """
    # Read the csv file and create a dataframe
    df = pd.read_csv(file)
    col_names = list(df.columns)

    # Creates the plot axis
    ax = plt.subplot(111)

    # Iterates the dataframe and plots
    if dom_col != 0:
        dom_col -= 1
        domain = df.iloc[:, dom_col]
        domain_name = col_names.pop(dom_col)
        df = df.drop(df.columns[[dom_col]], axis=1)

        for i in range(len(col_names)):
            ax.plot(domain, df[col_names[i]], label=col_names[i], linewidth=len(col_names) - i)
        
        plt.xlabel(domain_name)
        plt.xlim([domain.iloc[0], domain.iloc[-1]])
    else:
        for i in range(len(col_names)):
            ax.plot(df[col_names[i]], label=col_names[i], linewidth=len(col_names) - i)

    # Adds grid, legend ad shows plot
    plt.grid(True)
    ax.legend()
    plt.show()


if __name__ == '__main__':
    # Prompts the user with a basic interface to select a file
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), filetypes = (('csv files','*.csv'),('all files','*.*')))
    root.destroy()

    domain_column = 1   # Column of the CSV file which contains domain. If there is no domain then = 0.
    
    plot_columns(file, domain_column)

    sys.exit()