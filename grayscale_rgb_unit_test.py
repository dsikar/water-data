import unittest
import ImageAttribUtils
import os
import glob
from PIL import Image
import numpy as np

class TestStringMethods(unittest.TestCase):

    def test_dir(self):
        self.assertTrue(os.path.isdir("water-data/farson-digital/unit-test/"), "Unit test images not found, run git clone https://github.com/dsikar/water-data")
   
    def test_rgb(self):
        iau = ImageAttribUtils.ImageAttribUtils()
        files = sorted(glob.glob("water-data/farson-digital/unit-test/rgb/*.png"))
        for file in files:
            img = Image.open(file)
            imgnp = np.array(img)
            imgnp24bit = imgnp[:, :,0:3]
            self.assertTrue(iau.is_grayscale(imgnp24bit) == False, "Image is not rgb: " + file)

    def test_grayscale(self):
        iau = ImageAttribUtils.ImageAttribUtils()
        files = sorted(glob.glob("water-data/farson-digital/unit-test/grayscale/*.png"))
        for file in files:
            img = Image.open(file)
            imgnp = np.array(img)
            imgnp24bit = imgnp[:, :,0:3]
            self.assertFalse(iau.is_grayscale(imgnp24bit) == False, "Image is not grayscale: " + file)

if __name__ == '__main__':
    unittest.main()