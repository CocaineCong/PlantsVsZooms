import pygame  # 创建一个豌豆射手的一个类，以便加载图片


class Peashooter:
    def __init__(self):
        self.images = [pygame.image.load('photo\plant\init_wd\{:d}.Png'.format(i)) for i in range(13)]
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 300, 300
        self.zone=(0,0)