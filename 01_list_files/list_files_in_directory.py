import os
import sys
import pandas as pd

import tkinter as tk
from tkinter import filedialog

from datetime import datetime


def list_files(directory, ext1, ext2, ext3, ext4):
    files = os.listdir(directory)
    
    ext1_files = []
    ext2_files = []
    ext3_files = []
    ext4_files = []
    other_files = []
    
    for file in files:
        if file.endswith(ext1):
            ext1_files.append(file)
        elif file.endswith(ext2):
            ext2_files.append(file)
        elif file.endswith(ext3):
            ext3_files.append(file)
        elif file.endswith(ext4):
            ext4_files.append(file)
        else:
            other_files.append(file)
    
    return ext1_files, ext2_files, ext3_files, ext4_files, other_files
    

def store_list(directory, title, files):
    data_frame = pd.DataFrame(files)
    data_frame.to_csv(directory + '\\' + title + '.csv')
    

if __name__ == '__main__':
    # Prompts the user with a basic interface to select a folder/directory
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(parent=root, initialdir=os.getcwd())
    dir_name = os.path.basename(directory)

    # Generates the file with a list of the name of the files in the directory
    title = 'Lista_' + dir_name
    ext1_files, ext2_files, ext3_files, ext4_files, other_files = list_files(directory, ext1='.xlsx', ext2='.dwg', ext3='.pdf', ext4='.docx')
    sorted_files = ext1_files + ext2_files + ext3_files + ext4_files + other_files
    store_list(directory, title, sorted_files)

    sys.exit()