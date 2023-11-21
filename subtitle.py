
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
from matplotlib import pyplot as plt
import cv2
import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})



class Subtitle():
    def getPosition():#1 for top, -1 for bottom and array gives the actual position
        return 1
    

    def default_position(img_dim):
        pass
    
    def find_sub_box(img):
        logging.debug(f"img shape {img.shape}")
        height = img.shape[0]
        width = img.shape[1]

        return [[[0, .7*height], [width, .7*height], [width, height], [0, height]]]
    
    def show_sub(subbox, img):
        for bbox in subbox:
    
    #Define bounding boxes
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))
            logging.debug(f"tl {tl} tr {tr} br {br} bl {bl}")
            #Put rectangles and text on the image
            cv2.rectangle(img, tl, br, (0, 0, 0), 2)
        # show the output image
        plt.imshow(img)
        plt.show()

