"""
The program translate image to minecraft block map

@author: Tang142857
@project: workspace
@file: img2block.py
@date: 2021-06-30
Copyright(c): DFSA Software Develop Center
"""

import cv2
import numpy

import translator
import entry


def read_image(img_path: str, **kwargs):
    """
    Return the bit map of the image
    kwargs:
        ch:r,g,b,a,o
        resize:not use right now
    """
    origin_img = cv2.imread(img_path)
    # pay attention here ,there is BGR not RGB
    rgb_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2RGB)

    block_map = translator.translate_img(rgb_img)
    map = numpy.array(block_map, dtype=numpy.uint8)
    map = cv2.cvtColor(map, cv2.COLOR_RGB2BGR)
    block_map = translator.translate_img(rgb_img, False)

    cv2.imshow('block_map', map)
    cv2.imshow('origin_map', origin_img)
    cv2.waitKey()
    return block_map


if __name__ == '__main__':
    bm = read_image('/home/tang/file/download/pages/cpc.jpeg')
    # bm = read_image('/home/tang/file/pictures/non-human/non-cover.jpg')
    commands = translator.build_command(bm)
    entry.exe_lines(commands)
