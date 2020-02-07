#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
from zipfile import ZipFile
"""Copy Special exercise
"""
list_file_path = []


def get_special_path(dir):
    """Возвращает список абсолютных путей к специальным файлам в данном каталоге """

    if os.path.exists(dir):
        # dir_work = os.chdir(os.getcwd() + r"\copyspecial")
        # os.listdir(os.chdir(os.getcwd() + r"\copyspecial"))

        for root, directories, files in os.walk(os.getcwd() + r"\copyspecial"):
            # print('root--->', root)
            for directory in directories:
                print('directory---->', directory)
            for file in files:
                # os.path.join(root, file)
                list_file_path.append(os.path.join(root, file))
                # print('file--->', file)
                # print('list_path--->', list_file_path)
        return list_file_path

def copy_to(paths, dir):
    """Учитывая список путей копирует эти файлы в заданный каталог, paths - пути, dir - каталог"""
    for file in list_file_path:
        if os.path.exists(dir):
            shutil.copy(src=file,
                        dst=dir,
                        follow_symlinks=True)
        else:
            os.mkdir(dir)
            shutil.copy(src=file,
                        dst=dir,
                        follow_symlinks=True)


def zip_to(paths, zippath):
    #for dir in list_file_path:
    #print(dir[1], '<----')
    if os.path.exists(paths):
        src = os.path.realpath(r'D:\Ex_GooglePython\My_solution\copyspecial\xyz__hello__.txt')
        print('src', src)
        root_dir, tail = os.path.split(src)
        print('///root_dir---->', root_dir, '///tail--->', tail)
        base_name = zippath + r'\copyarch'
        #base_name = r'D:\Ex_GooglePython\My_solution\copyspecial'
        root_dir = paths
        base_dir = zippath
        shutil.make_archive(base_name=base_name, format='zip', root_dir=root_dir, base_dir=base_dir)

        with ZipFile(r'D:\Ex_GooglePython\My_solution\copyspecial\for_archive\copyarch.zip', 'w') as newzip:
            newzip.write(r'new_file.txt')
            newzip.write(r'text_file.txt')
            newzip.write(r'D:\Ex_GooglePython\My_solution\copyspecial\zz__something__.jpg')
# +++your code here+++
# Write functions and modify main() to call them

# print(get_special_path('D:\Ex_GooglePython\My_solution\copyspecial'))
# #copy_to(list_file_path, r'D:\Ex_GooglePython\My_solution\newcopy')
# zip_to(r'D:\Ex_GooglePython\My_solution\copyspecial', r'D:\Ex_GooglePython\My_solution\copyspecial\for_archive')

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        get_special_path(todir)
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        zip_to(todir, tozip)
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirsssssss")
        sys.exit(1)

    # get_special_path('D:\Упражнения GooglePython\My_solution')
    # copy_to(list_file_path, r'D:\Упражнения GooglePython\My_solution\copyspecial\copy_test')
    # zip_to(r'D:\Упражнения GooglePython\My_solution\copyspecial\copy_test',
    #        r'D:\Упражнения GooglePython\My_solution\copyspecial\copy_test')

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
