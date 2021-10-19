import cv2
import numpy as np
from keras.models import load_model

mask_model = load_model("mask_model/masknet.h5")  # insert path

face_model = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

mask_label = {0: "MASK", 1: "NO MASK"}


def _find_face(img):
    gray_img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
    faces = face_model.detectMultiScale(gray_img)  # returns a list of (x,y,w,h) tuples
    return faces


def detect_mask(img):
    faces = _find_face(img)

    for i in range(len(faces)):
        x, y, w, h = faces[i]
        crop = img[y : y + h, x : x + w]
        crop = cv2.resize(crop, (128, 128))
        crop = np.reshape(crop, [1, 128, 128, 3]) / 255.0
        mask_result = mask_model.predict(crop)
        if mask_label[mask_result.argmax()] == "MASK":
            cv2.putText(
                img,
                mask_label[mask_result.argmax()],
                (x, y - 10),
                0,
                0.5,
                (0, 255, 0),
                2,
            )
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(
                img,
                mask_label[mask_result.argmax()],
                (x, y - 10),
                0,
                0.5,
                (0, 0, 255),
                2,
            )
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return img

def img_resize(img):
    _, width = img.shape[:2]
    if width > 2200:
        resized = cv2.resize(img, dsize=(0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
        return resized
    return img

def load_detect_save(dir, filename):
    img = cv2.imread(f"{dir}/{filename}")
    img = img_resize(img)
    new_img = detect_mask(img)
    cv2.imwrite(f"{dir}/done_{filename}", new_img)
    return True


if __name__ == "__main__":
    img = cv2.imread("sample_data/main_sample.png")
    new_img = detect_mask(img)
    print(type(new_img))
    # cv2.imwrite('main_sample_processed.png', new_img)
    cv2.imshow("detect_mask", new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
