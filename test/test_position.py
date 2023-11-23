import sys
import os
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

import video
import bbox 

class TestBbox(unittest.TestCase):

    def setUp(self):
        # Set up logging for the tests
        logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

    def test_get_bbox_from_details(self):
        # Test case for get_bbox_from_details function
        details = [
            ([[68, 134], [274, 134], [274, 158], [68, 158]], 'WORLD BREAKING NEWS', 0.8607316213096277),
            ([[68, 134], [274, 134], [274, 158], [68, 158]], 'NEWS', 0.8)
        ]
        expected_result = [[[68, 134], [274, 134], [274, 158], [68, 158]], [[68, 134], [274, 134], [274, 158], [68, 158]]]
        actual_result = bbox.Bbox.get_bbox_from_details(details)

        self.assertEqual(actual_result, expected_result)

    def test_compress_bbox(self):
        # Test case for compress_bbox function
        bbox_data = [[68, 134], [274, 134], [274, 158], [68, 158]]
        expected_result = [68, 134, 274, 158]
        actual_result = bbox.Bbox.compress_bbox(bbox_data)

        self.assertEqual(actual_result, expected_result)

    def test_bbox_intersection(self):
        # Test case for bbox_intersection function
        boxA = [1, 2, 4, 6]
        boxB = [3, 4, 6, 8]
        expected_result = 2
        actual_result = bbox.Bbox.bbox_intersection(boxA, boxB)

        self.assertEqual(actual_result, expected_result)

    def test_find_obstruction(self):
        # Test case for find_obstruction function
        subtitle_details = [([[68, 134], [274, 134], [274, 158], [68, 158]], 'W', 0)]
        bounding_box = [[[68, 134], [274, 134], [274, 158], [68, 158]]]
        expected_result = 4944
        actual_result = bbox.Bbox.find_obstruction(subtitle_details, bounding_box)

        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
