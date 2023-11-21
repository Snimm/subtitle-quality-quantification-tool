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



# class TestBbox(unittest.TestCase):
     
#     def test_get_bbox_from_details(self):
#         details = [([[68, 134], [274, 134], [274, 158], [68, 158]], 'WORLD BREAKING NEWS', 0.8607316213096277), ([[68, 134], [274, 134], [274, 158], [68, 158]], 'NEWS', 0.8)]
#         result = bbox.get_bbox_from_details(details)
#         self.assertEqual(result, [[[68, 134], [274, 134], [274, 158], [68, 158]], [68, 134], [274, 134], [274, 158], [68, 158]])

#     def test_compress_bbox(self):
#         bbox_data = [[68, 134], [274, 134], [274, 158], [68, 158], [68, 134], [274, 134], [274, 158], [68, 158]]
#         result = bbox.compress_bbox(bbox_data)
#         self.assertEqual(result, [[68, 134, 274, 158],[68, 134, 274, 158]  ])
#         bbox_data = [[68, 134, 68, 158], [68, 134, 68, 158], [68, 134, 68, 158]]
#         result = bbox.compress_bbox(bbox_data)
#         self.assertEqual(result, [[68, 134, 68, 158], [68, 134, 68, 158], [68, 134, 68, 158]])

#     def test_bbox_intersection(self):
#         boxA = [1, 2, 4, 6]
#         boxB = [3, 4, 6, 8]
#         result = bbox.bbox_intersection(boxA, boxB)
#         self.assertEqual(result, 4)

#     def test_bbox_union(self):
#         boxA = [1, 2, 4, 6]
#         boxB = [3, 4, 6, 8]
#         result = bbox.bbox_union(boxA, boxB)
#         self.assertEqual(result, 15)

#     def test_bbox_intersection_over_union(self):
#         boxA = [1, 2, 4, 6]
#         boxB = [3, 4, 6, 8]
#         result = bbox.bbox_intersection_over_union(boxA, boxB)
#         self.assertEqual(result, 4 / 15)

# # class TestFindObstruction(unittest.TestCase):

# #     @patch('your_module.bbox.bbox_intersection', return_value=2)
# #     def test_find_obstruction(self, mock_intersection):
# #         details = [(1, 2, 3), (4, 5, 6)]
# #         sub_box_array = [((1, 2), (3, 4)), ((5, 6), (7, 8))]
# #         result = find_obstruction(details, sub_box_array)
# #         self.assertEqual(result, 4)  # (2 / 15) * 2 for each sub_box

# if __name__ == '__main__':
#     unittest.main()