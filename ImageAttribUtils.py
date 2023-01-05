class ImageAttribUtils():

  def __init__(self, px_diff=4, rgb_ratio=0.01):
    self.px_diff = px_diff 
    self.rgb_ratio = rgb_ratio

  def is_grayscale(self, img):
    """
    grayscale(img)
    Return True if image is grayscale
    Inputs
      img: image numpy array of shape (h,w,3)
    Outputs
      Boolean: True is image is grayscale, False if image is RGB
    """
    import numpy as np
    # assert image array type and length
    assert type(img).__module__ == np.__name__, "Expected numpy array"
    assert len(img.shape) == 3, "Expected array length == 3" # RGB channels

    arr_diff = np.maximum(np.maximum(img[:, :,0], img[:, :,1]), img[:, :,2]) - np.minimum(np.minimum(img[:, :,0], img[:, :,1]), img[:, :,2])
    return ((arr_diff > self.px_diff) == True).sum() / (img[:, :,0]).size < self.rgb_ratio 

  def is_grayscale_debug(self, img):
    """
    grayscale(img)
    Debug sum and ratio
    Inputs
      img: image numpy array of shape (h,w,3)
    Outputs
      none
    """
    import numpy as np
    # assert image array type and length
    assert type(img).__module__ == np.__name__, "Expected numpy array"
    assert len(img.shape) == 3, "Expected array length == 3" # RGB channels

    arr_diff = np.maximum(np.maximum(img[:, :,0], img[:, :,1]), img[:, :,2]) - np.minimum(np.minimum(img[:, :,0], img[:, :,1]), img[:, :,2])
    rgb_px_sum = ((arr_diff > self.px_diff) == True).sum() 
    img_size = (img[:, :,0]).size
    rgb_ratio = rgb_px_sum / img_size
    print("rgb_px_sum = {}, img_size = {}, rgb_ratio = {}".format(rgb_px_sum, img_size, rgb_ratio))   