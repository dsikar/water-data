def is_grayscale(img, t=1.0):
  """
  is_grayscale(img)
  Check if image is grayscale
  Inputs
    img: rgb image numpy array
    t: float, ratio of grayscale over RGB
  Outputs
    boolean: True if image is grayscale, false otherwise
  Example
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    imgpath = 'eagle_greyscale.jpg'
    img = Image.open(imgpath)
    imgnp = np.array(img)
    print(is_grayscale(imgnp, 0.95))
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
  total +=1

  if(neq/total < t):
    return False

  return True


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
  assert type(img).__module__ == np.__name__, "Expected numpy array"
  assert len(img.shape) == 3, "Expected array length == 3" # RGB channels

  w,h,d = img.shape
  for i in range (0,w):
    for k in range (0,h):
      if(img[i,k,0] != img[i,k,1] or img[i,k,1] != img[i,k,2]):
        return False
  return True
