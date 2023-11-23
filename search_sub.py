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


def time_to_frames(time_object,fps):
    # Parse the time string using the specified format
    # time_format = "%H:%M:%S.%f"
    # time_object = datetime.strptime(time_str, time_format)

    # Calculate the total seconds
    total_seconds = (
        time_object.hour * 3600 +
        time_object.minute * 60 +
        time_object.second +
        time_object.microsecond / 1e6
    )

    return total_seconds*fps


# subtitles = parser.parse("./test_resource/captions-example.srt")




class StrucSub:
    def __init__(self, start, end, text, fps):
        self.start = int(time_to_frames(start, fps))
        self.end = int(time_to_frames(end, fps))
        self.text = text

def create_sub_struct(subtitles):
    list_1sub = []
    for subtitle in subtitles:
        print(f'{subtitle.start} > {subtitle.end}')
        print(subtitle.text)
        unitsub = StrucSub(subtitle.start, subtitle.end, subtitle.text, 24)
        list_1sub.append(unitsub)
    return list_1sub



def search_text_in_frame(frame:int, list_1sub:list) -> list:

    #! this function is incomplete and may have edge cases where certain 
    text_index = {}
    for i, unitsub in enumerate(list_1sub):
        logging.debug(f"index: {i},  start: {unitsub.start}, end: {unitsub.end} text {unitsub.text}")
        if unitsub.end > frame and unitsub.start < frame:
            text_index[i] = unitsub.text
            continue

        elif unitsub.end > frame and unitsub.start > frame:
            break

        elif unitsub.end < frame:
            #end the loop as searching is point less now
            continue

    return text_index


# text = search_text_in_frame(132, list_1sub)
# print(text)
