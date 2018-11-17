import os
import re


def folder_deepness(directory):
    for root, dirs, files in os.walk(directory):
        deep = root.count("\\")
        maxdeep = 0
        if deep > maxdeep:
            maxdeep = deep
    return maxdeep


def russian_folders(directory):
    counter = 0
    for root, dirs, files in os.walk(directory):
        for folder in dirs:
        if re.search("^[А-Яа-я ]+$", folder) is not None:
            counter += 1
    return counter

def extension_freq(directory):
    ext = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            ext.append(re.search("(.[A-Za-z]+)$", file).group(1))
    maxcount = (0 , "")
    singext = set(ext)
    for extension in singext:
        counter = ext.count(extension)
        if counter > maxcount[0]:
            maxcount = (counter, extension)
    return maxcount[1]

def initial_freq(directory):
    for root, dirs, files in os.walk(directory):



