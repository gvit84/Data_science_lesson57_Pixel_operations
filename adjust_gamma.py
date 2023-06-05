import numpy as np
import cv2

def adjust_gamma(gamma):
    img = cv2.imread(image_path)
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    img_corrected = cv2.LUT(img, table)
    cv2.imshow('original', img)
    cv2.imshow('corrected', img_corrected)
    cv2.waitKey(0)
    return img_corrected



image_path = 'D:/MyPycharmProjects/Data_science_lesson57_Pixel_operations/img_correct_01.jpg'
adjust_gamma(0.5)
