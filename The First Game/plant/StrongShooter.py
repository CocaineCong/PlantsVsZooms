import pygame  # 创建一个Stronger豌豆射手的一个类，以便加载图片


class StrongShooter:
    def __init__(self):
        self.images = [pygame.image.load('D:\PycharmProjects\PyGame\The First Game\photo\plant\strong_wd\{}.Png'.format(i)) for i in range(15)]
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 100, 100
        self.zone=(0,0)