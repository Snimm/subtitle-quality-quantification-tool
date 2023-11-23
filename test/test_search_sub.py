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
        # Define subtitle and video paths
        subtitle_path = "/home/sonnet/ihavenotidea/test_resource/captions-example.srt"
        video_path = "/home/sonnet/ihavenotidea/test_resource/GoTrascript_captions_samples.mp4"

        # Capture video stream
        self.cam = cv2.VideoCapture(video_path)

        # Parse subtitles from the provided file
        self.subtitles = parser.parse(subtitle_path)

        # Create a list of subtitle objects with start, end, and text attributes
        fps = self.cam.get(cv2.CAP_PROP_FPS)
        self.list_1sub = search_sub.create_subtitle_structure(self.subtitles, fps)

    def test_search_sub(self):
        # Search for text in frame 137
        frame_index = 137
        expected_text = {1: 'Professional transcribers will ensure'}
        actual_text = search_sub.search_text_in_frame(frame_index, self.list_1sub)

        # Assert that the retrieved text matches the expected text
        self.assertEqual(actual_text, expected_text)

if __name__ == '__main__':
    unittest.main()
