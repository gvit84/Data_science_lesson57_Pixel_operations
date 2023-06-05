import cv2
def save_image(img, image_path):
    cv2.imwrite(image_path, img)

img = cv2.imread('D:/MyPycharmProjects/Data_science_lesson57_Pixel_operations/img_correct_01.jpg')
save_image(img, "D:/Images_home_task/img_correct_01_copy.jpg")