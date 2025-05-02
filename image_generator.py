import cv2 as cv
import os
from PIL import Image 

def get_last_id(path):
    """
    Get the last id of the images in the given path
    :param path: str
    :return: int
    """
    images = os.listdir(path)
    return str(len(images))

class ImageGen:
    def __init__(self, path):
        self.path = path
        self.images = os.listdir(path)

    def mirror_all_images(self):
        for img in self.images:
            img_path = os.path.join(self.path, img)
            image = cv.imread(img_path)
            mirrored_image = cv.flip(image, 1)
            save_path = f'{self.path}/{get_last_id(self.path)}.jpg'
            cv.imwrite(save_path, mirrored_image)

    def rotate_all_images(self, angle):
        for img in self.images:
            img_path = os.path.join(self.path, img)
            image = Image.open(img_path) 
            rotated_image = image.rotate(angle)
            save_path = f'{self.path}/{get_last_id(self.path)}.jpg'
            rotated_image = rotated_image.convert('RGB')
            rotated_image.save(save_path)

def rename_all_files(path):
    """
    Rename all files in the given path
    :param path: str
    :return: None
    """
    i=0
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        new_name = os.path.join(path, str(i)+".jpg")
        os.rename(file_path, new_name)
        i+=1

def rename():
    altf4_path = "images/altf4"
    ses_ac_path = "images/ses_ac"
    ses_kapa_path = "images/ses_kapa"

    rename_all_files(altf4_path)
    rename_all_files(ses_ac_path)
    rename_all_files(ses_kapa_path)

def image_generate():
    altf4_path = "images/altf4"
    ses_ac_path = "images/ses_ac"
    ses_kapa_path = "images/ses_kapa"

    altf4_gen = ImageGen(altf4_path)
    ses_ac_gen = ImageGen(ses_ac_path)
    ses_kapa_gen = ImageGen(ses_kapa_path)

    altf4_gen.mirror_all_images()
    ses_ac_gen.mirror_all_images()
    ses_kapa_gen.mirror_all_images()

    altf4_gen = ImageGen(altf4_path)
    ses_ac_gen = ImageGen(ses_ac_path)
    ses_kapa_gen = ImageGen(ses_kapa_path)

    altf4_gen.rotate_all_images(45)
    ses_ac_gen.rotate_all_images(45)
    ses_kapa_gen.rotate_all_images(45)

    altf4_gen.rotate_all_images(315)
    ses_ac_gen.rotate_all_images(315)
    ses_kapa_gen.rotate_all_images(315)

if __name__ == "__main__":
    #rename()
    image_generate()
