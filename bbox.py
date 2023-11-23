import logging
import cv2
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Disable existing loggers to avoid conflicting messages
logging.config.dictConfig({"version": 1, "disable_existing_loggers": True})


class Bbox:
    """
    A class for representing and manipulating bounding boxes.
    """

    @staticmethod
    def get_bbox_from_details(details: list[list]) -> list[list]:
        """
        Extracts a list of bounding boxes from a list of details.

        Args:
            details: A list of detail lists, where each detail is expected to have 3 elements.

        Returns:
            A list of bounding boxes, where each box is represented as a list of coordinates.

        Raises:
            AssertionError: If any detail element doesn't have 3 elements.
        """
        bbox_array = []
        for detail in details:
            assert len(detail) == 3, "Each detail element must have 3 elements!"
            bbox_array.append(detail[0])
        return bbox_array

    @staticmethod
    def compress_bbox(bbox: list) -> list:
        """
        Compresses a bounding box representation from a list of 4 points to a list of 2 points.

        Args:
            bbox: A list containing 4 points of the bounding box.

        Returns:
            A list containing the top-left and bottom-right points of the bounding box or None.

        Raises:
             logging.error: If the input bbox is not a list of length 4.
        """
        if isinstance(bbox, list) and len(bbox) == 4:
            new_bbox = [bbox[0][0], bbox[0][1], bbox[2][0], bbox[2][1]]
            return new_bbox
        logging.error(f"Invalid bbox: {bbox}")
        return None

    @staticmethod
    def bbox_intersection(boxA: list, boxB: list) -> float:
        """
        Calculates the area of intersection between two bounding boxes.

        Args:
            boxA: A list containing the coordinates of the first bounding box.
            boxB: A list containing the coordinates of the second bounding box.

        Returns:
            The area of intersection between the two bounding boxes.
        """
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])
        return abs(max((xB - xA, 0)) * max((yB - yA), 0))
    
    def draw_bbox_2_colors(bbox: list, img: cv2.Mat, text: str, colors: tuple) -> None:
        """
        Draws a white rectangle with a black outline around a bounding box and adds text if provided.

        Args:
            bbox: A list of four coordinates representing the bounding box.
            img: The NumPy array representing the image.
            text: The text to be added to the image.
            colors: A tuple of two RGB color values for the rectangle border.

        Returns:
            None
        """

    # Validate color format
        if len(colors) != 2 or not all(
        isinstance(color, tuple) and len(color) == 3 and all(0 <= i <= 255 for i in color)
        for color in colors):
            raise ValueError("Invalid colors format. Expected a tuple of two integers between 0 and 255.")

        # Convert coordinates to integers
        bbox = [
            (round(coordinate[0]), round(coordinate[1]))
            for coordinate in bbox
        ]

        # Extract coordinates
        tl, tr, br, bl = bbox

        # Draw white rectangle with black outline
        cv2.rectangle(img, tl, br, colors[0], 1)
        offset = 2  # Offset value to avoid overlapping
        tl_offset = (tl[0] + offset, tl[1] + offset)
        tr_offset = (tr[0] + offset, tr[1] + offset)
        br_offset = (br[0] + offset, br[1] + offset)
        bl_offset = (bl[0] + offset, bl[1] + offset)
        cv2.rectangle(img, tl_offset, br_offset, colors[1], 1)

        # Add text if provided
        if text:
            text = text.strip()

            # Remove non-ASCII characters to avoid encoding issues
            text = "".join([c if ord(c) < 128 else "" for c in text])

            cv2.putText(img, text, (tl[0], tl[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)
            cv2.putText(img, text, (tl[0], tl[1] - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[1], 1)


    @staticmethod
    def find_obstruction(details: list[list], sub_box_array: list[list]) -> int:
        """
        Calculates the total area of obstruction between text boxes and sub boxes.

        Args:
            details: A list of detail lists containing text information.
            sub_box_array: A list of lists containing coordinates of potential obstructions.

        Returns:
            The total area of the obstructed text.
        """

        logging.debug(f"Sub-box array: {sub_box_array}")
        logging.debug(f"Details: {details}")

        # Get a list of bounding boxes from details
        txt_box_array = Bbox.get_bbox_from_details(details)
        logging.debug(f"Text box array: {txt_box_array}")

        total_obstruction = 0  # Initialize total obstruction area

        # Iterate over each sub-box
        for sub_box in sub_box_array:
            # Compress the sub-box into a 2-point representation
            sub_box = Bbox.compress_bbox(sub_box)
            logging.debug(f"Compressed sub-box: {sub_box}")

            # Iterate over each text box
            for txt_box in txt_box_array:
                # Compress the text box into a 2-point representation
                txt_box = Bbox.compress_bbox(txt_box)
                logging.debug(f"Compressed text box: {txt_box}")

                # Calculate the area of intersection between the sub-box and the text box
                intersection_area = Bbox.bbox_intersection(sub_box, txt_box)
                logging.debug(f"Intersection area: {intersection_area}")

                # Update the total obstruction area
                total_obstruction += intersection_area

        return total_obstruction
