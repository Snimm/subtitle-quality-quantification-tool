import logging
import cv2
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import logging.config
#For some improting logging is not enough to import logging.config, it needs to be imported explicitly
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

import video

# Define video path
video_path = "./test_resource/GoTrascript_captions_samples.mp4"

def main(video_path):
    # Capture video from file
    cam = cv2.VideoCapture(video_path)

    # Load EasyOCR text recognition model
    reader = video.TextExtractor.load_easyocr()

    # Analyze the video
    video.analye_video(cam, None, reader, True, False, 500)

if __name__ == '__main__':
    # Run the main function
    main(video_path)
