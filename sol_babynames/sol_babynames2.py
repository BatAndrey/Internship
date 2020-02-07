#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'r')as file:
        tmp_str = ''
        baby_str = tmp_str.join(file.readlines())
    print('------OK---------')

    # Поиск всех имен
    match_obj_name = re.findall(r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>", baby_str)
    name_list = match_obj_name  # Список кортежей типа [(ранг, имя, имя), (...)]

    # Поиск года
    match_obj_year = re.search(r'Popularity\sin\s(\d\d\d\d)', baby_str)
    year_list = list(match_obj_year.groups())

    modern_name_list = []
    f_list_modern = []
    k = []

    for coil in name_list:
        # coil представляет собой кортеж (ранг, имя, имя)

        modern_name_list.append(list(coil))
        # modern_name_list представляет собой список из [ранг, имя, имя]

    for item in modern_name_list:
        # item представляет собой список из [ранг, имя, имя]

        f_list1 = item[1] + ' ' + item[0]  # is str
        f_list2 = item[2] + ' ' + item[0]  # is str
        f_list_modern.extend([f_list1.split('%d') + f_list2.split('%d')])  # is list
    for each in f_list_modern:
        k.extend(each)
    # print(year_list + sorted(k))
    return year_list + sorted(k)

# extract_names('baby2006.html')


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    # filename = ''
    if args[0] == '--summaryfile':
        summary = True
        filename = args[1]
        extract = extract_names(filename)
        text = '\n'.join(extract[0:10:1]) + '\n'
        # print(text)
        # print(extract_names(filename))
        with open('new_file.txt', 'a') as file_write:
            # baby_name = extract_names('baby2006.html')
            file_write.write(text + '\n')
        # if summary == True:
        #     for filename in args:
        #         f = open('baby.html.summary', 'a')
        #         f.write('ppp')
        #         f.close()
        del args[0:2]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file


if __name__ == '__main__':
    main()
