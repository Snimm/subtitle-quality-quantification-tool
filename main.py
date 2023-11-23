import logging
import cv2
import os

# Configure logging
logging.basicConfig(level=logging.ERROR, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import logging.config
#For some improting logging is not enough to import logging.config, it needs to be imported explicitly
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

import video
import subtitle

# Define video path
video_path = "./test_resource/GoTrascript_captions_samples.mp4"

def main(video_path):
    # Capture video from file
    cam = cv2.VideoCapture(video_path)

    # Load EasyOCR text recognition model
    reader = video.TextExtractor.load_easyocr()
    width_cam  = cam.get(cv2.CAP_PROP_FRAME_WIDTH) 
    height_cam  = cam.get(cv2.CAP_PROP_FRAME_HEIGHT) 
    fps = cam.get(cv2.CAP_PROP_FPS)
    frame_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Video details:")
    print(f"fps: {fps}, frame_count: {frame_count}, width: {width_cam} px, height: {height_cam} px, lenght: {frame_count/fps} sec")

    img_dim = (width_cam, height_cam)
    subbox_arr = subtitle.Subtitle.find_sub_box(img_dim)
    # Analyze the video
    video.analye_video(cam, subbox_arr, reader, True, False, 500)

if __name__ == '__main__':
    # Run the main function
    main(video_path)
