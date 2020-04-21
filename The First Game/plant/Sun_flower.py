import pygame  # 创建一个太阳花的一个类，以便加载图片


class SunFlower:
    def __init__(self):
        self.images = [pygame.image.load('D:\PycharmProjects\PyGame\The First Game\photo\plant\sunflower\{}.Png'.format(i)) for i in range(15)]
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 200, 300
        self.zone=(0,0)