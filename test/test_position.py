import sys
import os
import unittest
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



class TestBbox(unittest.TestCase):
     
    def test_get_bbox_from_details(self):
        details = [([[68, 134], [274, 134], [274, 158], [68, 158]], 'WORLD BREAKING NEWS', 0.8607316213096277), ([[68, 134], [274, 134], [274, 158], [68, 158]], 'NEWS', 0.8)]
        result = bbox.Bbox.get_bbox_from_details(details)
        self.assertEqual(result, [[[68, 134], [274, 134], [274, 158], [68, 158]], [[68, 134], [274, 134], [274, 158], [68, 158]]])

    def test_compress_bbox(self):
        bbox_data = [[68, 134], [274, 134], [274, 158], [68, 158]]
        result = bbox.Bbox.compress_bbox(bbox_data)
        self.assertEqual(result, [68, 134, 274, 158])

    def test_bbox_intersection(self):
        boxA = [1, 2, 4, 6]
        boxB = [3, 4, 6, 8]
        result = bbox.Bbox.bbox_intersection(boxA, boxB)
        self.assertEqual(result, 2)

    def test_find_obstruction(self):
        result = bbox.Bbox.find_obstruction([([[68, 134], [274, 134], [274, 158], [68, 158]], 'W', 0)], [[[68, 134], [274, 134], [274, 158], [68, 158]]])
        self.assertEqual(result, 4944)


if __name__ == '__main__':
    unittest.main()