# 1.ゲームの準備をする
from numpy import block
import pygame as pg, sys
from pygame.locals import *
from pygame import mixer
import random
pg.init()
screen = pg.display.set_mode((800, 600))

## プレイヤーデータ
myimgR = pg.image.load("images\playerR.png")
myimgU = pg.image.load("images\playerU.png")
myimgD = pg.image.load("images\playerD.png")
myimgR = pg.transform.scale(myimgR, (40, 50))
myimgL = pg.transform.flip(myimgR, True, False)
myimgU = pg.transform.scale(myimgU, (40, 50))
myimgU = pg.transform.flip(myimgU, True, False)
myimgD = pg.transform.scale(myimgD, (40, 50))
myimgD = pg.transform.flip(myimgD, True, False)
myrect = pg.Rect(50,200,40,50)
# pg.Rect(<上からの開始位置>,<左からの開始位置>,<横の長さ>,<縦の長さ>)
# stage position
blocks = [
        pg.Rect(500,350,100,30),
        pg.Rect(200,450,100,30),
        pg.Rect(350,400,100,30),
        pg.Rect(700,560,400,40),
        pg.Rect(0,560,600,40),
        pg.Rect(650,490,50,30),
        pg.Rect(650,250,200,40)] 

#load images
sun_img = pg.image.load('img/sun.png')
bg_img = pg.image.load('img/sky.png')
restart_img = pg.image.load('img/restart_btn.png')
start_img = pg.image.load('img/start_btn.png')
exit_img = pg.image.load('img/exit.png')
grass_img = pg.image.load('img/grass.png')
rumput_img= pg.image.load('img/rumpuyt.png')
clouds_img= pg.image.load('images/Nice.png')

# 足場用の画像
grass_list = [pg.transform.scale(rumput_img, (100,30)),
            pg.transform.scale(rumput_img, (100,30)),
            pg.transform.scale(rumput_img, (100,30)),
            pg.transform.scale(rumput_img, (400,40)),
            pg.transform.scale(rumput_img, (600,40)),
            pg.transform.scale(rumput_img, (50,30)),
            pg.transform.scale(clouds_img, (150,40))]
## メインループで使う変数
rightFlag = True
UpFlag = True
DownFlag = True
LeftFlag = True
abc = 0

#load images
Background = pg.transform.scale(bg_img, (800,600))
sun_img = pg.image.load('img/sun.png')
sun_img = pg.transform.scale(sun_img, (350,200))
grass_img = pg.image.load('img/grass.png')
grass_img = pg.transform.scale(grass_img, (800,150))
door_img= pg.transform.scale(exit_img, (40,50))

on_floor = False    # 地面にいるか？
jumping = False

y_gravity = 0.6
jump_Height = 15 
y_velocity = jump_Height

## ゲームステージ
def gamestage():
    pg.time.delay(20)
    global abc, blocks, myrect, on_floor, jumping, y_gravity, jump_Height, y_velocity
    # 3.画面を初期化する
    screen.fill(( 0,0,0))
    vx = 0
    vy = 5
    ##background image
    screen.blit(Background,(0,0))
    screen.blit(sun_img, (100, 20))
    screen.blit(bg_img, (800, 600))
    screen.blit(door_img, (710, 200))
    # screen.blit(grass_img,(0,500))
    # 4.ユーザーからの入力を調べる
    key = pg.key.get_pressed()
    # 5.絵を描いたり、判定したりする
    if key[pg.K_RIGHT]:
        vx = 4
        if on_floor:
            vx = 5
            vy = 0 
        abc=0

    if key[pg.K_LEFT]:
        vx = -4
        if on_floor:
            vx = -5
            vy = 0
        abc = 1

    if key[pg.K_UP]:
        vy = -4
        abc = 2
    
    if key[pg.K_DOWN]:
        vy = 4
        abc = 3
    if key[pg.K_SPACE]:
        jumping = True
        vy = 0
        abc = 2
    
  
## プレイヤーの処理
    myrect.x += vx
    myrect.y += vy
    # 足場との当たり判定
    if myrect.collidelist(blocks) != -1:
        if jumping:
            vy = 6
        y_velocity = jump_Height
        jumping = False
        on_floor = True
        myrect.x -= vx
        myrect.y -= vy
    else:
        on_floor = False
    # 足場
    for i, block in enumerate(blocks):
        screen.blit(grass_list[i],block)

    if jumping:
        # print("Xの位置：",myrect.x,"Yの位置",myrect.y)
        # print("vy：",vy)
        myrect.y -= y_velocity
        y_velocity -= y_gravity
        # if y_velocity < -jump_Height:
        #     y_velocity = jump_Height
        #     jumping = False

    if abc== 0:
        screen.blit(myimgR, myrect)
    if abc== 1:
        screen.blit(myimgL, myrect)
    if abc== 2:
        screen.blit(myimgU, myrect)
    if abc== 3:
        screen.blit(myimgD, myrect)


    myrect.x = myrect.x + 0
    if myrect.x >= 800:
        myrect.x =-100
    myrect.y = myrect.y + 0
    if myrect.y >= 600:
        myrect.y =-100



def pushstage():
    blocks.appends(myrect(200,100,100,300))
def createstage ():
    for b in blocks:
        screen.blit(b,myrect)

def colliderectstage(mychar):
    for b in block:
        if mychar.colliderect(b):
            myrect.x -= 10
            myrect.y -= 10

def update(self):
    """スプライトの更新"""



# 2.この下をずっとループする
while True:
    gamestage()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
  
    
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
