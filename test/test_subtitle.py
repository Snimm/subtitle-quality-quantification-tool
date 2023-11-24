import sys
import os
import cv2
import unittest
dirname = os.path.dirname(__file__)
path_to_folder = dirname[:-5]
sys.path.append(path_to_folder)
import logging
import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
from pysubparser import parser
import subtitle

class TestSubtitle(unittest.TestCase):

    def test_get_general_sub_area(self):
        image = cv2.imread(image_path)
        height = image.shape[0]
        width = image.shape[1]
        dimensions = (height, width)
        percentage_width_covered_by_sub = 80
        percentage_height__covered_by_sub = 15
        # Test case for get_general_sub_area function
        expected_result = [[[30.1, 153.0], [270.9, 153.0], [270.9, 180.0], [30.1, 180.0]]]
        actual_result = subtitle.Subtitle.get_general_sub_area(dimensions,percentage_width_covered_by_sub, percentage_height__covered_by_sub)
        subtitle.Subtitle.show_sub(actual_result, image, True)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    logging.warning("This test requires an image file to run, if the image file is changed test needs to be updated")

    image_path = "./test_resource/text.jpeg"
    try:
        image_path
    except NameError:
        image_path = input("Enter the path to the image file: ")
    
    unittest.main()
