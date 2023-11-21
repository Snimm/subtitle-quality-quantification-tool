
import logging
import cv2
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

reader = video.text_extractor.load_easyocr()
img = cv2.imread('/home/sonnet/Pictures/news_bottom.png')
logging.debug(img.shape)
details_from_image = video.text_extractor.infer_from_model(img, reader)

#video.text_extractor.showb_details(details_from_image, img)
logging.debug(f"details in main: {details_from_image}")
logging.debug(f"bbox from details {video.text_extractor.extract_bbox_from_details(details_from_image)}")

subbox = subtitle.Subtitle.find_sub_box(img)

abs_obstruction = bbox.Bbox.find_obstruction(details_from_image,subbox )
logging.debug(f"abs_obstruction {abs_obstruction}")
relative_obstruction = abs_obstruction/(img.shape[0]*img.shape[1])

logging.debug(f"relatiove_obstruction {relative_obstruction}")
#logging.debug(subtitle.Subtitle.show_sub(subbox, img))
