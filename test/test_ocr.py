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



class Testtext_extractor(unittest.TestCase):
    def test_infer_from_model(self):
        
        reader = video.text_extractor.load_easyocr()
        image = cv2.imread("./test_resource/text.jpeg")
        details_from_image = video.text_extractor.infer_from_model(image, reader)
        video.text_extractor.showb_details(details_from_image, image, True)


if __name__ == '__main__':
    unittest.main()