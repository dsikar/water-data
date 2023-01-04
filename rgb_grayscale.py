import ImageAttribUtils
import os
import glob
from PIL import Image
import numpy as np

def is_grayscale(img):
    """
    is_grayscale(img)
    Check if image is grayscale
    Inputs
      img: rgb image numpy array
    Outputs
      boolean: True if image is grayscale, false otherwise
    Example
      from PIL import Image
      import numpy as np
      import matplotlib.pyplot as plt
      imgpath = 'eagle_greyscale.jpg'
      img = Image.open(imgpath)
      imgnp = np.array(img)
      print(is_grayscale(imgnp))
    """
    import numpy as np
    # assert image array type and length
    dt = type(img).__module__
    assert dt == np.__name__, "Expected numpy array, got " + dt
    assert len(img.shape) == 3, "Expected array length == 3" # RGB channels

    w,h,d = img.shape
    for i in range (0,w):
      for k in range (0,h):
        if(img[i,k,0] != img[i,k,1] or img[i,k,1] != img[i,k,2]):
          print("i: {}, k:{}".format(i, k))
          return False
    return True

  def grayscale(img):
    """
    grayscale(img)
    Return image grayscale ratio
    Inputs
      img: rgb image numpy array
      t: float, ratio of grayscale over RGB
    Outputs
      Ratio of pixels that have equal values (grayscale) by total number of pixels
    Example
      from PIL import Image
      import numpy as np
      import matplotlib.pyplot as plt
      imgpath = 'eagle_grayscale.jpg'
      img = Image.open(imgpath)
      imgnp = np.array(img)
      print(grayscale(imgnp))
    """
    import numpy as np
    # assert image array type and length
    assert type(img).__module__ == np.__name__, "Expected numpy array"
    assert len(img.shape) == 3, "Expected array length == 3" # RGB channels

    total = 0
    neq = 0
    w,h,d = img.shape
    for i in range (0,w):
      for k in range (0,h):
        if(img[i,k,0] != img[i,k,1] or img[i,k,1] != img[i,k,2]):
          neq += 1
        total += 1
    #print("neq =", neq)
    #print("total =", total)
    return (total - neq) / total

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
  print("is_gs: {}, gs_rt: {:.4f}), file: {}".format(is_grayscale(imgnp16bit), grayscale(imgnp16bit), file))
