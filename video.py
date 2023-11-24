import easyocr
import cv2
import logging
from matplotlib import pyplot as plt
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

# Import custom modules
import bbox
import subtitle
import search_sub
# Define text extractor class
class TextExtractor:
    @staticmethod
    def find_image_shape(img: cv2.Mat) -> tuple:
        """
        Determines the shape of an image.

        Args:
            img: The input image.

        Returns:
            A tuple containing the image's height and width.
        """
        return img.shape

    @staticmethod
    def load_easyocr() -> easyocr.Reader:
        """
        Loads the EasyOCR text recognition model.

        Returns:
            An instance of the EasyOCR text recognition model.
        """
        reader = easyocr.Reader(['hi', 'en'], gpu=True)  # Hindi, Telugu, and English
        return reader

    @staticmethod
    def infer_from_model(image: cv2.Mat, reader: easyocr.Reader) -> list:
        """
        Recognizes text from an image using the EasyOCR model.

        Args:
            image: The input image.
            reader: The EasyOCR text recognition model.

        Returns:
            A list of recognized text elements, each represented as a tuple containing the bounding box, text, and probability.
        """
        results = reader.readtext(image, detail=1, paragraph=False)  # Set detail to 0 for simple text output
        #logging.debug(f"Recognition details for image: {results}")
        return results

    @staticmethod
    def extract_bbox_from_details(details: list) -> list:
        """
        Extracts bounding boxes from recognition details.

        Args:
            details: The recognition details.

        Returns:
            A list of bounding boxes.
        """
        bboxes = []
        for i in details:
            bboxes.append(i[0])
        return bboxes

    @staticmethod
    def show_bbox_details(details: list, img: cv2.Mat, display: bool):
        """
        Visualizes bounding boxes and text on an image.

        Args:
            details: The recognition details.
            img: The input image.
            display: Whether to display the image.
        """
        for (ibbox, text, prob) in details:
            bbox.Bbox.draw_bbox_2_colors(ibbox, img, text, ((0,0,255),(255,0,255)))

        if display:
            plt.imshow(img)
            plt.show()

# Define obstruction calculation function
def obstruction_from_image(img: cv2.Mat, reader: easyocr.Reader, subbox: list) -> float:
    """
    Calculates the obstruction of text by subboxes in an image.

        Args:
            img: The input image.
            reader: The EasyOCR text recognition model.
            subbox: The subbox representing the area of interest.

        Returns:
            The relative obstruction of text by subboxes.
        """
    details_from_image = TextExtractor.infer_from_model(img, reader)
    TextExtractor.show_bbox_details(details_from_image, img, False)

    abs_obstruction = bbox.Bbox.find_obstruction(details_from_image, subbox)
    relative_obstruction = abs_obstruction / (img.shape[0] * img.shape[1])
    return relative_obstruction

# Define video analysis function
def analye_video(cam: cv2.VideoCapture, subbox: list, reader: easyocr.Reader, display_image: bool, save_image: bool, every_what_frame: int, list_1sub:list) -> list:
    
    logging.info("Starting video analysis")
    logging.debug(f"Initial subtitle box: {subbox}")

    issue_frames = []
    create_issue_frames = True

    try:
        if not os.path.exists(f'./position_issue_frames'):
            os.makedirs(f'./position_issue_frames')
            logging.info("Created directory for position issue frames")
    except OSError as e:
        print('Error: Creating directory of position_issue_frames')
        logging.error(e)

    frame_count = 0
    obs_arr = []
    ob_loc = []

    # Process video frames
    while True:

        subbox_for_i_frame = subbox.copy()
        ret, frame = cam.read()

        if ret:
            frame_count += 1

            # Process only every `every_what_frame` frames
            if frame_count % every_what_frame == 0:
                logging.debug(f"Processing frame {frame_count}")

                # Extract text in the current frame
                text = search_sub.search_text_in_frame(frame_count, list_1sub)

                # If no text is found, reset the subtitle box to zeros
                if len(text) == 0:
                    logging.debug("No text found in frame, resetting subtitle box")
                    subbox_for_i_frame = [[[0, 0], [0, 0], [0, 0], [0, 0]]]

                logging.debug(f"Updated subtitle box: {subbox_for_i_frame}")

                # Calculate obstruction
                obs = obstruction_from_image(frame, reader, subbox_for_i_frame)
                obs_arr.append(obs)
                logging.debug(f"Obstruction: {obs}, Frame: {frame_count}, Time: {frame_count / cam.get(cv2.CAP_PROP_FPS)} sec")

                if obs > 0:
                    logging.warning(f"Obstruction issue detected in frame {frame_count}, Time: {frame_count / cam.get(cv2.CAP_PROP_FPS)} sec")
                    issue_frames.append(frame_count)

                # Create issue frames if necessary
                if create_issue_frames and obs > 0:
                    ob_loc.append(frame_count)
                    frame = subtitle.Subtitle.show_sub(subbox_for_i_frame, frame, display_image)

                    if save_image:
                        logging.debug(f"Saving issue frame {frame_count}")
                        frame.savefig(f"./position_issue_frames/frame_{frame_count}.png", bbox_inches='tight')

        else:
            logging.info("Video analysis complete")
            break

    # Release camera object
    cam.release()

    # Calculate average obstruction
    avg_obs_frame = sum(obs_arr) / len(obs_arr)
    logging.debug(f"Average obstruction per frame: {avg_obs_frame}")
    return issue_frames
