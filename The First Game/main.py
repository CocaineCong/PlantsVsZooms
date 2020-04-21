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
card_slot = pygame.image.load(r'D:\PycharmProjects\PyGame\The First Game\photo\cards\card.png').convert()  # 放入卡槽
card_sunflower = pygame.image.load(
    r'D:\PycharmProjects\PyGame\The First Game\photo\cards\sunflower_cards.png').convert()  # 放入sunflower卡片
card_peershooter = pygame.image.load(
    r'D:\PycharmProjects\PyGame\The First Game\photo\cards\peershooter_cards.png').convert()  # 放入peershooter卡片

card_rect = card_sunflower.get_rect()  # 获取到卡片的大小
card_sunflower = pygame.transform.scale(card_sunflower,
                                        (int(card_rect.width * 0.8), int(card_rect.height * 1.0)))  # 改变卡片的大小

sun_num = '0'  # 阳光数
font = pygame.font.SysFont('arial', 20)  # 设置字体和大小
fontImg = font.render(sun_num, True, (0, 0, 0))  # 000是颜色


# 主函数
def main():
    p1 = []
    card_store = []  # 这个是存放卡片的列表 ,只能是一个一个列表，因为只能是只有一个卡片在移动
    # peashooter = Peashooter()
    # sunflower = SunFlower()
    strongshooter = StrongShooter()
    peaList = []
    p1=[]
    SunFlowerList=[]
    block = pygame.time.Clock()  # 刷新率
    index = 0
    is_pick = False  # 是否被选中 原始的状态都是没有点击的
    # 临时存放pea
    pick_type=None
    while 1:  # 让窗口一直循环
        block.tick(20)  # 刷新率 FPS
        screen.blit(backgroup, (0, 0))  # 在主screen下绘制背景图片
        screen.blit(card_slot, (280, 0))  # 在主screen下绘制卡槽
        screen.blit(card_sunflower, (350, 10))  # 绘制cards
        screen.blit(card_peershooter, (410, 10))  # 绘制cards
        screen.blit(fontImg, (310, 68))  # 绘制sun_num
        press = pygame.mouse.get_pressed()  # 模拟鼠标的点击（0，0，0）   （1，0，0）左键 滑轮 右键
        x, y = pygame.mouse.get_pos()  # 鼠标的坐标
        if index > 13:  # 循环图片
            index = 0
        # screen.blit(peashooter.images[index % 13], peashooter.rect)  # 绘制豌豆射手,多图片绘制，一帧一帧绘制
        # screen.blit(sunflower.images[index % 15], sunflower.rect)  # 绘制太阳花射手,多图片绘制，一帧一帧绘制
        # screen.blit(strongshooter.images[index % 15], strongshooter.rect)  # 绘制stronger豌豆射手,多图片绘制，一帧一帧绘制

        for p in card_store:  # 将放在卡片数组中的植物卡牌显示出来
            screen.blit(p.images[0], (x, y))  # 可以根据鼠标的移动来进行显示
            # screen.blit(l.images[0], (x, y))  # 可以根据鼠标的移动来进行显示   stronger_shooter以后再补充，没有相应的图片

        for p in p1:  # 将放在卡片数组中的植物卡牌显示出来
            screen.blit(p.images[0], p.zone)
        for pea in peaList:  # 将放在卡片数组中的植物卡牌显示出来
            screen.blit(pea.images[index % 13], pea.zone)
        for sunFlower in SunFlowerList:  # 将放在卡片数组中的植物卡牌显示出来
            screen.blit(sunFlower.images[index % 15], sunFlower.zone)

        pygame.display.update()  # 渲染窗口，这样不能退出，每次都是要终止命令

        for event in pygame.event.get():  # 加上事件之后就是可以从右上角退出
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:  # 模拟点击
                # print(x,y)
                if not is_pick:
                    if 350 <= x <= 350 + card_sunflower.get_rect().width and 10 <= y <= 10 + card_sunflower.get_rect().height:  # 到太阳花的地方
                        if press[0]:  # 这个就是左击 如果点击的话就是会在控制台返回这个是数据，就会执行这个函数
                            # print('hit pea card')
                            p = SunFlower()
                            card_store.append(p)  # 一点击就是添加到其中 就是会不会添加图片进来
                            is_pick = True  # 用了之后就要将其变成状态
                            pick_type='pea'


                    # press('pea')  # 当这个鼠标到这个区域的时候就会在控制台打出这个pea
                    elif 410 <= x <= 410 + card_peershooter.get_rect().width and 10 <= y <= 10 + card_peershooter.get_rect().height:  # 到豌豆选手的地方
                        if press[0]:  # 如果点击的话就是会在控制台返回这个是数据，就会执行这个函数
                            # print('hit pea card')
                            p = Peashooter()
                            pick_type='flower'
                            card_store.append(p)  # 将这个类里面的卡片放到卡片当中
                            is_pick = True  # 因为已经点击了所以要改变状态
                    # elif 410<= x <= 410 + card_StrongShooter.get_rect().width and 10 <= y <= 10 + card_StrongShooter.get_rect().height:  # 到stronger豌豆选手的地方
                    #    if press[0]:  # 如果点击的话就是会在控制台返回这个是数据，就会执行这个函数
                    #        # print('hit pea card')
                    #        l = StrongShooter
                    #        Strong_Shooter.append(l)

                if is_pick:
                    # 259 280  330 275
                    if 330 <= x <= 405 and 186 <= y <= 272:  # 放置的坐标
                        if pick_type=='pea':
                            p = Peashooter()
                            # print('xxxx')  # 测试用
                            p.zone(330, 180)
                            p1.append(p)
                            if press[0]:
                                peaList.append(p)
                                card_store.clear()  # 直接将其这个列表清空就可以取消了
                                p1.clear()
                                is_pick=False
                        elif pick_type=='flower':
                            f = SunFlower()
                            # print('xxxx')  # 测试用
                            f.zone(330, 180)
                            p1.append(f)
                            if press[0]:
                                SunFlowerList.append(f)
                                card_store.clear()  # 直接将其这个列表清空就可以取消了
                                p1.clear()
                                is_pick = False


                    else:
                        p1.clear()

                    if press[2]:  # 这个就是右击
                        card_store.clear()  # 直接将其这个列表清空就可以取消了
                        is_pick = False

        index += 1


if __name__ == '__main__':
    main()
