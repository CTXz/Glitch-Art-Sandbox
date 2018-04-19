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
