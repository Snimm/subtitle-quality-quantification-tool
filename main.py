
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


def obstruction_from_image(img, reader,subbox) :
    details_from_image = video.text_extractor.infer_from_model(img, reader)
    video.text_extractor.showb_details(details_from_image, img, False)
    #logging.debug(subtitle.Subtitle.show_sub(subbox, img, False))
    abs_obstruction = bbox.Bbox.find_obstruction(details_from_image,subbox )
    #logging.debug(f"abs_obstruction {abs_obstruction}")
    relative_obstruction = abs_obstruction/(img.shape[0]*img.shape[1])
    return relative_obstruction
    # logging.debug(f"relatiove_obstruction {relative_obstruction}")
    


reader = video.text_extractor.load_easyocr()
# img = cv2.imread('/home/sonnet/Pictures/news_bottom.png')
video_path = "/home/sonnet/ihavenotidea/test_resource/GoTrascript_captions_samples.mp4"
cam = cv2.VideoCapture(video_path) 
create_issue_frames = True
dirname = os.path.dirname(__file__)
path_to_folder = dirname[:-5]

try: 
    # creating a folder named data 
    if not os.path.exists(f'{path_to_folder}/position_issue_frames'): 
        os.makedirs(f'{path_to_folder}/position_issue_frames') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of position_issue_frames') 


i = 0
obs_arr = []
subbox = None
if subbox == None:
    subbox_given = False
while(True): 
    # reading from frame 
    ret,frame = cam.read() 
    if ret:
        i += 1
        if i%500 == 0:
            if subbox_given == False:
                subbox = subtitle.Subtitle.find_sub_box(frame)
            obs = obstruction_from_image(frame, reader, subbox)
            obs_arr.append(obs)
            logging.debug(f"obs {obs}, i {i}")
            if create_issue_frames == True:
                if obs > 0.005:
                    frame = subtitle.Subtitle.show_sub(subbox, frame, True)

    else:
        break

cam.release()
avg_obs_frame = sum(obs_arr)/len(obs_arr)
logging.debug(f"avg_obs_frame {avg_obs_frame}")
logging.debug(f"subbox {subbox}")