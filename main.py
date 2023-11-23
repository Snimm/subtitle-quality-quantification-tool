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
import subtitle

from pysubparser import parser
import search_sub
# Define video path
video_path = "./test_resource/GoTrascript_captions_samples.mp4"
sub_path = "./test_resource/captions-example.srt"
def main(video_path):
    # Capture video from file
    cam = cv2.VideoCapture(video_path)

    # Load EasyOCR text recognition model
    reader = video.TextExtractor.load_easyocr()
    width_cam  = cam.get(cv2.CAP_PROP_FRAME_WIDTH) 
    height_cam  = cam.get(cv2.CAP_PROP_FRAME_HEIGHT) 
    fps = cam.get(cv2.CAP_PROP_FPS)
    frame_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)
    subtitles = parser.parse(sub_path)
    list_1sub = search_sub.create_subtitle_structure(subtitles, fps)
    print("Video details:")
    print(f"fps: {fps}, frame_count: {frame_count}, width: {width_cam} px, height: {height_cam} px, lenght: {frame_count/fps} sec")

    img_dim = (height_cam, width_cam )
    subbox_area = subtitle.Subtitle.get_general_sub_area(img_dim)

    # Analyze the video
    video.analye_video(cam, subbox_area, reader, True, False, 500, list_1sub )

if __name__ == '__main__':
    # Run the main function
    main(video_path)
