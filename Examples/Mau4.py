# Copyright (c) 2018 Patrick Pedersen <ctx.xda@gmail.com>
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

import sys
sys.path.append('..')

import Glitch

from PIL import Image

im = Image.open("./Original/Mau5.jpg")
Glitch.horizontalStretch(im, (422, 73, 422 + 160, 73 + 30), 10)
Glitch.horizontalStretch(im, (485, 119, 485 + 39, 119 + 39))

top = 258
copy = 100

for i in range (0, 3):
    tile = im.crop((116, top, 116 + 763, 258 + 351))
    Glitch.tile(im, tile, (116, top), 270, int(copy), 1)

    top += 150 - (i * 50)
    copy /= 2

Glitch.addPlayButton(im, 30)
im.save("./Results/Mau4.jpg")
