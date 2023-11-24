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
        image = cv2.imread(image_path)

        # Extract text from the image
        actual_result = video.TextExtractor.infer_from_model(image, reader)

        # Display bounding boxes and text details
        video.TextExtractor.show_bbox_details(actual_result, image, True)

        expected_result = [([[46, 38], [76, 38], [76, 66], [46, 66]], 'Ps', 0.9999931722173684), ([[46, 76], [248, 76], [248, 106], [46, 106]], 'HOW TO CREATE', 0.639090788896376), ([[46, 106], [276, 106], [276, 136], [46, 136]], 'HIGHLIGHTED TEXT', 0.5509695520392965), ([[44, 136], [216, 136], [216, 166], [44, 166]], 'IN PHOTSHOP', 0.7551000150388635)]
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    logging.warning("This test requires an image file to run, if the image file is changed test needs to be updated")
    image_path = "./test_resource/text.jpeg"
    try:
        image_path
    except NameError:
        image_path = input("Enter the path to the image file: ")
    
    unittest.main()
