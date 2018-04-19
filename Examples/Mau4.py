import sys
sys.path.append('..')

import Glitch

from PIL import Image

im = Image.open("./Original/Mau5.jpg")
Glitch.horizontalStretch(im, (422, 73, 422 + 160, 73 + 30), 10)
Glitch.horizontalStretch(im, (485, 119, 485 + 39, 119 + 39))

tile = im.crop((116, 258, 116 + 763, 258 + 351))
Glitch.tile(im, tile, (116, 258), 270, 100, 1)

tile = im.crop((116, 408, 116 + 763, 408 + 351))
Glitch.tile(im, tile, (116, 408), 270, 50, 1)

tile = im.crop((116, 508, 116 + 763, 508 + 351))
Glitch.tile(im, tile, (116, 508), 270, 25, 1)

tile = im.crop((116, 583, 116 + 763, 583 + 351))
Glitch.tile(im, tile, (116, 583), 270, 12, 1)

Glitch.addPlayButton(im, 30)

im.save("./Results/Mau4.jpg")
