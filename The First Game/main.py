import pygame, sys  # system的缩写
from plant.peashooter import Peashooter
from plant.StrongShooter import StrongShooter
from plant.Sun_flower import SunFlower

pygame.init()  # pygame初始化

size = width, height = 1200, 600
screen = pygame.display.set_mode(size)  # display播放，set_mode设置模型，就可以设置出这种大小的模型,主screen
pygame.display.set_caption("The First Game")  # 设置这个游戏的titlie
bg_path = r"D:\PycharmProjects\PyGame\The First Game\photo\BackGround\BG0.jpg"  # 设置背景图
backgroup = pygame.image.load(bg_path).convert()  # 加载背景图


# 主函数
def main():
    peashooter = Peashooter()
    sunflower=SunFlower()
    strongshooter=StrongShooter()
    block = pygame.time.Clock()  # 刷新率
    index = 0
    while 1:  # 让窗口一直循环
        block.tick(20)  # 刷新率 FPS
        screen.blit(backgroup, (0, 0))  # 在主screen下绘制背景图片
        if index > 13:  # 循环图片
            index = 0
        screen.blit(peashooter.images[index % 13], peashooter.rect)  # 绘制豌豆射手,多图片绘制，一帧一帧绘制
        screen.blit(sunflower.images[index % 15], sunflower.rect)  # 绘制太阳花射手,多图片绘制，一帧一帧绘制
        screen.blit(strongshooter.images[index % 15], strongshooter.rect)  # 绘制stronger豌豆射手,多图片绘制，一帧一帧绘制

        pygame.display.update()  # 这样不能退出，每次都是要终止命令
        for event in pygame.event.get():  # 加上事件之后就是可以从右上角退出
            if event.type == pygame.QUIT:
                sys.exit()

        index += 1


if __name__ == '__main__':
    main()
