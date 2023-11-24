from pysubparser import parser

from datetime import datetime
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import logging.config
#For some improting logging is not enough to import logging.config, it needs to be imported explicitly
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})


class StrucSub:
    def __init__(self, start, end, text, fps):
        self.start = int(time_to_frames(start, fps))
        self.end = int(time_to_frames(end, fps))
        self.text = text

def time_to_frames(time_object, fps):
    """Converts time to frames based on the specified FPS"""
    # Parse the time string using the specified format
    # time_format = "%H:%M:%S.%f"
    # time_object = datetime.strptime(time_str, time_format)

    # Calculate the total seconds
    total_seconds = (time_object.hour * 3600 +
        time_object.minute * 60 +
        time_object.second +
        time_object.microsecond / 1e6)

    return total_seconds * fps


def create_subtitle_structure(subtitles, fps):
    """Creates a list of subtitle objects with start, end, and text attributes"""
    subtitle_list = []
    for subtitle in subtitles:
        subtitle_object = StrucSub(subtitle.start, subtitle.end, subtitle.text, fps)
        subtitle_list.append(subtitle_object)

    return subtitle_list


def search_text_in_frame(frame: int, subtitle_list: list) -> dict:
    """Searches for text in a given frame based on the provided subtitle list"""
    text_index = {}
    for i, subtitle_object in enumerate(subtitle_list):
        if subtitle_object.end < frame:  # Subtitle has already ended
            continue

        elif subtitle_object.end > frame and subtitle_object.start <= frame:  # Subtitle is ongoing
            text_index[i] = subtitle_object.text
            #logging.debug(f" frame {frame} index: {i}, start: {subtitle_object.start}, end: {subtitle_object.end}, text: {subtitle_object.text}")
            continue

        elif subtitle_object.end > frame and subtitle_object.start > frame:  # Subtitle has not yet started
            break

    return text_index


# subtitles = parser.parse("./test_resource/captions-example.srt")








def search_text_in_frame(frame:int, list_1sub:list) -> list:

    #! this function is incomplete and may have edge cases where certain 
    text_index = {}
    for i, unitsub in enumerate(list_1sub):
        
        if unitsub.end < frame:
            continue

        elif unitsub.end > frame and unitsub.start < frame:
            text_index[i] = unitsub.text
            #logging.debug(f"index: {i},  start: {unitsub.start}, end: {unitsub.end} text {unitsub.text}")
            continue

        elif unitsub.end > frame and unitsub.start > frame:
            break

    return text_index
