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


class Subtitle:
    @staticmethod
    def get_position():  # Return 1 for top, -1 for bottom, or 0 for center
        return 1  # Default to top position

    @staticmethod
    def find_sub_box(img):
        logging.debug(f"Image shape: {img.shape}")
        height = img.shape[0]
        width = img.shape[1]

        # Assume the bottom 30% of the image contains the subtitle
        subbox = [[[0, 0.7 * height], [width, 0.7 * height], [width, height], [0, height]]]

        # Adjust the subbox position based on the configured position
        position = Subtitle.get_position()
        if position == -1:  # Bottom position
            subbox[0][0][1] = 0.3 * height
            subbox[0][1][1] = 0.3 * height
            subbox[0][2][1] = 0
            subbox[0][3][1] = 0
        elif position == 0:  # Center position
            subbox[0][0][1] = 0.4 * height
            subbox[0][1][1] = 0.4 * height
            subbox[0][2][1] = 0.6 * height
            subbox[0][3][1] = 0.6 * height

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
