
import logging
import cv2
import os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import logging.config

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

import video

video_path = "./test_resource/GoTrascript_captions_samples.mp4"

def main(video_path):
    cam = cv2.VideoCapture(video_path) 
    reader = video.text_extractor.load_easyocr()
    video.analye_video(cam, None, reader, True, False, 500)

if __name__ == '__main__':
    main(video_path)