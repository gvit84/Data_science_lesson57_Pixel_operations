import cv2
def crop_image(start_x, start_y, end_x, end_y):
    image = cv2.imread(image_path)
    cropped_image = image[start_y:end_y, start_x:end_x]
    cv2.imshow('crop', cropped_image)
    cv2.waitKey(0)
    return cropped_image

image_path = 'D:/MyPycharmProjects/Data_science_lesson57_Pixel_operations/img_correct_01.jpg'
crop_image(100, 200, 1250, 1500)




