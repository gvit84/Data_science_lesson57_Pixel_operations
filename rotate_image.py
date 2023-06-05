import cv2

def rotate_image(angle):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    cv2.imshow('rotate', rotated_image)
    cv2.waitKey(0)
    return rotated_image

image_path = 'D:/MyPycharmProjects/Data_science_lesson57_Pixel_operations/img_correct_01.jpg'
rotate_image(90)

