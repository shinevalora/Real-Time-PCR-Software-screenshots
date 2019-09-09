# _*_coding:utf-8_*_
#  作者    : shinevalora
#  创建时间: 2019/9/8  20:13


def screenshots(bbox=(238, 320, 842, 725)):
    from PIL import ImageGrab, ImageFont, ImageDraw

    ttfont = ImageFont.truetype(r"C:\Windows\Fonts\Ebrima.ttf", 26)

    text = ['NTC', 'WT', 'MU', 'HET']

    print('截屏区域为：(left, upper, right, lower)-tuple:', bbox)

    num = int(input('请输入你想要截多少张图:'))

    for i in range(1, num + 1):
        your_choice = int(input("{1:'NTC',2:'WT',3:'MU',4:'HET'}:"))

        # #bbox(left, upper, right, lower)-tuple
        img = ImageGrab.grab(bbox=bbox)

        draw = ImageDraw.Draw(img)

        draw.text((120, 80), text[your_choice - 1], fill=(0, 0, 0), font=ttfont, align='left')

        img.save(f'Image/{i}_{text[your_choice - 1]}.jpg')


screenshots()
