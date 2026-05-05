import cv2


def preprocess_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Could not read image file")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    return thresh
