import logging
import cv2
import os
import math

# Configure logging
logging.basicConfig(level=logging.WARNING, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import logging.config
#For some reason, improting logging is not enough to import logging.config, it needs to be imported explicitly
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
def get_video_details(video_path: str):
    """Extracts video details such as FPS, frame count, width, and height"""

    cam = cv2.VideoCapture(video_path)

    # Capture video properties
    width_cam = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    height_cam = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cam.get(cv2.CAP_PROP_FPS)
    frame_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)

    # Display video details
    print("Video details:")
    logging.debug(f"Video path: {video_path}")
    print(f"FPS: {fps}")
    print(f"Frame count: {frame_count}")
    print(f"Width: {width_cam} px")
    print(f"Height: {height_cam} px")
    print(f"Length: {frame_count / fps} sec")

    return cam, fps, frame_count, width_cam, height_cam

@app.command()
def main(video_path: str, sub_path: str, percentage_width_covered_by_sub: float = 85,
         percentage_height__covered_by_sub: float = 15, display_images_with_issue: bool = True,
         save_images_with_issue: bool = False, number_of_frames_to_analyze: int = 10):
    """Analyzes a video for subtitle obstruction"""

    # Load EasyOCR text recognition model
    reader = video.TextExtractor.load_easyocr()

    # Capture video from file
    cam, fps, frame_count, width_cam, height_cam = get_video_details(video_path)

    # Parse subtitles from the provided file
    subtitles = parser.parse(sub_path)

    # Create a list of subtitle objects with start, end, and text attributes
    list_1sub = search_sub.create_subtitle_structure(subtitles, fps)

    # Calculate every nth frame to analyze based on the specified number of frames
    every_nth_frame_to_analyze = math.ceil(frame_count / number_of_frames_to_analyze)
    print(f"Every nth frame to analyze: {every_nth_frame_to_analyze}")

    # Define subtitle box area based on percentages
    img_dim = (height_cam, width_cam)
    subbox_area = subtitle.Subtitle.get_general_sub_area(img_dim, percentage_width_covered_by_sub, percentage_height__covered_by_sub)

    # Analyze the video for subtitle obstruction
    video.analye_video(cam, subbox_area, reader, display_images_with_issue, save_images_with_issue, every_nth_frame_to_analyze, list_1sub)

if __name__ == '__main__':
    app()
