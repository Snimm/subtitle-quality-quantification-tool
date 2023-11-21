
import logging
import cv2
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

import video

reader = video.text_extractor.load_easyocr()
img = cv2.imread('/home/sonnet/Pictures/news_bottom.png')

details_from_image = video.text_extractor.infer_from_model(img, reader)

video.text_extractor.showb_details(details_from_image, img)
logging.debug(video.text_extractor.extract_bbox_from_details(details_from_image))