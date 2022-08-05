#从精灵模块中导入所有命令
from sprites import *

# 1.笑脸变色游戏

#新建一个造型
images = 'res/smiles.png','res/smlie.png','res/dragon.png'
#新建一个人物
cat = Sprite(shape=images)
#播放音乐(好像不生效)
cat.play('laughing.wav')
#条件成立时执行（while循环）
'''
while True:
    #往前走10
    cat.fd(10)
    #播放下一个造型
    cat.nextcostume()
    #等待时间0.5
    cat.wait(0.5)
'''
#条件成立时执行（for循环）
for i in range(5):
    #往前走10
    cat.fd(10)
    #播放下一个造型
    cat.nextcostume()
    #等待时间0.5
    cat.wait(0.5)

# 2.弹球游戏
def ballgame(self):
    ball = Sprite(1)
    while True:
        ball.fd(0.1)
        ball.bounce_on_edge()


