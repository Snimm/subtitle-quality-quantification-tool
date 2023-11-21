
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

logging.debug("starting bbox")
class Bbox():
    @staticmethod
    def get_bbox_from_details(details):
        bbox_array = []
        for detail in details:
            assert len(detail) == 3
            bbox_array.append(detail[0])
        return bbox_array
    
    @staticmethod
    def compress_bbox(bbox):
        logging.debug(bbox)
        logging.debug(len(bbox))
        if len(bbox) == 4:
            logging.debug(bbox)
            new_bbox = [bbox[0][0], bbox[0][1], bbox[2][0],  bbox[2][1]]

            logging.debug(new_bbox)
            return new_bbox
        # elif len(bbox) == 2:
        #     new_bbox = [bbox[0][0], bbox[0][1], bbox[1][0],  bbox[1][1]]
        #     return new_bbox
        else:
            logging.error("Invalid bbox")
            return None

    @staticmethod
    def bbox_intersection(boxA, boxB):
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])
        return max(0, xB - xA + 1) * max(0, yB - yA + 1)
    @staticmethod    
    def bbox_union(boxA, boxB):
        # compute the area of both the prediction and ground-truth
        # rectangles
        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
        return float(boxAArea + boxBArea - Bbox.bbox_intersection(boxA, boxB))
    @staticmethod
    def bbox_intersection_over_union(boxA, boxB):
	# determine the (x, y)-coordinates of the intersection rectangle
        interArea = Bbox.bbox_intersection(boxA, boxB)
        iou = interArea / Bbox.bbox_union(boxA, boxB)
        # return the intersection over union value
        return iou
    
    @staticmethod
    def find_obstruction(details, sub_box_array):

        logging.debug(f"sub_box_array: {sub_box_array}")
        logging.debug(f"details: {details}")
        txt_box_array = Bbox.get_bbox_from_details(details)
        logging.debug(f"txt_box_array: {txt_box_array}")
        obstruction = 0
        for sub_box in sub_box_array:

            sub_box = Bbox.compress_bbox(sub_box)
            logging.debug(f"sub_box_compressed: {sub_box}")
            for txt_box in txt_box_array:
                logging.debug(f"sub_box: {sub_box}, txt_box: {txt_box}")
                txt_box = Bbox.compress_bbox(txt_box)
                logging.debug(f"txt_box after compression: {txt_box}")
                obstruction += (Bbox.bbox_intersection(sub_box, txt_box))

        return obstruction


if __name__ == "__main__":
    assert 5175 == Bbox.find_obstruction([([[68, 134], [274, 134], [274, 158], [68, 158]], 'WORLD BREAKING NEWS', 0.8607316213096277)], [[[68, 134], [274, 134], [274, 158], [68, 158]]])