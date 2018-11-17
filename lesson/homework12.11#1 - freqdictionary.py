# n1: обработать mystem ом папку с текстовыми файлами, с помощью regexp создать частотный словарь лемм и POS (no pymyst)

import os
import re


def analyze_run(filename):
    os.system(r'C:\Users\"Lorenzo Tosi"\.local\bin\.\mystem.exe {} {}-tag.txt -id'.format(filename, filename.rstrip(".txt")))


if __name__ == "__main__":
    filename = r'C:\Users\"Lorenzo Tosi"\.local\bin\eseninpoems.txt'
    analyze_run(filename)
