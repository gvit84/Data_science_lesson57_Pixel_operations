import cv2

def resize_image(new_width, new_height):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (new_width, new_height))
    cv2.imshow('original', image)
    cv2.imshow('resized', resized_image)
    cv2.waitKey(0)
    return resized_image

image_path = 'D:/MyPycharmProjects/Data_science_lesson57_Pixel_operations/img_correct_01.jpg'
resize_image(480, 640)

