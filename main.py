# Import Packages
import easygui
import psutil
import sys
import linecache
import os
import datetime


# Set Variables to Global
global Directory
global CpuTestLength
global MemoryUsage
global CpuUsage
global DiskUsage


# Loads all the settings from the config file
def LoadConfig():
    global Directory
    global CpuTestLength
    Directory = linecache.getline(r"Config.txt", 2).rstrip('\n')
    CpuTestLength = linecache.getline(r"Config.txt", 4).rstrip('\n')
    print("Loaded Current Config Settings!")
    print("Directory: " + str(Directory))
    print("CPU Test Length: " + CpuTestLength + " Seconds")


def HardwareStats():
    global MemoryUsage
    global CpuUsage
    global DiskUsage
    global Directory
    global CpuTestLength
    CpuUsage = psutil.cpu_percent(int(CpuTestLength))
    MemoryUsage = psutil.virtual_memory()[2]
    print(CpuUsage)
    print(MemoryUsage)

def SaveData():
    current_time = datetime.datetime.now()
    FileName = str(current_time.year) + "-" + str(current_time.month) + "-" + str(current_time.day)
    if Directory[-1] != '\\':
        Directory += "\\"
    os.mkdir(Directory + FileName)
    # I was planning to make a new folder, save all the data into a text file, copy the logs, include a copy of the config file,
    # and the script version number than zip it and send it to the client computer with the date it was taken as the file name.

SaveData()
LoadConfig()
HardwareStats()


