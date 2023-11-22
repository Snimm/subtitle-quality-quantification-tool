
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
from matplotlib import pyplot as plt
import cv2
import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
import bbox


class Subtitle():
    @staticmethod
    def getPosition():#1 for top, -1 for bottom and array gives the actual position
        return 1

    @staticmethod
    def find_sub_box(img):
        logging.debug(f"img shape {img.shape}")
        height = img.shape[0]
        width = img.shape[1]
        #assume bootom 30% of the image is the subtitle
        return [[[0, .7*height], [width, .7*height], [width, height], [0, height]]]
    
    @staticmethod
    def show_sub(subbox, img, display):
        for ibbox in subbox:
            bbox.Bbox.draw_white_black_rec(ibbox, img, None, ((0,0,0),(255,255,255)))
        # show the output image
        image = plt.gcf()
        plt.imshow(img)
        if display:
            plt.show()
        return image

