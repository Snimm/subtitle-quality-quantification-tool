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
import search_sub



class TestSubSearch(unittest.TestCase):

    
    def setUp(self):
        sub_path = "/home/sonnet/ihavenotidea/test_resource/captions-example.srt"
        video_path = "/home/sonnet/ihavenotidea/test_resource/GoTrascript_captions_samples.mp4"
        # Load the EasyOCR model
        cam = cv2.VideoCapture(video_path)
        subtitles = parser.parse(sub_path)
        list_1sub = search_sub.create_sub_struct(subtitles, cam.get(cv2.CAP_PROP_FPS))
        self.list_1sub = list_1sub

    def test_search_sub(self):
        text = search_sub.search_text_in_frame(137, self.list_1sub)
        assert text == {1: 'Professional transcribers will ensure'}

if __name__ == '__main__':
    unittest.main()