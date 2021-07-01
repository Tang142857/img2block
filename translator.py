"""
Translator

@author: Tang142857
@project: workspace
@file: translator.py
@date: 2021-07-01
Copyright(c): DFSA Software Develop Center
"""
import numpy
import cv2

DATA = {
    (176, 46, 38): 'red_concrete',
    (94, 124, 22): 'green_concrete',
    (137, 50, 184): 'purple_concrete',
    (22, 156, 156): 'cyan_concrete',
    (157, 157, 151): 'light_gray_concrete',
    (71, 79, 82): 'gray_concrete',
    (243, 139, 170): 'pink_concrete',
    (128, 199, 31): 'lime_concrete',
    (254, 216, 61): 'yellow_concrete',
    (58, 179, 218): 'light_blue_concrete',
    (199, 78, 189): 'magenta_concrete',
    (249, 128, 29): 'orange_concrete',
    (29, 29, 33): 'black_concrete',
    (131, 84, 50): 'brown_concrete',
    (60, 68, 170): 'blue_concrete',
    (249, 255, 254): 'white_concrete'
}


class Color(object):
    def __init__(self, rgb: tuple):
        self.rgb = rgb
        self.length = 0
        self.block_name = ''

    def calc_length(self, competitor: tuple):
        r_length = abs(self.rgb[0] - competitor[0])
        g_length = abs(self.rgb[1] - competitor[1])
        b_length = abs(self.rgb[2] - competitor[2])
        main_length = r_length ** 2 + g_length ** 2 + b_length ** 2
        self.length = main_length

    def __str__(self):
        return str(self.rgb) + self.block_name

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_length(obj):
        return obj.length


def get_closest(src_rgb):
    for color in color_list:
        color.calc_length(src_rgb)
    color_list.sort(key=Color.get_length)
    return color_list[0].rgb


def translate_img(img: numpy.array):
    """Translate a img to block map"""
    block_map = []
    for raw in img:
        raw_map = []
        for cell in raw:
            color_id = tuple(cell)
            raw_map.append(get_closest(color_id))
        block_map.append(raw_map)
    return block_map


color_list = []
for color_code in DATA.keys():
    c = Color(color_code)
    c.block_name = DATA[color_code]
    color_list.append(c)

if __name__ == '__main__':
    # predata = DATA.split('\n')[:-1]
    # dist = []
    # for d in predata:
    #     r, g, b = d[:2], d[2:4], d[4:6]
    #     new_line = f'{int(r,base=16)},{int(g,base=16)},{int(b,base=16)},{d[7:]}\n'
    #     dist.append(new_line)
    # with open('data.log', 'w') as f:
    #     f.writelines(dist)
    print(get_closest((123, 123, 255)))
