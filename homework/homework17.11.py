import os
import re


def go_for_a_walk(directory):
    rootlist, dirlist, filelist = [], [], []
    for root, dirs, files in os.walk(directory):
        rootlist.append(root)
        dirlist.append(dirs)
        filelist.append(files)
    return rootlist, dirlist, filelist


def how_deep(rootlist):
    maxdeep = 0
    for root in rootlist:
        deep = root.count("\\")
        if deep > maxdeep:
            maxdeep = deep
    return str(maxdeep)


def russian_folders(dirlist):
    counter = 0
    for dirs in dirlist:
        for folder in dirs:
            if re.search("^[А-Яа-я ]+$", folder) is not None:
                counter += 1
    return counter


def extension_freq(filelist):
    ext = []
    for files in filelist:
        for file in files:
            ext.append(re.search("(.[A-Za-z]+)$", file).group(1))
    maxcount = (0, "")
    singext = set(ext)
    for extension in singext:
        counter = ext.count(extension)
        if counter > maxcount[0]:
            maxcount = (counter, extension)
    return maxcount[1]


def initial_freq(dirlist):
    letters = []
    for dirs in dirlist:
        for directory in dirs:
            letters.append(re.search("^(.)?", directory).group(1))
    singlet = set(letters)
    maxcount = (0, "")
    for let in singlet:
        counter = letters.count(let)
        if counter > maxcount[0]:
            maxcount = (counter, let)
    return maxcount[1]


def filename_count(filelist):
    allfiles = []
    for files in filelist:
        for file in files:
            allfiles.append(re.sub("(.[A-Za-z]+)$", "", file))
    filenames = set(allfiles)
    return len(filenames)


def sameoldextension_count(filelist):
    n = 0
    ext = []
    counter = 0
    while n < len(filelist):
        for file in filelist[n]:
            ext.append(re.search("(.[A-Za-z]+)$", file).group(1))
        if len(set(ext)) != len(ext):
            counter += 1
        ext = []
        n += 1
    return counter


def folderfile_count(rootlist, filelist):
    n = 0
    longest = 0
    papkaname = ""
    while n < len(rootlist):
        length = len(filelist[n])
        if length > longest:
            papkaname = rootlist[n]
            longest = length
        n += 1
    return papkaname


def write_it_all(resultlist):
    with open("homework17.11_results.txt", "w+", encoding="utf-8") as f:
        f.write("\n".join(str(r) for r in resultlist))


if __name__ == "__main__":
    directory = "."
    results = []
    listroot, listdir, listfile = go_for_a_walk(directory)
    results.append(how_deep(listroot))
    results.append(russian_folders(listdir))
    results.append(extension_freq(listfile))
    results.append(initial_freq(listdir))
    results.append(filename_count(listfile))
    results.append(sameoldextension_count(listfile))
    results.append(folderfile_count(listroot, listfile))
    write_it_all(results)
