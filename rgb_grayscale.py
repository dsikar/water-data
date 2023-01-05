import ImageAttribUtils
import os
import glob
from PIL import Image
import numpy as np

path = "water-data"
if not os.path.exists(path):
    command = "git clone https://github.com/dsikar/water-data"
    os.system(command)

iau = ImageAttribUtils.ImageAttribUtils()

files = sorted(glob.glob("water-data/farson-digital/*/*.png"))
for file in files:
  img = Image.open(file)
  imgnp = np.array(img)
  imgnp16bit = imgnp[:, :,0:3]
  # print("gs: {}, file: {}".format(iau.is_grayscale(imgnp16bit), file))
  iau.is_grayscale_debug(imgnp16bit)
  print("gs: {}, file: {}".format(iau.is_grayscale(imgnp16bit), file))