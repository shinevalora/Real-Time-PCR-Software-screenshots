# _*_coding:utf-8_*_
#  作者    : shinevalora
#  创建时间: 2019/9/8  20:13


def screenshots():
    from PIL import ImageGrab, ImageFont, ImageDraw

    ttfont = ImageFont.truetype(r"C:\Windows\Fonts\Ebrima.ttf", 26)

    text = ['NTC', 'WT', 'MU', 'HET']

    # path2=os.makedirs('data1',exist_ok=True)


    for i in range(1,13):

        your_choice = int(input("{1:'NTC',2:'WT',3:'MU',4:'HET'}:"))

        # #(left, upper, right, lower)-tuple
        img = ImageGrab.grab(bbox=(238, 320, 842, 725))

        draw = ImageDraw.Draw(img)

        draw.text((120, 80), text[your_choice-1], fill=(0, 0, 0), font=ttfont, align='left')


        img.save(f'data/{i}_{text[your_choice-1]}.jpg')


# screenshots()


# import os
# import shutil
#
#
# path1='data1'
# path2='data1/data'
#
#
# file_list=os.listdir('data')
#
# print(file_list)
#
#
# if len(os.listdir('data'))>4:
#     print(os.listdir('data')[:4])



# 定义图像拼接函数
def image_compose():
    from PIL import Image

    import os

    image_path = 'data/'  # 图片集地址

    image_row = 2  # 图片间隔，也就是合并成一张图后，一共有几行
    image_column = 2  # 图片间隔，也就是合并成一张图后，一共有几列

    # 获取图片集地址下的所有图片名称
    image_names = [name for name in os.listdir(image_path)]

    # # 简单的对于参数的设定和实际图片集的大小进行数量判断
    # if len(image_names) != image_row * image_column:
    #     raise ValueError("合成图片的参数和要求的数量不能匹配！")

    image_height, image_width = Image.open(image_path + image_names[0]).size

    to_image = Image.new('RGB', (image_column * image_height, image_row * image_width))  # 创建一个新图

    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, image_row + 1):
        for x in range(1, image_column + 1):
            print('image_column * y:',image_column * y)
            # print(x)
            print('image_names[image_column * y + x ]:',image_names[image_column * y + x ])
            from_image = Image.open(image_path + image_names[image_column * y + x ])    #.resize((image_heiht, image_width), Image.ANTIALIAS)
            # print('from_image:',from_image)
            to_image.paste(from_image, ((x - 1) * image_height, (y - 1) * image_width))

    return to_image.save("result_smooth_white_4.jpg")  # 保存新图


image_compose()


















