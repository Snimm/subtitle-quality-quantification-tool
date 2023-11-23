import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import matplotlib.pyplot as plt
import cv2
import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
import bbox


class Subtitle():

    @staticmethod
    def get_position_top_down():  # Return 1 for top, -1 for bottom, or 0 for center
        return -1  # Default to top position

    @staticmethod
    def get_general_sub_area(img_dim, percent_start_width = 10, percent_end_width = 90, percent_start_height = 85, percent_end_height = 100):
        logging.debug(f"Image shape: {img_dim}")
        height = img_dim[1]
        width = img_dim[0]

        tl_x = percent_start_width*width*0.01
        tr_x = percent_end_width*width*0.01
        
        # Adjust the subbox position based on the configured position
        position_top_bottom = Subtitle.get_position_top_down()
        if position_top_bottom == -1:  # Bottom position
                    # Assume the bottom 15% of the image contains the subtitle
            tl_y = percent_start_height*height*0.01
            br_y = percent_end_height*height*0.01

        elif position_top_bottom == 1:  # top  position
            # Assume the top 15% of the image contains the subtitle
            tl_y = height - percent_end_height*height*0.01
            br_y = height - percent_start_height*height*0.01

        bl_x = tl_x
        bl_y = br_y
        tr_y = tl_y
        br_x = tr_x

        
        subbox = [[[tl_x, tl_y], [tr_x, tr_y], [br_x, br_y], [bl_x, bl_y]]]
        logging.debug(f"subbox_arr: {subbox}")
        return subbox

    @staticmethod
    def show_sub(subbox, img, display):
        for ibbox in subbox:
            bbox.Bbox.draw_bbox_2_colors(ibbox, img, None, ((255, 0, 0), (0, 255, 0)))

        # Show the output image
        plt.imshow(img)
        if display:
            plt.show()

        return img  # Return the image for further processing if needed
