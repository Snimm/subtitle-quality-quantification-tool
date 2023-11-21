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
        details = [([[68, 134], [274, 134], [274, 158], [68, 158]], 'WORLD BREAKING NEWS', 0.8607316213096277)]
        bbox_array = bbox.get_bbox_from_details(details)
        self.assertEqual(bbox_array, [[68, 134], [274, 134], [274, 158], [68, 158]])
    
    def test_compress_bbox(self):
        bbox_array = [[68, 134], [274, 134], [274, 158], [68, 158]]
        new_bbox = bbox.bbox.compress_bbox(bbox_array)
        self.assertEqual(new_bbox, [68, 134, 274, 158])
    
    def test_bbox_intersection(self):
        boxA = (0, 0, 1, 1)
        boxB = (0, 0, 1, 1)
        intersection = bbox.bbox_intersection(boxA, boxB)
        self.assertEqual(intersection, 1)
    
    def test_bbox_union(self):
        boxA = (0, 0, 1, 1)
        boxB = (0, 0, 1, 1)
        union = bbox.bbox_union(boxA, boxB)
        self.assertEqual(union, 4)
    
    def test_bbox_intersection_over_union(self):
        boxA = (0, 0, 1, 1)
        boxB = (0, 0, 1, 1)
        iou = bbox.bbox_intersection_over_union(boxA, boxB)
        self.assertEqual(iou, 0.25)

if __name__ == '__main__':
    unittest.main() 