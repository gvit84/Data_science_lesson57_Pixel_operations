import cv2

def open_image(image_path):
    img = cv2.imread(image_path)
    cv2.imshow('img', img)
    cv2.waitKey(0)

image_path = 'D:/MyPycharmProjects/Data_science_lesson57_Pixel_operations/img_correct_01.jpg'
open_image(image_path)