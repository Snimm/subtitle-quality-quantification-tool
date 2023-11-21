
import easyocr
import cv2
import logging
from matplotlib import pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

print("staring video.py")


class text_extractor():

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
    
    def extract_bbox_from_details(details):
        bboxs = []
        for i in details:
            bboxs.append(i[0])
        return bboxs
    
    
    def showb_details(details_from_image, img):
        for (bbox, text, prob) in details_from_image:
            
            #Define bounding boxes
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))
            
            #Remove non-ASCII characters to display clean text on the image (using opencv)
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        
            #Put rectangles and text on the image
            cv2.rectangle(img, tl, br, (0, 0, 0), 2)
            cv2.putText(img, text, (tl[0], tl[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        # show the output image
        plt.imshow(img)
        plt.show()