# _*_coding:utf-8_*_
#  作者    : shinevalora
#  创建时间: 2019/9/8  20:13


# 定义图像拼接函数
def image_compose():
    import os
    num = len(os.listdir('Image/'))

    print(num)

    import cv2
    import numpy as np

    for i in range(1, num + 1, 4):
        img1 = cv2.imread(f"{i}.jpg")
        img2 = cv2.imread(f"{i + 1}.jpg")

        heng1 = np.hstack((img1, img2))

        img3 = cv2.imread(f"{i + 2}.jpg")
        img4 = cv2.imread(f"{i + 3}.jpg")

        heng2 = np.hstack((img3, img4))

        cv2.imwrite(f"hstack_{i}_{i + 1}.jpg", heng1)
        cv2.imwrite(f"hstack_{i + 2}_{i + 3}.jpg", heng2)

        img5 = cv2.imread(f"hstack_{i}_{i + 1}.jpg")
        img6 = cv2.imread(f"hstack_{i + 2}_{i + 3}.jpg")

        hebing = np.vstack((img5, img6))

        cv2.imwrite(f"Image_save/compose_{i}_{i + 1}_{i + 2}_{i + 3}.jpg", hebing)

        cv2.waitKey(10)

# image_compose()





