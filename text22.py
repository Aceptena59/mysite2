# 1.ゲームの準備をする
from tokenize import maybe
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
myrect = pg.Rect(100,100,100,150)
myg = pg.Rect(100,400,200,150)
myb = pg.Rect(200,500,200,150)
img1 = pg.image.load("images/plane.jpg")
img1 = pg.transform.scale(img1,(150,150))
#img2 = pg.image.load("images/plane.jpg")
#img2 = pg.transform.scale(img2,(150,150))
# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    myrect.x = myrect.x + 1
    if myrect.x == 800:
        myrect.x=-100
    if myg.x == 800:
        myg.x=-100
    myg.x = myg.x + 2
    if myb.x == 800:
        myb.x= -100
    myb.x = myb.x - 2
    pg.draw.rect(screen, pg.Color("RED"), myrect )
    screen.blit(img1, myg)
    screen.blit(img1, myb)
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()