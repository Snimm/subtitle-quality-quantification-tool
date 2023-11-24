import logging
import cv2
import os
import math

# Configure logging
logging.basicConfig(level=logging.WARNING, format=' %(asctime)s -  %(levelname)s -  %(message)s')
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
import typer
# Define video path


app = typer.Typer()

@app.command()
def get_video_details(video_path:str):
    cam = cv2.VideoCapture(video_path)
    width_cam  = cam.get(cv2.CAP_PROP_FRAME_WIDTH) 
    height_cam  = cam.get(cv2.CAP_PROP_FRAME_HEIGHT) 
    fps = cam.get(cv2.CAP_PROP_FPS)
    frame_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Video details:")
    print(f"fps: {fps}, frame_count: {frame_count}, width: {width_cam} px, height: {height_cam} px, lenght: {frame_count/fps} sec")

    return cam, fps, frame_count, width_cam, height_cam

@app.command()
def main(video_path:str,sub_path:str, percentage_width_covered_by_sub:float = 85,  
         percentage_height__covered_by_sub:float = 15, display_images_with_issue:bool = True, 
         save_images_with_issue:bool = False, number_of_frames_to_analyze:int = 10):
    
    logging.debug(f" type of number_of_frames_to_analyze {type(number_of_frames_to_analyze)}")
    # Load EasyOCR text recognition model
    reader = video.TextExtractor.load_easyocr()
    # Capture video from file
    cam, fps, frame_count, width_cam, height_cam = get_video_details(video_path)
    subtitles = parser.parse(sub_path)
    list_1sub = search_sub.create_subtitle_structure(subtitles, fps)
    every_nth_frame_to_analyze = math.ceil(frame_count / number_of_frames_to_analyze)
    print(f"every_nth_frame_to_analyze: {every_nth_frame_to_analyze}")
    img_dim = (height_cam, width_cam )
    subbox_area = subtitle.Subtitle.get_general_sub_area(img_dim,percentage_width_covered_by_sub,  percentage_height__covered_by_sub)
    # Analyze the video
    video.analye_video(cam, subbox_area, reader, display_images_with_issue, save_images_with_issue, every_nth_frame_to_analyze, list_1sub )

if __name__ == '__main__':
    #Run the app function
    # video_path = "./test_resource/GoTrascript_captions_samples.mp4"
    # sub_path = "./test_resource/captions-example.srt"
    # main(video_path, sub_path)
    app()
