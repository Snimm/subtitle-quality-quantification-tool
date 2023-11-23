import sys
import os
import unittest
import cv2
import matplotlib.pyplot as plt
dirname = os.path.dirname(__file__)
path_to_folder = dirname[:-5]
sys.path.append(path_to_folder)
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

import video
import bbox 


import unittest
import cv2
import video

class TestTextExtractor(unittest.TestCase):

    def test_infer_from_model(self):
        # Load the EasyOCR model
        reader = video.TextExtractor.load_easyocr()

        # Read the test image
        image = cv2.imread("./test_resource/text.jpeg")

        # Extract text from the image
        details_from_image = video.TextExtractor.infer_from_model(image, reader)

        # Display bounding boxes and text details
        video.TextExtractor.show_bbox_details(details_from_image, image, True)

if __name__ == '__main__':
    unittest.main()
