from pygame import*
w=400
h=300

win = display.set_mode((w,h))
class Alfa(sprite.Sprite):
    def __init__(self,x,y,h,w,image_name,speed):
        super().__init__()
        self.image = image.load(image_name)
        self.rect = Rect(w,h,y,x)
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

ball = Alfa(100,100,50,50,'pixil-frame-0 (2).png',0)
while True:
    
    for e in event.get():
        if e.type == 12:
            exit()
    win.fill((229,190,1))
    ball.reset()
    display.update()

