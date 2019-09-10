# _*_coding:utf-8_*_
#  作者    : shinevalora
#  创建时间: 2019/9/8  20:13

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")


def screenshots(bbox=(238, 320, 842, 725)):
    from PIL import ImageGrab, ImageFont, ImageDraw

    ttfont = ImageFont.truetype(r"C:\Windows\Fonts\Ebrima.ttf", 26)

    text = ['NTC', 'WT', 'MU', 'HET']

    # '截屏区域为：(left, upper, right, lower)-tuple:', bbox)

    end_num = int(input('请输入你想要截多少张图:'))
    start_num=int(input('请输入截图图片的起始数：1-则是从 1_*.jpg   , 2 -则是从 2_*.jpg开始:'))

    for i in range(start_num, start_num+end_num):
        try:
            your_choice = int(input("只能输入 1 2 3 4------{1:'NTC',2:'WT',3:'MU',4:'HET'}: "))

            # #bbox(left, upper, right, lower)-tuple
            img = ImageGrab.grab(bbox=bbox)

            draw = ImageDraw.Draw(img)

            draw.text((120, 80), text[your_choice - 1], fill=(0, 0, 0), font=ttfont, align='left')

            img.save(f'Image/{i}_{text[your_choice - 1]}.jpg')

            logging.info(f'Image/{i}_{text[your_choice - 1]}.jpg 保存成功！')

        except:
            logging.info('你输入有误，请重新输入')


screenshots()
