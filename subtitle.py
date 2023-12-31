import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
import matplotlib.pyplot as plt
import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
import bbox
class Subtitle():

    @staticmethod
    def get_position_top_down():  
        #TODO
        # Return 1 for top, -1 for bottom
        return -1  # Default to bottom position

    @staticmethod
    def get_general_sub_area(video_dimensions: tuple, percentage_width_covered_by_sub:float,  percentage_height__covered_by_sub:float):  
        """Calculates the general subtitle area based on specified percentages"""
        percent_start_width = (100-percentage_width_covered_by_sub)/2
        percent_end_width = 100 - percent_start_width
        percent_start_height = (100-percentage_height__covered_by_sub)
        percent_end_height = 100 
        percent_start_height = 85.0
       

        height, width = video_dimensions

        tl_x = percent_start_width*width*0.01
        tr_x = percent_end_width*width*0.01
        
        # Adjust the subbox position based on the configured position
        position_top_bottom = Subtitle.get_position_top_down()
        if position_top_bottom == -1: 
            # Bottom position
            # Assume the bottom 15% of the image contains the subtitle
            tl_y = percent_start_height*height*0.01
            br_y = percent_end_height*height*0.01

        elif position_top_bottom == 1:  
            # top  position
            # Assume the top 15% of the image contains the subtitle
            tl_y = height - percent_end_height*height*0.01
            br_y = height - percent_start_height*height*0.01
        else:
            raise ValueError("Invalid subtitle position: " + str(position_top_bottom))

        bl_x = tl_x
        bl_y = br_y
        tr_y = tl_y
        br_x = tr_x

        # Construct the subtitle box using the calculated coordinates
        subbox = [[[tl_x, tl_y], [tr_x, tr_y], [br_x, br_y], [bl_x, bl_y]]]
        #logging.debug(f"subbox_arr: {subbox}")
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
