import os
from PIL import Image


def canvas_img(img):
    # for o in glob.glob('*.png'):
    img1 = Image.open(img)

    He =   [ 39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17 ]
    target = Image.new('RGB', (260, 160))
    for c in range(0, 52):
        _ = He[c] % 26 * 12 + 1
        f = 80 if He[c] > 25 else 0
        box1 = (_, f, _ + 10, f + 80)
        region = img1.crop(box1)
        tmp = 80 if c > 25 else 0
        target.paste(region, (c % 26 * 10, tmp))
    target.save(os.path.splitext(img)[0] + '1.png')

    return os.path.splitext(img)[0] + '1.png'


class SlideCrack(object):
    def __init__(self, gap_img, bg):
        self.gap_img = gap_img
        self.bg = bg

    @staticmethod
    def pixel_is_equal(image1, image2, x, y):
        """
        判断两张图片的像素是否相等,不相等即为缺口位置
        :param image1:
        :param image2:
        :param x:  x坐标
        :param y: y 坐标
        :return:
        """
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, image1, image2):
        """
        获取缺口位置
        :param image1:完整图片
        :param image2: 带缺口的图片
        :return:
        """
        left = 50
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.pixel_is_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def run(self):
        image1 = Image.open(self.bg)
        image2 = Image.open(self.gap_img)
        gap = self.get_gap(image1, image2)
        return gap


def get_distance(img1, img2):
    img11 = canvas_img(img1)
    img22 = canvas_img(img2)

    gt = SlideCrack(img11, img22)
    val = gt.run()
    return val

if __name__ == '__main__':
    img1 = "bg.png"
    img2 = "fullbg.png"
    distance = get_distance(img1, img2)
    print(distance)