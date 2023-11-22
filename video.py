
import easyocr
import cv2
import logging
from matplotlib import pyplot as plt
import os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
import bbox
import subtitle
logging.debug("staring video.py")


class text_extractor():
    def find_image_shape(img):
        return img.shape


    @staticmethod
    def load_easyocr():
        reader = easyocr.Reader(['hi', 'en'], gpu=True)  #Hindi, telugu, and English
        return reader
    
    @staticmethod
    def infer_from_model(image, reader):
        results = reader.readtext(image, detail=1, paragraph=False) #Set detail to 0 for simple text output
        logging.debug(f"details of image {results}")
        #Paragraph=True will combine all results making it easy to capture it in a dataframe. 
        return results
    @staticmethod
    def extract_bbox_from_details(details):
        bboxs = []
        for i in details:
            bboxs.append(i[0])
        return bboxs
    
    @staticmethod
    def showb_details(details_from_image, img, display):
        for (ibbox, text, prob) in details_from_image:
            bbox.Bbox.draw_white_black_rec(ibbox, img, text, ((0,255,0),(255,0,255)))
 
        # show the output image
        if display == True:
            plt.imshow(img)
            plt.show()

def obstruction_from_image(img, reader,subbox) :
    details_from_image = text_extractor.infer_from_model(img, reader)
    text_extractor.showb_details(details_from_image, img, False)
    #logging.debug(subtitle.Subtitle.show_sub(subbox, img, False))
    abs_obstruction = bbox.Bbox.find_obstruction(details_from_image,subbox )
    #logging.debug(f"abs_obstruction {abs_obstruction}")
    relative_obstruction = abs_obstruction/(img.shape[0]*img.shape[1])
    return relative_obstruction
    # logging.debug(f"relatiove_obstruction {relative_obstruction}")



def analye_video(cam, subbox, reader, display_image, save_image, every_what_frame):
    # img = cv2.imread('/home/sonnet/Pictures/news_bottom.png')
    create_issue_frames = True
    try: 
        # creating a folder named data 
        if not os.path.exists(f'./position_issue_frames'): 
            os.makedirs(f'./position_issue_frames') 
    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of position_issue_frames') 
    i = 0
    obs_arr = []
    ob_loc = []
    subbox_given = True
    if subbox == None:
        subbox_given = False
    while(True): 
        # reading from frame 
        ret,frame = cam.read() 
        if ret:
            i += 1
            if i%every_what_frame == 0:
                if subbox_given == False:
                    subbox = subtitle.Subtitle.find_sub_box(frame)

                obs = obstruction_from_image(frame, reader, subbox)
                obs_arr.append(obs)
                logging.debug(f"obs {obs}, i {i}")
                if create_issue_frames == True:
                    if obs > 0.005:
                        ob_loc.append(i)
                        frame = subtitle.Subtitle.show_sub(subbox, frame, display_image)
                        if save_image == True:
                            frame.savefig(f"./position_issue_frames/frame_{i}.png", bbox_inches='tight')
        else:
            break

    cam.release()
    avg_obs_frame = sum(obs_arr)/len(obs_arr)
    logging.debug(f"avg_obs_frame {avg_obs_frame}")
    logging.debug(f"subbox {subbox}")

