from glob import glob
import os
import sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
filepath = filedialog.askdirectory()

files  = glob(os.path.abspath(filepath)+'\\*.csv')
files.sort()

def progressBar(value, endvalue, bar_length=20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '|'
        spaces = ' ' * (bar_length - len(arrow))
        sys.stdout.write('\rProgress: [{0}] {1}%'.format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

for index, file in enumerate(files):
    f = open(os.path.abspath(file),'r' )
    lines = f.readlines()
    f.close()
    
    for i,l in enumerate(lines) :
        if (i==0):
            lines[i] = l.replace('\n', ',filename,index\n')
        else:
            lines[i] = l.replace('\n', ','+os.path.basename(file)+','+str(index+1)+'\n')
    
    if not os.path.exists(os.path.dirname(os.path.abspath(filepath))+'\\extended\\'):
        os.makedirs(os.path.dirname(os.path.abspath(filepath))+'\\extended\\')
    
    outname = os.path.dirname(os.path.abspath(filepath))+'\\extended\\'+os.path.basename(file)
    f2 = open(outname,'w')
    f2.writelines(lines)
    f2.close()
    progressBar(index, len(files), bar_length = 60)
