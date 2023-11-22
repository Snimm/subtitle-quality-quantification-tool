
import logging
import cv2
import os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
from matplotlib import pyplot as plt
import logging.config

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})


import video
import bbox
import subtitle

video_path = "/home/sonnet/ihavenotidea/test_resource/GoTrascript_captions_samples.mp4"
cam = cv2.VideoCapture(video_path) 
reader = video.text_extractor.load_easyocr()

video.analye_video(cam, None, reader, True, False, 500)