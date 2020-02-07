#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0
(Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

import urllib.request
import re
import sys
import os


def read_urls(filename):
    with open(filename, 'r') as animal:
        tmp_str = '\n'
        read_log_file = tmp_str.join(animal.readlines())
        print("Read log file--->", read_log_file)

    # Поиск URL
    # url_match = re.findall(r" /\S+", read_log_file, re.M) #work is good
    url_match = re.findall(r"/\S+\w+-\w+.jpg", read_log_file, re.M)
    modern_url_match = list(set(url_match))
    str_http = 'http://code.google.com'
    img_urls = []
    while len(modern_url_match) != 0:
        url_pop = modern_url_match.pop()
        img_urls.append(str_http + url_pop)
        if len(modern_url_match) == 0:
            return sorted(img_urls, key=sort_col)


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """

    if os.path.exists(dest_dir):
        print(os.environ)
        with open('D:\Ex_GooglePython\My_solution\log_puzzle\dowload_urls\index.html', 'w+') as f:
            f.write("<verbatim>\n<html>\n<body>\n<img src='img0.jpg'><img\nsrc='img1.jpg'><img\nsrc='img2.jpg'><img\n"
                    "src='img3.jpg'><img\nsrc='img4.jpg'><img\nsrc='img5.jpg'><img\nsrc='img6.jpg'><img\n"
                    "src='img7.jpg'><img\n"
                    "src='img8.jpg'><img\nsrc='img9.jpg'><img\nsrc='img10.jpg'><img\nsrc='img11.jpg'><img\n"
                    "src='img12.jpg'><img\n"
                    "src='img13.jpg'><img\nsrc='img14.jpg'><img\nsrc='img15.jpg'><img\nsrc='img16.jpg'><img\n"
                    "src='img17.jpg'><img\n"
                    "src='img18.jpg'><img\nsrc='img19.jpg'></body>\n</html>")
        print('Dir is exist')
        # do not create catalod and crerate html

    else:
        print('This dir is not exist')
        # create catalog
        os.mkdir(dest_dir)
        with open('D:\Ex_GooglePython\My_solution\log_puzzle\dowload_urls\partC\index.html', 'w+') as f:
            f.write("<verbatim>\n<html>\n<body>\n<img src='img0.jpg'><img\nsrc='img1.jpg'><img\nsrc='img2.jpg'><img\n"
                    "src='img3.jpg'><img\nsrc='img4.jpg'><img\nsrc='img5.jpg'><img\nsrc='img6.jpg'><img\n"
                    "src='img7.jpg'><img\n"
                    "src='img8.jpg'><img\nsrc='img9.jpg'><img\nsrc='img10.jpg'><img\nsrc='img11.jpg'><img\n"
                    "src='img12.jpg'><img\n"
                    "src='img13.jpg'><img\nsrc='img14.jpg'><img\nsrc='img15.jpg'><img\nsrc='img16.jpg'><img\n"
                    "src='img17.jpg'><img\n"
                    "src='img18.jpg'><img\nsrc='img19.jpg'><img\nsrc='img20.jpg'><img\nsrc='img21.jpg'><img\n"
                    "src='img22.jpg'><img\nsrc='img23.jpg'><img\nsrc='img24.jpg'><img\n"
                    "src='img25.jpg'><img\nsrc='img26.jpg'><img\nsrc='img27.jpg'><img\n"
                    "src='img28.jpg'><img\nsrc='img29.jpg'><img\nsrc='img30.jpg'><img\n"
                    "src='img31.jpg'><img\nsrc='img32.jpg'><img\nsrc='img33.jpg'><img\nsrc='img34.jpg'><img\n"
                    "src='img35.jpg'><img\nsrc='img36.jpg'><img\nsrc='img37.jpg'><img\nsrc='img38.jpg'><img\n"
                    "src='img39.jpg'><img\nsrc='img40.jpg'><img\nsrc='img41.jpg'><img\nsrc='img42.jpg'><img\n"
                    "src='img43.jpg'><img\nsrc='img44.jpg'><img\nsrc='img45.jpg'><img\nsrc='img46.jpg'><img\n"
                    "</body>\n</html>")
    i = 0
    for each_url in img_urls:
        print('dowload process', each_url)
        urllib.request.urlretrieve(each_url,
                                   filename=r'D:\Ex_GooglePython\My_solution\log_puzzle\dowload_urls\partC\img{}.jpg'.format(str(i)))
        i += 1


def sort_col(k):
    s = re.search(r'-\w+.jpg', k, re.M)
    ss = s.group()

    return list(ss)

# l = ['p-bjag-badf.jpg', 'p-bgcf-bbef', 'p-bjbd-bbbf', 'p-baac-baae']
# print(read_urls('place_code.google.com'))
# print(sorted(l, key=sort_col))
# #print(sort_col(k))

#download_images(read_urls('place_code.google.com'), r'A:\PyCharm\lessons_niit\log_puzzle\partC')
#download_images(read_urls('animal_code.google.com'), r'A:\PyCharm\lessons_niit\log_puzzle')

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
