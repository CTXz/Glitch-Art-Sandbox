# Copyright (c) 2017 Patrick Pedersen <ctx.xda@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Just a bunch of code that lets me make glitch stuff

import os
import PIL
import operator
import math
import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def tile(background, image, pos, angle, by, offset=1):
    for i in range(0, by + 1, 1):
        background.paste(image, tuple(map(operator.add, pos, (int((i * offset) * math.cos(math.radians(angle))), int((i * offset) * math.sin(-math.radians(angle)))))))

def horizontalStretch(image, box, row = None):
    if row == None:
        row = box[1]

    px = image.load()
    for y in range(box[1], box[3]):
        for x in range(box[0], box[2]):
            px[x,y] = px[x, row]

def verticalStrech(image, box, colon = None):
    if colon == None:
        colon = box[0]

    px = image.load()
    for x in range(box[0], box[2]):
        for y in range(box[1], box[3]):
            px[x,y] = px[colon, y]

def fillWithRow(im, row):
    crop = im.crop((0, row-1, im.size[0], row))

    for i in range(0, im.size[1]):
        im.paste(crop, (0, i))

def fillWithColon(im, colon):
    crop = im.crop((colon - 1, 0, colon, im.size[1]))

    for i in range(0, im.size[0]):
        im.paste(crop, (i, 0))

def addPlayButton(im, size = 50):
    d = ImageDraw.Draw(im)
    d.text((30, 30), "PLAY", (255, 255, 255), ImageFont.truetype(os.getenv("HOME") + "/.local/share/fonts/VCR_OSD_MONO_1.001.ttf", size))

def tunnel(im, box, by, offset=1, bias_x = 0, bias_y = 0):
    crop = im.crop(box)

    if by == -1:

        i = 0

        w = crop.size[0] - i*offset
        h = crop.size[1] - i*offset

        while w > 0 and h > 0:
            resize = crop.resize((w, h))
            crop.paste(resize, (int((crop.size[0] - resize.size[0])/2) + bias_x, int((crop.size[1] - resize.size[1])/2) + bias_y))

            i += 1

            w = crop.size[0] - i*offset
            h = crop.size[1] - i*offset


    for i in range(0, by):
        resize = crop.resize((crop.size[0] - i*offset, crop.size[1] - i*offset))
        crop.paste(resize, (int((crop.size[0] - resize.size[0])/2) + bias_x, int((crop.size[1] - resize.size[1])/2) + bias_y))

    im.paste(crop, (box[0], box[1]))

def pixelatedStretch(im, count, max_rect, min_rect=(20, 20), honly=False, vonly=False):
    for i in range(0, count):
        w = random.randint(min_rect[0], max_rect[0])
        h = random.randint(min_rect[1], max_rect[1])

        x = random.randint(0, im.size[0] - w)
        y = random.randint(0, im.size[1] - h)

        pixel = (x, y, x + w, y + h)

        if honly and not vonly or random.randint(0, 1) and not vonly:
            horizontalStretch(im, pixel)
        else:
            verticalStrech(im, pixel)
