# _*_coding:utf-8_*_
#  作者    : shinevalora
#  创建时间: 2019/9/8  20:13

import logging
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")

Img, Image_save = 'Img', 'Image_save'

if not os.path.exists(Img):
    os.makedirs(Img)

if not os.path.exists(Image_save):
    os.makedirs(Image_save)


# 定义图像拼接函数
def image_compose():
    import glob

    import cv2
    import numpy as np

    num = len(os.listdir('Image/'))
    # print(num)

    if num % 4 == 0:

        logging.info(f"Image 文件夹下的 .jpg 图片格式的文件共有 {num} 个\n")

        for i in range(1, num + 1, 4):
            logging.info(f"准备读取并合并{glob.glob(f'Image/{i}_*.jpg')[0]}")
            logging.info(f"准备读取并合并{glob.glob(f'Image/{i + 1}_*.jpg')[0]}")
            logging.info(f"准备读取并合并{glob.glob(f'Image/{i + 2}_*.jpg')[0]}")
            logging.info(f"准备读取并合并{glob.glob(f'Image/{i + 3}_*.jpg')[0]}")

            img1 = cv2.imread(glob.glob(f'Image/{i}_*.jpg')[0])
            img2 = cv2.imread(glob.glob(f'Image/{i + 1}_*.jpg')[0])

            heng1 = np.hstack((img1, img2))

            img3 = cv2.imread(glob.glob(f'Image/{i + 2}_*.jpg')[0])
            img4 = cv2.imread(glob.glob(f'Image/{i + 3}_*.jpg')[0])

            heng2 = np.hstack((img3, img4))

            cv2.imwrite(f"{Img}/hstack_{i}_{i + 1}.jpg", heng1)
            cv2.imwrite(f"{Img}/hstack_{i + 2}_{i + 3}.jpg", heng2)

            img5 = cv2.imread(f"{Img}/hstack_{i}_{i + 1}.jpg")
            img6 = cv2.imread(f"{Img}/hstack_{i + 2}_{i + 3}.jpg")

            hebing = np.vstack((img5, img6))

            cv2.imwrite(f"{Image_save}/compose_{i}_{i + 1}_{i + 2}_{i + 3}.jpg", hebing)

            logging.info(f"{Image_save}/compose_{i}_{i + 1}_{i + 2}_{i + 3}.jpg  拼接并保存成功！\n\n")

        logging.info(f"共合成 {int(num / 4)} 个 两行两列的 .jpg 图片\n")

    else:
        logging.info(f"Image 文件夹下的 .jpg 图片格式的文件个数必须为4的倍数")
        exit()


image_compose()
